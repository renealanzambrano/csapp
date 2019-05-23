from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Alumno import views

urlpatterns=[
    re_path(r'^lista1/$', views.AlumnoList.as_view()),
    re_path(r'^mcuAlumno/(?P<pk>\d+)/$',views.AlumnoUpgrade.as_view())
]