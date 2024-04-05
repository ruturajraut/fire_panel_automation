import requests
import time
import gvl

TEMPERATURE_RECIEPT_URL = "https://l94nyfvaf3.execute-api.ap-south-1.amazonaws.com/v1/receive-temperature-data"
ZONE_DATA_URL = "https://l94nyfvaf3.execute-api.ap-south-1.amazonaws.com/v1/bms-zone-data"
PARAM_DATA_SEND_URL = "https://l94nyfvaf3.execute-api.ap-south-1.amazonaws.com/v1/bms-param-data"




def get_zone_data():
    print(f'client ID :  {gvl.client_id}')
    print(f'Location ID :  {gvl.location_id}')
    print(f'Zone ID : {gvl.zone_id}')
    print('')
    print("Connecting to AWS for zone data...")
    print('')
    data_json = {"client_id" : gvl.client_id,"location_id" : gvl.location_id,"zone_id" : gvl.zone_id}
    # sending post request 
    r = requests.post(url = ZONE_DATA_URL, json = data_json,verify=False)
    data = r.json()

    print("...reply recieved from AWS server")
    print('')
    if(not 'dataAvailable' in data or not data['dataAvailable']):
        print('No data is available from the AWS server')
        return False

    #setting zone name and controller details
    gvl.zone_name = data['data']['zone_name']
    gvl.controller_net_id = data['data']['controller_address']
    # gvl.controller_net_id = '5.103.234.86.1.1'
    gvl.controller_port = data['data']['controller_port']
    print('')
    print(f'Zone Name : {gvl.zone_name}')
    print(f'Controller AMS NET ID : {gvl.controller_net_id}')
    print(f'Controller Port : {gvl.controller_port}')
    print('')

    if(not 'mqttData' in data['data']):
        print('MQTT Data not available from AWS. Cannot continue without MQTT')
        return False
    else:
        print('Setting MQTT Data...')
        gvl.mqtt_broker_details = data['data']['mqttData']

    
    if(not 'parameter_list' in data['data']):
        print('Devices and Parameters data (parameter_map) is not available from AWS. Cannot continue without device data')
        return False
    else:
        print('Setting Device and Parameter data...')
        gvl.parameter_list = data['data']['parameter_list']

        # print(gvl.parameter_list)
    
    return True

    # print(data)

def send_param_data(param_id,param_value):
    print(f'sending data to aws...({param_id},{param_value})')
    data_json = {"param_id" : param_id, "param_value" : param_value}
    r = requests.post(url = PARAM_DATA_SEND_URL, json = data_json,headers={'Connection':'close'})

def send_device_type_data(json):
    print(f'sending data for all devices of a paticular device type to aws...')
    print(json)

def sendMail(subject,body,recipients):
    data = '{"quantumEmailAlert" : true,"username":"' + gvl.email_details["username"] + '","password" : "' + gvl.email_details["password"] + '","emailSubject" : "' + subject + '","emailBody" : "' + body + '","recipients" : "' + recipients + '"}'
    try:
        x=requests.post(gvl.email_details["url"],data=data)
    except:
        print("Error while sending email")
    