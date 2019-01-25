from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^destroy', views.destroy, name="destroy"),
    url(r'^remove', views.remove, name="remove"),
    url(r'^create', views.create, name="create"),
    url(r'^', views.index, name="index"),
]