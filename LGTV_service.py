# -*- coding: utf-8 -*-

import configparser

import paho.mqtt.client as mqtt

from libLGTV_serial import LGTV

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

tvmodel = config['general']['tvmodel']
serialport = config['general']['serialport']

username = config['mqtt']['username']
password = config['mqtt']['password']

mqtt_server = config['mqtt']['server']
mqtt_port = int(config['mqtt']['port'])

topic = '{}/command'.format(config['mqtt']['topic'])

# Setup tv/serial connection
tv = LGTV(tvmodel, serialport)

# Setup functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code {}".format(str(rc)))

def on_message(client, userdata, msg):
    command = msg.payload.decode('utf-8')
    
    print("{} {}".format(msg.topic, command))

    tv.send(command)

# Setup and connect mqtt
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username, password)

client.connect(mqtt_server, mqtt_port, 60)

client.subscribe(topic)

client.loop_forever()
