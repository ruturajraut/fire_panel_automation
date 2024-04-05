import mysql.connector
from datetime import datetime
import gvl

print ("database connected")





def insert_param_record(device_id,device_name,param_id,param_name,value,setpoint_low,setpoint_high,isAlarm):
    try:
      mydb = mysql.connector.connect(
        host="claypot-db-instance.ci3ywfy1btrn.ap-south-1.rds.amazonaws.com",
        user="claypot_db_user",
        password="claypot_db_user_password",
        database="claypot_db"
      )

      # print(mydb)
      mycursor = mydb.cursor()

      timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      sql = "INSERT INTO server_monitoring (client_id,zone_id,device_id,device_name,param_id,param_name,value,dt,setpoint_low,setpoint_high,isAlarm)"
      sql = sql +" VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      val = (gvl.client_id,gvl.zone_id,device_id,device_name,param_id,param_name,value,timestamp,setpoint_low,setpoint_high,isAlarm)
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      mycursor.close()
      mydb = None
    except:
      print("Error while inserting data to the database")  

#insert_param_record()