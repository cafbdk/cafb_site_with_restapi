from django.shortcuts import render
from django.views.generic import ListView, View
# Create your views here.
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from restapi.models import Product
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


from .nutrition import UpcFood
import os
import json
import unirest


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
        list_products = Product.objects.all()
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
        upc_code = request.POST.get('upc', 'not finding upc code')

        api_key = os.environ.get('api_key', '')  #api_key, 
        api_id = os.environ.get('api_id', '') #api_id)
        
        # u = UpcFood(upc_code, api_key, api_id)
        # context = u.get_food_item()

        context = {'request': 'ok', 'upc_requested' : upc_code}

        # response = unirest.get("https://api.nutritionix.com/v1_1/item?upc={upc}&appId={apiID}&appKey={apiKey}".format(
                # apiID=api_id, apiKey=api_key, upc=upc_code),
                #                headers={"Accept": "application/json"})

        # food_info = response.body
        # new_dict_keys = map(lambda x:str(x).replace('nf_',''), food_info.keys())
        # context = dict(zip(new_dict_keys, food_info.values()))
        # context.update({'upc_code_requested': upc_code})

        return HttpResponse(json.dumps(context), content_type = "application/json") 



