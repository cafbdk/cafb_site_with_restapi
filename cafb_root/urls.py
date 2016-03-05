from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'cafb_root.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('landingpage.urls')),
    # url(r'^api-auth/', include('restapi.urls', namespace='rest_framework'))

]
