from django.shortcuts import render
from rest_framework import viewsets
from restapi.serializers import ProductSerializer
from restapi.models import Product
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('created').reverse()
    serializer_class = ProductSerializer



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