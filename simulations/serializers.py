from rest_framework import serializers

# Project settings 
from django.conf import settings

from simulations.models import PowerLog

# PowerLog
class PowerLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = PowerLog
		fields = ('id', 'power' , 'duration' , 'pv', 'registered_at' )

		