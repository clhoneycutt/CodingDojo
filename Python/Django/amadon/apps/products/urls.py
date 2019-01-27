from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^purchase', views.purchase, name='purchase'),
    url(r'^thankyou', views.thankyou, name='thankyou'),
    url(r'^', views.index, name='index'),
]