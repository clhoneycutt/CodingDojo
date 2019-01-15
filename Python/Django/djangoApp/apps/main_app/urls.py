from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<number>\d+)$', views.show, name='show'),
    url(r'^(?P<number>\d+)/edit', views.edit, name='edit'),
    url(r'^(?P<number>\d+)/delete', views.destroy, name='destroy'),
    url(r'^', views.index, name='index'),
]