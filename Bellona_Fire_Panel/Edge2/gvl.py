import json
import pyads

client_id = 15
location_id=7
zone_id=11
zone_name=''

controller_net_id="5.140.125.54.1.1"
controller_port = 851 # use 801 for tc2, use 851 for tc3
plc_val_prefix = '.' # use . for tc2, use .GVL for tc3

mqtt_broker_details = {
    'server_url' : 'mqtt://fortuitous-optician.cloudmqtt.com',
    'user' : 'geopcxoy',
    'pass' : 'osn07Rx4Eu-C',
    'port' : 1883,
    'ssl_port' : 8883,
    'websockets_port' : 443
}

email_details = {
    'url' : 'https://l94nyfvaf3.execute-api.ap-south-1.amazonaws.com/v1/device_update_status',
    'username' : 'quantum_email_alerts_username',
    'password' : 'pwd_email_alerts_user'
}


parameter_list = [
    {
        "device_type" : "fireAlarm",
        "mqtt_topic" : "bellonaFirePanel",
        "table" : "bellona_fire_panel",
        "frequency" : 36000,
        "counter" : 0,
        "items" : [
            {
                "id" : "bellonaFirePanel",
                "name" : "Bellona Fire Panel",
                "parameters" : [
                    # {
                    #     "PLCVariableName" : "UNACKNOWLEDGED_FIRE_ALARM_EXISTS",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                    #     "MQTTVariableName" : "unacknowledgedFireAlarmExists",
                    #     "lastStatus" : None,
                    #     # "columnName" : "run_status"
                    # },
                    # {
                    #     "PLCVariableName" : "UNACKNOWLEDGED_SUPERVISORY_EXIST",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                    #     "MQTTVariableName" : "unacknowledgedSupervisoryExists",
                    #     "lastStatus" : None,
                    #     # "columnName" : "run_status"
                    # },
                    # {
                    #     "PLCVariableName" : "UNACKNOWLEDGED_TROUBLE_EXISTS",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                    #     "MQTTVariableName" : "unacknowledgedTroubleExists",
                    #     "lastStatus" : None,
                    #     # "columnName" : "run_status"
                    # },
                    
                    {
                        "PLCVariableName" : "NUMBER_OF_SYSTEM_FIRE_ALARMS",
                        "PLCVariableDataType" : pyads.PLCTYPE_INT,
                        "MQTTVariableName" : "numberOfSystemFireAlarms",
                        "lastStatus" : None,
                        # "columnName" : "run_status"
                    },
                    {
                        "PLCVariableName" : "NUMBER_OF_SYSTEM_SUPERVISORIES",
                        "PLCVariableDataType" : pyads.PLCTYPE_INT,
                        "MQTTVariableName" : "numberOfSystemSupervisories",
                        "lastStatus" : None,
                        # "columnName" : "run_status"
                    },
                    {
                        "PLCVariableName" : "NUMBER_OF_SYSTEM_TROUBLES",
                        "PLCVariableDataType" : pyads.PLCTYPE_INT,
                        "MQTTVariableName" : "numberOfSYstemTroubles",
                        "lastStatus" : None,
                        # "columnName" : "run_status"
                    },
                    {
                        "PLCVariableName" : "EXCESSIVELY_DIRTY_OUT_OF_RANGE",
                        "PLCVariableDataType" : pyads.PLCTYPE_INT,
                        "MQTTVariableName" : "excessivelyDirtyOutOfRange",
                        "lastStatus" : None,
                        # "columnName" : "run_status"
                    },
                    {
                        "PLCVariableName" : "DIRTY_SENSOR_COUNTER",
                        "PLCVariableDataType" : pyads.PLCTYPE_INT,
                        "MQTTVariableName" : "dirtySensorCounter",
                        "lastStatus" : None,
                        # "columnName" : "run_status"
                    },
                    {
                        "PLCVariableName" : "ALMOST_DIRTY_COUNTER",
                        "PLCVariableDataType" : pyads.PLCTYPE_INT,
                        "MQTTVariableName" : "almostDirtyCounter",
                        "lastStatus" : None,
                        # "columnName" : "run_status"
                    },
                    {
                        "PLCVariableName" : "CARD_MISSING_FAILED",
                        "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                        "MQTTVariableName" : "cardMissingFailed",
                        "lastStatus" : None,
                        # "columnName" : "run_status"
                    },
                    {
                        "PLCVariableName" : "AC_FAILURE",
                        "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                        "MQTTVariableName" : "ACFailure",
                        "lastStatus" : None,
                        # "columnName" : "run_status"
                    },
                    {
                        "PLCVariableName" : "POSITIVE_EARTH_GROUND",
                        "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                        "MQTTVariableName" : "positiveEarthGround",
                        "lastStatus" : None,
                        # "columnName" : "run_status"
                    },
                    {
                        "PLCVariableName" : "NEGATIVE_EARTH_GROUND",
                        "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                        "MQTTVariableName" : "negativeEarthGround",
                        "lastStatus" : None,
                        # "columnName" : "run_status"
                    },
                    {
                        "PLCVariableName" : "LOW_BATTERY",
                        "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                        "MQTTVariableName" : "lowBattery",
                        "lastStatus" : None,
                        # "columnName" : "run_status"
                    },
                    {
                        "PLCVariableName" : "DEPLETED_MISSING_BATTERY",
                        "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                        "MQTTVariableName" : "depletedMissingBattery",
                        "lastStatus" : None,
                        # "columnName" : "run_status"
                    },
                    # {
                    #     "PLCVariableName" : "MCP_ACTIVATED",
                    #     "PLCVariableDataType" : pyads.PLCTYPE_BOOL,
                    #     "MQTTVariableName" : "mcpActivated",
                    #     "lastStatus" : None,
                    #     # "columnName" : "run_status"
                    # },
                ]
            }
        ]
    }
]


