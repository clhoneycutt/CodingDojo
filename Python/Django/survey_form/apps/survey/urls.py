from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^result', views.result, name="result"),
    url(r'^process', views.process, name="process"),
    url(r'^', views.index, name="main")
]
