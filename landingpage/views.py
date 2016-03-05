from django.shortcuts import render
from django.views.generic import TemplateView, View
# Create your views here.

from .nutrition import UpcFood


class HomeView(TemplateView):
    template_name = 'landing_page.html'


class UPCAPI(View):
    http_method_names = [u'post']

    def post(self, request, *args, **kwargs):
        """
        Custom method for listview
        """
        email = request.POST.get('upcCode', 'not works')

        u = UpcFood(upc_code, api_key, api_id)

        context = u.convert_dict_to_attributes()

        context.update({'item':'works'})

        return HttpResponse(json.dumps(context), content_type = "application/json")  

