import sys
import paho.mqtt.client
import ssl
import psycopg2
from sqlalchemy import create_engine
import json
import numpy as np

host='queenie.db.elephantsql.com'
user ='cltubkki'
password='1U1Qq9qTvSD4QgR1ItbyFJkVZz5ejqms'
dbname='cltubkki'

def select(query,data):
    cur = myConnection.cursor()
    try:
        cur.execute(query,data)
    except Exception as e:
        myConnection.commit()
        print('Error en el query:', e)
    else:
        records = cur.fetchall()
        cur.close()
        return records

def select2(query,data):
    cur = myConnection.cursor()
    try:
        cur.execute(query,data)
    except Exception as e:
        myConnection.commit()
        print('Error en el query:', e)
    else:
        cur.close()
        print(myConnection.commit())

myConnection = psycopg2.connect(host = host,
                                user= user,
                                password =password,
                                dbname= dbname)

def on_connect(client, userdata, flags, rc):
    print('connected (%s)' % client._client_id)
    client.subscribe(topic='casa/cocina/#', qos=2)

def on_message(client, userdata, message):
    print('------------------------------')
    print('topic: %s' % message.topic)
    print('payload: %s' % message.payload)
    if("nevera" in message.topic):
        if("temperatura" in (json.loads(message.payload))):
            query = 'INSERT INTO public.nevera_temp("dateTime", temperatura) VALUES (%s, %s);'
            data = ((json.loads(message.payload))['dateTime'], float((json.loads(message.payload))['temperatura']))
            select2(query,data)
        elif("capacidad" in (json.loads(message.payload))):
            query = 'INSERT INTO public.nevera_capaci("dateTime", capacidad) VALUES (%s, %s);'
            data = ((json.loads(message.payload))['dateTime'], int(float((json.loads(message.payload))['capacidad'])))
            select2(query,data)
    if("olla" in message.topic):
        if("temperatura" in (json.loads(message.payload))):
            query = 'INSERT INTO public.olla("dateTime", temperatura) VALUES (%s, %s);'
            data = ((json.loads(message.payload))['dateTime'], float((json.loads(message.payload))['temperatura']))
            select2(query,data)
        elif("mensaje" in (json.loads(message.payload))):
            query = 'INSERT INTO public.mensaje("dateTime", mensaje) VALUES (%s, %s);'
            data = ((json.loads(message.payload))['dateTime'], ((json.loads(message.payload))['mensaje']))
            select2(query,data)

    print('qos: %d' % message.qos)

def main():
    client = paho.mqtt.client.Client(client_id='sus_cocina', clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host='127.0.0.1', port=1883)
    client.loop_forever()

if __name__ == '__main__':
    main()

sys.exit(0)
