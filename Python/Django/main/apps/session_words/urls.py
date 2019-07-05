from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add_word', views.add_word, name="add_word"),
    url(r'^clear_session', views.clear_session, name="clear_session"),
    url(r'^', views.index, name="index"),
]