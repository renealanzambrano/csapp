from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Cliente import views
urlpatterns = [
    re_path(r'^lista2/$', views.ClienteList.as_view()),
    re_path(r'^mcuCliente/(?P<pk>\d+)/$',views.ClienteUpgrade.as_view())
]