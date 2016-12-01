from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^show/$', views.showForm, name='showForm'),
    url(r'^login/$', views.showLogin, name='showLogin'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout/$', views.logout_view, name='logout'),
]