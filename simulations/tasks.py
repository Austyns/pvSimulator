from celery.decorators import task, periodic_task
from celery.task.schedules import crontab
from django.db import connection
import json
from simulations.views import *
from datetime import timedelta

from random import seed
from random import randint
import datetime
from decimal import Decimal

current_time = datetime.datetime.now()
# seed random number generator
seed(1)

@task()
def doSomeTask():
	print('x + y')

def generateConsumption():
	return randint(0, 9000)

@task()
def generateData():
	# do something
	# print('genetating data')
	print(randint(0, 9000))
	# generate random meter reading value
	meter_reading = generateConsumption()
	# assuming that meter reading is sent every 15 minutes
	duration = 15 / 60 # convert to hour for standard PV calculation in KWh
	pv = meter_reading*duration
	# write output to file 
	current = {}
	current["meter_reading"] = meter_reading
	current["duration"] = duration
	current["pv"] = pv
	file_name = datetime.datetime.utcnow()
	with open('outputs/'+str(file_name)+'.txt', 'w') as outputFile:
		outputFile.write(json.dumps(current))
	# push to the database
	query_data = []
	query_data = [(Decimal('%.2f' % meter_reading), Decimal('%.2f' % duration), Decimal('%.4f' % pv), str(datetime.datetime.now()) )]
	# print((query_data))
	# print(type(query_data))
	query = """INSERT INTO simulations_powerlog (power, duration, pv, registered_at) VALUES ( ?, ?, ?, ? ) """
	with connection.cursor() as cursor:

		res = cursor.executemany(query, query_data)
		connection.commit()
		print(res)
		print("Done")