# parameter_list = [
#     {
#         "device_type_name" : "energy meters",
#         "mqtt_topic" : "octopus_np_em",
#         "devices" : [
#             {
#                 "device_name" : "Ground Floor LT Panel",
#                 "parameter_map" : [
#                     {"mqtt":"avg_amp","plc" : "energy_meter_gnd_floor_amp_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_power_factor","plc" : "energy_meter_gnd_floor_pf_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_total_voltage","plc" : "energy_meter_gnd_floor_vll_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_voltage","plc" : "energy_meter_gnd_floor_vln_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"total_watts","plc" : "energy_meter_gnd_floor_watt_total","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"kwh","plc" : "energy_meter_gnd_floor_kwh","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "1st Floor LT Panel",
#                 "parameter_map" : [
#                     {"mqtt":"avg_amp","plc" : "energy_meter_1_floor_amp_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_power_factor","plc" : "energy_meter_1_floor_pf_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_total_voltage","plc" : "energy_meter_1_floor_vll_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_voltage","plc" : "energy_meter_1_floor_vln_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"total_watts","plc" : "energy_meter_1_floor_watt_total","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"kwh","plc" : "energy_meter_1_floor_kwh","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             },

#             {
#                 "device_name" : "4th Floor LT Panel",
#                 "parameter_map" : [
#                     {"mqtt":"avg_amp","plc" : "energy_meter_4_floor_amp_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_power_factor","plc" : "energy_meter_4_floor_pf_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_total_voltage","plc" : "energy_meter_4_floor_vll_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_voltage","plc" : "energy_meter_4_floor_vln_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"total_watts","plc" : "energy_meter_4_floor_watt_total","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"kwh","plc" : "energy_meter_4_floor_kwh","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             },

#             {
#                 "device_name" : "5th Floor LT Panel",
#                 "parameter_map" : [
#                     {"mqtt":"avg_amp","plc" : "energy_meter_5_floor_amp_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_power_factor","plc" : "energy_meter_5_floor_pf_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_total_voltage","plc" : "energy_meter_5_floor_vll_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_voltage","plc" : "energy_meter_5_floor_vln_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"total_watts","plc" : "energy_meter_5_floor_watt_total","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"kwh","plc" : "energy_meter_5_floor_kwh","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             },

