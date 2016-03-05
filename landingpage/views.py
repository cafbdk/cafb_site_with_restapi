from django.shortcuts import render
from django.views.generic import TemplateView, View
# Create your views here.
from django.core.exceptions import ImproperlyConfigured

from .nutrition import UpcFood
import os

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
        upc_code = request.POST.get('upcCode', 'not works')

        api_key = os.environ.get('api_key', '')  #api_key, 
        api_id = os.environ.get('api_id', '') #api_id)
        
        u = UpcFood(upc_code, api_key, api_id)
        context = u.food_info()

        context.update({'upc_code': upc_code, 'request': 'ok'})

        return HttpResponse(json.dumps(context), content_type = "application/json") 



