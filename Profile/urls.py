from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Profile import views
urlpatterns = [
    re_path(r'^lista3/$', views.ProfileList.as_view()),
    re_path(r'^mcuProfile/(?P<pk>\d+)/$',views.ProfileUpgrade.as_view())
]