#             {
#                 "device_name" : "6th Floor LT Panel",
#                 "parameter_map" : [
#                     {"mqtt":"avg_amp","plc" : "energy_meter_6_floor_amp_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_power_factor","plc" : "energy_meter_6_floor_pf_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_total_voltage","plc" : "energy_meter_6_floor_vll_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"avg_voltage","plc" : "energy_meter_6_floor_vln_avg","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"total_watts","plc" : "energy_meter_6_floor_watt_total","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"kwh","plc" : "energy_meter_6_floor_kwh","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             },

            
#         ]
#     },
#     {
#         "device_type_name" : "air handling units",
#         "mqtt_topic" : "octopus_np_ahu",
#         "devices" : [
#             {
#                 "device_name" : "ground_floor_ahu",
#                 "parameter_map" : [
#                     {"mqtt":"return_air_temperature","plc" : "ahu_gnd_floor_return_air_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"run_status","plc" : "ahu_gnd_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"filter_status","plc" : "ahu_gnd_floor_filter_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"auto_manual_status","plc" : "ahu_gnd_floor_auto_manual_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"trip_status","plc" : "ahu_gnd_floor_trip_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"tfa_run_status","plc" : "tfa_gnd_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "1_floor_ahu",
#                 "parameter_map" : [
#                     {"mqtt":"return_air_temperature","plc" : "ahu_1_floor_return_air_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"run_status","plc" : "ahu_1_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"filter_status","plc" : "ahu_1_floor_filter_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"auto_manual_status","plc" : "ahu_1_floor_auto_manual_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"trip_status","plc" : "ahu_1_floor_trip_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"tfa_run_status","plc" : "tfa_1_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "4_floor_ahu",
#                 "parameter_map" : [
#                     {"mqtt":"return_air_temperature","plc" : "ahu_4_floor_return_air_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"run_status","plc" : "ahu_4_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"filter_status","plc" : "ahu_4_floor_filter_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"auto_manual_status","plc" : "ahu_4_floor_auto_manual_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"trip_status","plc" : "ahu_4_floor_trip_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"tfa_run_status","plc" : "tfa_4_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "5_floor_ahu",
#                 "parameter_map" : [
#                     {"mqtt":"return_air_temperature","plc" : "ahu_5_floor_return_air_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"run_status","plc" : "ahu_5_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"filter_status","plc" : "ahu_5_floor_filter_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"auto_manual_status","plc" : "ahu_5_floor_auto_manual_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"trip_status","plc" : "ahu_5_floor_trip_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"tfa_run_status","plc" : "tfa_5_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "6_floor_ahu",
#                 "parameter_map" : [
#                     {"mqtt":"return_air_temperature","plc" : "ahu_6_floor_return_air_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"run_status","plc" : "ahu_6_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"filter_status","plc" : "ahu_6_floor_filter_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"auto_manual_status","plc" : "ahu_6_floor_auto_manual_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"trip_status","plc" : "ahu_6_floor_trip_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"tfa_run_status","plc" : "tfa_6_floor_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             }
#         ]
#     },
#     {
#         "device_type_name" : "temperature and humidity",
#         "mqtt_topic" : "octopus_np_temp_rh",
#         "devices" : [
#             {
#                 "device_name" : "terrace_floor_sensor",
#                 "parameter_map" : [
#                     {"mqtt":"temperature","plc" : "terrace_floor_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"humidity","plc" : "terrace_floor_humidity","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "server_room_sensor",
#                 "parameter_map" : [
#                     {"mqtt":"temperature","plc" : "server_room_temperature","plc_data_type" : pyads.PLCTYPE_REAL,"value":None},
#                     {"mqtt":"humidity","plc" : "server_room_humidity","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             }
#         ]
#     },
#     {
#         "device_type_name" : "hydrogen sensor",
#         "mqtt_topic" : "octopus_np_temp_hydro",
#         "devices" : [
#             {
#                 "device_name" : "ups_room_sensor",
#                 "parameter_map" : [
#                     {"mqtt":"level","plc" : "ups_room_h2","plc_data_type" : pyads.PLCTYPE_REAL,"value":None}
#                 ]
#             }
#         ]
#     },
#     {
#         "device_type_name" : "pumps",
#         "mqtt_topic" : "octopus_np_pumps",
#         "devices" : [
#             {
#                 "device_name" : "domestic_pump_1",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "domestic_pump_1_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "domestic_pump_2",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "domestic_pump_2_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "flush_pump_1",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "flush_pump_1_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "flush_pump_2",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "flush_pump_2_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "fire_pump_1",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "fire_pump_1_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "fire_pump_2",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "fire_pump_2_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "jockey_pump_1",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "jockey_pump_1_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "jockey_pump_2",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "jockey_pump_2_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "booster_pump_1",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "booster_pump_1_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "booster_pump_2",
#                 "parameter_map" : [
#                     {"mqtt":"status","plc" : "booster_pump_2_run_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             }
#         ]
#     },
#     {
#         "device_type_name" : "tanks",
#         "mqtt_topic" : "octopus_np_tanks",
#         "devices" : [
#             {
#                 "device_name" : "domestic_tank",
#                 "parameter_map" : [
#                     {"mqtt":"high_status","plc" : "domestic_tank_high_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"low_status","plc" : "domestic_tank_low_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "flush_tank",
#                 "parameter_map" : [
#                     {"mqtt":"high_status","plc" : "flush_tank_high_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"low_status","plc" : "flush_tank_low_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "fire_tank_1",
#                 "parameter_map" : [
#                     {"mqtt":"high_status","plc" : "fire_tank_1_high_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"low_status","plc" : "fire_tank_1_low_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#             {
#                 "device_name" : "fire_tank_2",
#                 "parameter_map" : [
#                     {"mqtt":"high_status","plc" : "fire_tank_2_high_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None},
#                     {"mqtt":"low_status","plc" : "fire_tank_2_low_status","plc_data_type" : pyads.PLCTYPE_BOOL,"value":None}
#                 ]
#             },
#         ]
#     }
# ]

pyads_datatype_map = {
    'REAL' : pyads.PLCTYPE_REAL,
    'BOOL' : pyads.PLCTYPE_BOOL
}

previous_temperature_reading = 0
temperature_difference_trigger = 0.005
fan_trigger_temperature = 30
fan_mode = 0 #0- auto,1-manual
fan_status=0