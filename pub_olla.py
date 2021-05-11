import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
import random


def conectado(client, userdata, flags, rc):
	print('Conectado al publicador de olla')

def main():
	client = paho.mqtt.client.Client("Olla", False)
	client.qos = 0
	client.connect(host = 'localhost')
	max_temp = 150.0
	min_temp = 0.0
	tiempo = datetime.datetime.now().replace(minute = 0, second=0, microsecond = 0)
	while(True):
		temp_actual = random.uniform(min_temp, max_temp)				
		datos = {
			"dateTime": str(tiempo),
			"temperatura": str(round(temp_actual,2))
		}
		client.publish('casa/cocina/olla',json.dumps(datos),qos = 0)		
		print(datos)
		tiempo += datetime.timedelta(minutes=1)
		if(temp_actual >= 100):
			datos2 = {
			"dateTime": str(tiempo),
			"mensaje": "El agua hirvio"
			}
			client.publish('casa/cocina/olla',json.dumps(datos2),qos = 0)
			print(datos2)
		time.sleep(1)

if __name__ == '__main__':
	main()
	sys.exit(0)