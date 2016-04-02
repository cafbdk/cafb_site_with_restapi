"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))


Inlcude this in your project urls.py

url(r'^slack/', include('django_slack_invite.urls'))

"""
from django.conf.urls import url
from .views import HomeView, UPCAPI, UPCFoundView, UPCNotFoundView, TryAgainView, TakePicView, SkipView, WellnessYesView, WellnessNoView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^upc_found/$',UPCFoundView.as_view(), name='upc_found'),
    url(r'^upc_not_found/$',UPCNotFoundView.as_view(), name='upc_not_found'),
    url(r'^try_again/$',TryAgainView.as_view(), name='try_again'),
    url(r'^take_pic/$',TakePicView.as_view(), name='take_pic'),
    url(r'^skip/$',SkipView.as_view(), name='skip'),
    url(r'^wellness_yes/$',WellnessYesView.as_view(), name='wellness_yes'),
    url(r'^wellness_no/$',WellnessNoView.as_view(), name='wellness_no'),

        url(r'upc/', UPCAPI.as_view()),



]
