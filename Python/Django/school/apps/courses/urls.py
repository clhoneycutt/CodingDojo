from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<course_id>\d+)/destroy/', views.destroy, name="destroy"),
    url(r'^(?P<course_id>\d+)/remove/', views.remove, name="remove"),
    url(r'^create/', views.create, name="create"),
    url(r'^', views.index, name="index"),
]

# (?P<id>\d+)