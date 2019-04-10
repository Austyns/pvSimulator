from django.conf.urls import  url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from simulations import views

from rest_framework.schemas import get_schema_view

urlpatterns = [
            url(r'^consumptions/$', views.simulations.as_view()),
        ]
urlpatterns = format_suffix_patterns(urlpatterns)