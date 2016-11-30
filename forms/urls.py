from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^show/$', views.showForm),
    url(r'^login/$', views.showLogin),
    url(r'^home/$', views.showLogin),
    url(r'^logout/$', views.logout_view),
    url(r'^home/$', views.home),

]