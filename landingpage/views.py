from django.shortcuts import render
from django.views.generic import TemplateView, View
# Create your views here.
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .nutrition import UpcFood
import os
import json

envs = {
    'TOKEN' : os.environ.get('api_key', ''),
    'ID': os.environ.get('api_id', ''),
    }

if '' in envs.values(): ### in one value isn't set
    raise ImproperlyConfigured('landing_page.views: Set all values in the .env or with heroku:config.')

class HomeView(TemplateView):
    template_name = 'landing_page.html'


class UPCAPI(View):
    http_method_names = [u'post']

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UPCAPI, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Custom method for listview
        """
        upc_code = request.POST.get('upcCode', 'not works')

        api_key = os.environ.get('api_key', '')  #api_key, 
        api_id = os.environ.get('api_id', '') #api_id)
        
        # u = UpcFood(upc_code, api_key, api_id)
        # context = u.get_food_item()

        # context.update({'request': 'ok'})

        context = {'ok': True}

        return HttpResponse(json.dumps(context), content_type = "application/json") 



