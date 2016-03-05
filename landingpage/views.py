from django.shortcuts import render
from django.views.generic import TemplateView, View
# Create your views here.
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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

class HomeView(TemplateView):
    template_name = 'landing_page.html'


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

        context = {'request': 'ok', 'upc_requested' : request}

        # response = unirest.get("https://api.nutritionix.com/v1_1/item?upc={upc}&appId={apiID}&appKey={apiKey}".format(
                # apiID=api_id, apiKey=api_key, upc=upc_code),
                #                headers={"Accept": "application/json"})

        # food_info = response.body
        # new_dict_keys = map(lambda x:str(x).replace('nf_',''), food_info.keys())
        # context = dict(zip(new_dict_keys, food_info.values()))
        # context.update({'upc_code_requested': upc_code})

        return HttpResponse(json.dumps(context), content_type = "application/json") 



