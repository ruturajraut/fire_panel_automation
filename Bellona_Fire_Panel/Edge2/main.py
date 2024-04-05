from xmlrpc.client import TRANSPORT_ERROR
import pyads
import threading
# import local_db as db
# import web_service as ws
import mqtt_service as mqtt
import json
import gvl
import plc
import random
import web_service as ws
import requests
import database as db
from datetime import datetime
import time

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'telegram'))
# print(sys.path)
try:
    print("will try to import telegram")
    import telegram_send_message
    # from ..telegram import telegram
except Exception as e:
    print("Telegram Exception:")
    print(e)
    print("telegram exception ended")

# import local_to_aws_data_sync as syncer

web_send_counter=300
web_send_threshold = 300
dbWritten = False

dbLastWriteYear = None
dbLastWriteMonth = None
dbLastWriteDay = None
dbLastWriteHour = None
dbLastWriteMinute = None


def data_retrieval_repeater():
    global dbWritten
    global dbLastWriteYear
    global dbLastWriteMonth
    global dbLastWriteDay
    global dbLastWriteHour
    global dbLastWriteMinute

    global web_send_counter
    global web_send_threshold

    lastPythonTakeValues = False

    while True:
        dt = datetime.now()

        # -------checking test has been conducted and broadcasting results-------
        try:
            pythonTakeValues = plc.plc_in.read_by_name("GVL.pythonTakeValues",pyads.PLCTYPE_BOOL)
            testComplete = plc.plc_in.read_by_name("GVL.testComplete",pyads.PLCTYPE_BOOL)
            testSuccessful = plc.plc_in.read_by_name("GVL.testSuccessful",pyads.PLCTYPE_BOOL)
        except pyads.ADSError:
            print(f"unable to find PLC variables related to testing")
        
        # pythonTakeValues = True
        print(pythonTakeValues)
        telegramMessage = ""
        if(pythonTakeValues == True and lastPythonTakeValues == False):
            telegramMessage = "Location : Bellona, Thane \n\n"
            telegramMessage = telegramMessage + "An automated test was attempted by the FireCloud System \n\n"
            if(testComplete):
                telegramMessage = telegramMessage + "Loop test <b>complete</b>. \n\n"
            else:
                telegramMessage = telegramMessage + "Loop test <b>FAILED</b> \n\n"
                
            if(testSuccessful):
                telegramMessage = telegramMessage + "Modbus Test <b>successful</b>. \n\n"
            else:
                telegramMessage = telegramMessage + "Modbus Test <b>failed</b>. \n\n"
            
            db_data = {
                "loc" : "bellona",
                "python_take_values" : pythonTakeValues,
                "trouble_count_before_test" : plc.plc_in.read_by_name("GVL.troubleCountBeforeTest",pyads.PLCTYPE_INT),
                "test_complete" : testComplete,
                "test_successful" : testSuccessful,
                "num_alarm" : plc.plc_in.read_by_name("GVL.NUMBER_OF_SYSTEM_FIRE_ALARMS",pyads.PLCTYPE_INT),
                "num_super" : plc.plc_in.read_by_name("GVL.NUMBER_OF_SYSTEM_SUPERVISORIES",pyads.PLCTYPE_INT),
                "num_troubles" : plc.plc_in.read_by_name("GVL.NUMBER_OF_SYSTEM_TROUBLES",pyads.PLCTYPE_INT),
                "out_of_range" : plc.plc_in.read_by_name("GVL.EXCESSIVELY_DIRTY_OUT_OF_RANGE",pyads.PLCTYPE_INT),
                "dirty_sensor" : plc.plc_in.read_by_name("GVL.DIRTY_SENSOR_COUNTER",pyads.PLCTYPE_INT),
                "almost_dirty" : plc.plc_in.read_by_name("GVL.ALMOST_DIRTY_COUNTER",pyads.PLCTYPE_INT),
                "card_missing_failed" : plc.plc_in.read_by_name("GVL.CARD_MISSING_FAILED",pyads.PLCTYPE_BOOL),
                "ac_failure" : plc.plc_in.read_by_name("GVL.AC_FAILURE",pyads.PLCTYPE_BOOL),
                "positive_earth_ground" : plc.plc_in.read_by_name("GVL.POSITIVE_EARTH_GROUND",pyads.PLCTYPE_BOOL),
                "negative_earth_ground" : plc.plc_in.read_by_name("GVL.NEGATIVE_EARTH_GROUND",pyads.PLCTYPE_BOOL),
                "low_battery" : plc.plc_in.read_by_name("GVL.LOW_BATTERY",pyads.PLCTYPE_BOOL),
                "depleted_missing_battery" : plc.plc_in.read_by_name("GVL.DEPLETED_MISSING_BATTERY",pyads.PLCTYPE_BOOL),
            }
            
            
            print(db_data)
            
            db.insert_firecloud_test_record(db_data)   

            for item in db_data:
                if(item != "python_take_values"):
                    telegramMessage = telegramMessage + item + " : " + str(db_data[item]) + "\n"
            
            print(telegramMessage)
            telegram_send_message.send_to_telegram(telegramMessage,"firecloud-test.jpg","-1001957799917")
            
        
        lastPythonTakeValues = pythonTakeValues
        # -----end of test related code

        # print(web_send_counter)

        for device_type in gvl.parameter_list:
            data_sendable = {
                "device_type" : device_type["device_type"],
                "data" : {}
                }

            complete_database_data = []

            if('items' in device_type):
                parameter_data = {}
                for item in device_type['items']:
                    item_table_data = {"id" : item["id"],"name" : item["name"]}
                    hasDGRunStatusChanged = False
                    parameter_data["id"] = item["id"]
                    parameter_data["name"] = item["name"]
                    for param in item["parameters"]:
                        # print("GVL." + param["PLCVariableName"])
                        try:
                            x = plc.plc_in.read_by_name("GVL." + param["PLCVariableName"], param["PLCVariableDataType"])
                            parameter_data[param["MQTTVariableName"]] = x
                                    
                        except pyads.ADSError:
                            print(f"unable to find PLC variable GVL.{param['PLCVariableName']}")
                        
                        
                    data_sendable["data"] = parameter_data
                    complete_database_data.append(item_table_data)

                    if hasDGRunStatusChanged:
                        db.insert_dg_record(item_table_data)
                        hasDGRunStatusChanged = False
            
            mqtt.publish(device_type['mqtt_topic'],json.dumps(data_sendable))
            # print(data_sendable)
            # print("THE WALK DG CONTROLLER")

            

        

        time.sleep(2)
        # threading.Timer(2, data_retrieval_repeater).start()

def printLastWrite():
    global dbLastWriteYear
    global dbLastWriteMonth
    global dbLastWriteDay
    global dbLastWriteHour
    global dbLastWriteMinute

    print(dbLastWriteYear)
    print(dbLastWriteMonth)
    print(dbLastWriteDay)
    print(dbLastWriteHour)
    print(dbLastWriteMinute)

# if ws.get_zone_data():
plc.check_controller_availability()
mqtt.connect()

data_retrieval_repeater()
input("")


