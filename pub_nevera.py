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
	print('Conectado al publicador de nevera')

def main():
	client = paho.mqtt.client.Client("Nevera", False)
	client.qos = 0
	client.connect(host = 'localhost')
	max_temp = 12.0
	min_temp = 8.0
	max_hielo = 10.0
	min_hielo = 0.0
	tiempo = datetime.datetime.now().replace(minute = 0, second=0, microsecond = 0)
	caso_hielo = True
	while(True):
		temp_actual = random.uniform(min_temp, max_temp)				
		datos = {
			"dateTime": str(tiempo),
			"temperatura": str(round(temp_actual,2))
		}
		client.publish('casa/cocina/nevera',json.dumps(datos),qos = 0)		
		print(datos)
		if(caso_hielo):
			capacidad_hielo = random.uniform(min_hielo, max_hielo)
			datos2 = {
			"dateTime": str(tiempo),
			"capacidad": str(round(capacidad_hielo,0))
			}
			client.publish('casa/cocina/nevera',json.dumps(datos2),qos = 0)
			print(datos2)

		caso_hielo = not caso_hielo
		tiempo += datetime.timedelta(minutes=5)
		time.sleep(5)

if __name__ == '__main__':
	main()
	sys.exit(0)