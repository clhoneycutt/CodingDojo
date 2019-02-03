from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/new', views.new, name="new"),
    url(r'^/create', views.createBook, name="create"),
    url(r'^/(?P<bookid>\d+)/addreview', views.addReview, name="addReview"),
    url(r'^/(?P<bookid>\d+)/show', views.show, name="show"),
    url(r'^/(?P<bookid>\d+)/(?P<reviewid>\d+)/destroy', views.deleteReview, name="destroy"),
    url(r'^', views.index, name="index"),
    # url(r'^update/', views.update, name="update"),
    # url(r'^success/', views.success, name="success"),
    # url(r'^edit/', views.edit, name="edit"),
]


# /(?P<bookid>\d+)