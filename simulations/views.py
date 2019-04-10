from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
import json

from simulations.models import PowerLog
from simulations.serializers import PowerLogSerializer

# Task manager 
from simulations.tasks import *
generateData.delay()

class simulations(generics.ListCreateAPIView):
	"""This view class handles creating or geting list of PowerLogs """
	queryset = PowerLog.objects.all()
	serializer_class = PowerLogSerializer

	def get_queryset(self):
		_response = PowerLog.objects.order_by('-registered_at')
		return _response

