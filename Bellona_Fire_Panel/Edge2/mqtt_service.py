import paho.mqtt.client as mqtt
import os, urllib.parse as urlparse
import time
import json
import gvl
import plc
import database as db
import web_service as ws


def handle_message(topic,payload):
    print("handle message")

    if(topic == "theWalkDG1_command"):
        if(payload=='start-dg'):
            plc.startDG()
        elif(payload=='stop-dg'):
            plc.stopDG()

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))
    # mqttc.subscribe("octopus-fan-command", 0)
    mqttc.subscribe("theWalkDG1_command")

def on_disconnect(client, userdata, rc):
    print("disconnected...")
    connect()

def on_message(client, obj, msg):
    # print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    handle_message(msg.topic,msg.payload.decode('utf-8'))


def on_publish(client, obj, mid):
    pass
    # print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)



mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
#mqttc.on_log = on_log

# print(mqttc.on_connect)

def connect():
    
    url_str = gvl.mqtt_broker_details["server_url"]
    print(url_str)
    url = urlparse.urlparse(url_str)
    # Connect
    mqttc.username_pw_set(gvl.mqtt_broker_details["user"], gvl.mqtt_broker_details["pass"])

    isMqttConnected = False

    while isMqttConnected == False:
        try:
            mqttc.connect(url.hostname, gvl.mqtt_broker_details["port"])
            mqttc.loop_start()
            isMqttConnected = True
        except:
            print("...unable to connect to MQTT")
            time.sleep(10)

# topic = url.path[1:] or 'octopus'

def subscribe(topic):
    # Start subscribe, with QoS level 0
    mqttc.subscribe(topic, 0)
    

def publish(topic,message):
    # Publish a message
    mqttc.publish(topic, message)





# Continue the network loop, exit when an error occurs
# rc = 0
# while rc == 0:
#     rc = mqttc.loop()
# print("rc: " + str(rc))