from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new', views.new), # GET method - view new user form
    url(r'^create', views.create),  # POST method - create user in db
    url(r'^(?P<id>\d+)/edit', views.edit), # GET method - View edit form
    url(r'^(?P<id>\d+)/show', views.show),  # GET method - view user information
    url(r'^(?P<id>\d+)/update', views.update), # POST Method - Update user information
    url(r'^(?P<id>\d+)/destroy', views.destroy), # GET Method - deletes user from database
    url(r'^', views.index), # GET Method - view landing page
]