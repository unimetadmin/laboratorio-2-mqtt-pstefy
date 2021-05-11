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
	print('Conectado al publicador de tanque')

def main():
	client = paho.mqtt.client.Client("Tanque", False)
	client.qos = 0
	client.connect(host = 'localhost')
	redu_agua_max = 15
	redu_agua_min = 5
	aumen_agua_max = 25
	aumen_agua_min = 15
	tiempo = datetime.datetime.now().replace(minute = 0, second=0, microsecond = 0)
	nivel_agua = 100
	contador = 0
    
	while(True):
		reduccion_actual = int(round(random.uniform(redu_agua_min, redu_agua_max),0))
		if(reduccion_actual >= nivel_agua):
			nivel_agua = 0
		else:
			nivel_agua -= reduccion_actual

		if(contador == 3):
			contador = 0
			aumento_actual = int(round(random.uniform(aumen_agua_min, aumen_agua_max),0))
			if((aumento_actual + nivel_agua) > 100):
				nivel_agua = 100
			else:
				nivel_agua += aumento_actual
		datos = {
			"dateTime": str(tiempo),
			"nivel_agua": str(nivel_agua)
		}

		client.publish('casa/bano/tanque',json.dumps(datos),qos = 0)		
		print(datos)


		if(nivel_agua == 0):
			datos2 = {
			"dateTime": str(tiempo),
			"mensaje": "Ya no queda agua"
			}
			client.publish('casa/bano/tanque',json.dumps(datos2),qos = 0)
			print(datos2)
		elif(nivel_agua <= 50):
			datos3 = {
			"dateTime": str(tiempo),
			"mensaje": "El tanque va por: " + str(nivel_agua) + "%"
			}
			client.publish('casa/bano/tanque',json.dumps(datos3),qos = 0)
			print(datos3)

		tiempo += datetime.timedelta(minutes=10)
		contador += 1
		time.sleep(2) #10

if __name__ == '__main__':
	main()
	sys.exit(0)