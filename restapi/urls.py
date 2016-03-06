from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    # Examples:
    url(r'^', include(router.urls)),
    # url(r'^auth/', include('restapi.urls', namespace='rest_framework'))
    url(r'^auth/upc=(?P<upccode>[0-9]+)/$', views.ProductDetail.as_view()),


]


# urlpatterns = format_suffix_patterns(urlpatterns)