from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login, name="login"),
    url(r'^register/', views.register, name="register"),
    url(r'^success/', views.success, name="success"),
    url(r'^logout/', views.logout, name="logout"),
    url(r'^', views.index, name="index"),
]
