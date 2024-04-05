import gvl
import pyads
import time
from threading import Thread

plc_in = ''
plc_out = ''

def check_controller_availability():
    global plc_in
    global plc_out
    isControllerAvailable = False
    while isControllerAvailable == False:
        print(f"Trying to connect to controller on {gvl.controller_net_id}, port:{gvl.controller_port}")
        try:
            plc_in = pyads.Connection(gvl.controller_net_id, gvl.controller_port)
            plc_out = pyads.Connection(gvl.controller_net_id, gvl.controller_port)
            plc_in.open()
            plc_out.open()
            isControllerAvailable = plc_in.read_by_name('GVL.controller_available', pyads.PLCTYPE_BOOL)
            print(isControllerAvailable)
        except:
            print("...unable to connect to controller")
            time.sleep(10)
    



def startDG():
    try:
        plc_out.write_by_name('GVL.dgStartCommandInputFromUser', True, pyads.PLCTYPE_BOOL)
        print("starting DG")
        
    except:
        print("Error while starting DG...")

def stopDG():
    try:
        plc_out.write_by_name('GVL.dgStopCommandInputFromUser', True, pyads.PLCTYPE_BOOL)
        print("stopping DG...")
    except:
        print("Error while stopping DG...")
