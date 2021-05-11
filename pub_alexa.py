import pyowm
import requests, json 
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
    print('Conectado al publicador de alexa')

def main():
    client = paho.mqtt.client.Client("Alexa", False)
    client.qos = 0
    client.connect(host = 'localhost')
    tiempo = datetime.datetime.now().replace(minute = 0, second=0, microsecond = 0)
    api_key = "04175454c695300ac9b743ce20de3d17"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Caracas,VE"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        caso = 0
        while(True):
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature -= 273.15
            if(caso == 0):
                current_temperature += 1
                caso = 1
            elif(caso == 1):
                current_temperature -= 1
                caso = 2
            elif(caso == 2):
                caso = 0
            datos = {
                "dateTime": str(tiempo),
                "temperatura": str(round(current_temperature,1))
            }
            client.publish('casa/sala/alexa',json.dumps(datos),qos = 0)
            print(datos)
            tiempo += datetime.timedelta(minutes = 1)
            time.sleep(2)
    else:
        datos2 = {
            "dateTime": str(tiempo),
            "mensaje": "La ciudad no fue encontrada"
        }
        client.publish('casa/sala/alexa',json.dumps(datos2),qos = 0)
        print(datos2)

if __name__ == '__main__':
    main()
    sys.exit(0)


