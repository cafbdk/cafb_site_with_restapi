from django.shortcuts import render
from django.views.generic import ListView, View, CreateView
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerializer
from .models import Product
from .utils import is_wellness
from .nutrition import UpcFood
import os
import json
import unirest
from django.conf import settings
import csv

envs = {
    'TOKEN' : os.environ.get('api_key', ''),
    'ID': os.environ.get('api_id', ''),
    }

if '' in envs.values(): ### in one value isn't set
    raise ImproperlyConfigured('landing_page.views: Set all values in the .env or with heroku:config.')

class HomeView(ListView):
    model = Product
    template_name = 'landing_page.html'
    context_object_name = "product_list"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        list_products = Product.objects.all().order_by('created').reverse()
        paginator = Paginator(list_products, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_products = paginator.page(page)
        except PageNotAnInteger:
            file_products = paginator.page(1)
        except EmptyPage:
            file_products = paginator.page(paginator.num_pages)

        context['list_products'] = file_products

        return context



class UPCAPI(View):
    http_method_names = [u'post']

    def post(self, request, *args, **kwargs):
        """
        Custom method for listview
        """
        upc_code = request.POST.get('upc_code', 'NONE')

        api_key = os.environ.get('api_key', '')  #api_key,
        api_id = os.environ.get('api_id', '') #api_id)

        try:
            # raise Exception
            obj = Product.objects.filter(gtin_code=upc_code)
            context = {'status': True}
            context.update(obj.values()[0])
            del context['created']
            context.update({'status': True})
            # print context
            PATH = settings.BASE_DIR
            fname  = PATH +'/cafb_main/fixtures/rules.csv'
            with open(fname,'r') as f:
                rules = csv.DictReader(f)
                wellness=is_wellness(response.body,'03',rules)
                context['wellness']=wellness

        except: #Product.DoesNotExist


            response = unirest.get("https://api.nutritionix.com/v1_1/item?upc={upc}&appId={apiID}&appKey={apiKey}".format(
                    apiID=api_id, apiKey=api_key, upc=upc_code),
                                   headers={"Accept": "application/json"})
            if response.code == 200:

                food_info = response.body
                new_dict_keys = map(lambda x:str(x).replace('nf_',''), food_info.keys())
                context = dict(zip(new_dict_keys, food_info.values()))

                # upc_code = int(upc_code)
                obj = Product(gtin_code=upc_code, gtin_name=context['item_name'])
                obj.save()

                context['gtin_name'] = context['item_name']
                context.update({'status': True})

                PATH = settings.BASE_DIR
                fname  = PATH +'/cafb_main/fixtures/rules.csv'
                #time to test the nutrition value
                with open(fname,'r') as f:
                    rules = csv.DictReader(f)
                    wellness=is_wellness(response.body,'03',rules)
                    context['wellness']=wellness
            else:
                context = {'status': False}

        context.update({'gtin_code': upc_code})
        return HttpResponse(json.dumps(context), content_type = "application/json")

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('created').reverse()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(gtin_code=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            # add get or request from another API
            raise Http404


class ProductDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, upccode):
        try:
            return Product.objects.get(gtin_code=upccode)
        except Product.DoesNotExist:
            # add get or request from another API
            raise Http404

    def get(self, request, upccode, format=None):
        product = self.get_object(upccode)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
