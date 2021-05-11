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
	print('Conectado al publicador de contador de personas')

def main():
	client = paho.mqtt.client.Client("Contador", False)
	client.qos = 0
	client.connect(host = 'localhost')
	max_personas = 10
	min_personas = 0
	tiempo = datetime.datetime.now().replace(minute = 0, second=0, microsecond = 0)
	while(True):
		personas_actuales = random.uniform(min_personas, max_personas)				
		datos = {
			"dateTime": str(tiempo),
			"personas": str(int(round(personas_actuales,0)))
		}
		client.publish('casa/sala/contador_personas',json.dumps(datos),qos = 0)		
		print(datos)
        
		tiempo += datetime.timedelta(minutes = 1)
		if(int(personas_actuales) > 5):
			datos2 = {
			"dateTime": str(tiempo),
			"mensaje": "ALERTA: Retirense de la sala, no pueden haber mas de 5 personas al mismo tiempo"
			}
			client.publish('casa/sala/contador_personas',json.dumps(datos2),qos = 0)
			print(datos2)
		time.sleep(1)

if __name__ == '__main__':
	main()
	sys.exit(0)