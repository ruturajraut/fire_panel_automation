import mysql.connector
from datetime import datetime
import gvl

print ("database connected")


def insert_firecloud_test_record(data):
    # print(data)
    try:
      mydb = mysql.connector.connect(
        host="claypot-db-instance.ci3ywfy1btrn.ap-south-1.rds.amazonaws.com",
        user="claypot_db_user",
        password="claypot_db_user_password",
        database="claypot_db"
      )

      mycursor = mydb.cursor()
      dt = datetime.now().strftime('%Y-%m-%d')
      tm = datetime.now().strftime('%H:%M:%S')
      dttm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      sql = "INSERT INTO firecloud_testing (dt,tm,dttm,loc,python_take_values,trouble_count_before_test,test_complete,test_successful,num_alarm,num_super,num_troubles,out_of_range,dirty_sensor,almost_dirty,card_missing_failed,ac_failure,positive_earth_ground,negative_earth_ground,low_battery,depleted_missing_battery)"
      sql = sql +" VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      val = (dt,tm,dttm,data["loc"],data["python_take_values"],data["trouble_count_before_test"],data["test_complete"],data["test_successful"],data["num_alarm"],data["num_super"],data["num_troubles"],data["out_of_range"],data["dirty_sensor"],data["almost_dirty"],data["card_missing_failed"],data["ac_failure"],data["positive_earth_ground"],data["negative_earth_ground"],data["low_battery"],data["depleted_missing_battery"])
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      mycursor.close()
      mydb = None
      return True
    except mysql.connector.Error as err:
      print("mysql error")
      print(err)  
    except:
      print("Error while inserting data to the database")
      return False




def insert_dg_record(data):
    # print(data)
    try:
      mydb = mysql.connector.connect(
        host="claypot-db-instance.ci3ywfy1btrn.ap-south-1.rds.amazonaws.com",
        user="claypot_db_user",
        password="claypot_db_user_password",
        database="claypot_db"
      )

      mycursor = mydb.cursor()

      timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      sql = "INSERT INTO quantum_dg (dg_id,dg_name,run_status,coolant_temperature,battery_voltage,fuel_level,engine_speed,frequency,l1_l2_voltage,l2_l3_voltage,l3_l1_voltage,l1_current,l2_current,l3_current,auto_manual,run_hours,run_minutes,kwh,dt)"
      sql = sql +" VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      val = (data["id"],data["name"],data["run_status"],data["coolant_temperature"],data["battery_voltage"],data["fuel_level"],data["engine_speed"],data["frequency"],data["l1_l2_voltage"],data["l2_l3_voltage"],data["l3_l1_voltage"],data["l1_current"],data["l2_current"],data["l3_current"],data["auto_manual"],data["run_hours"],data["run_minutes"],data["kwh"],timestamp)
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      mycursor.close()
      mydb = None
      return True
    except:
      print("Error while inserting data to the database")
      return False



def insert_tank_record(data):
    print(data)
    try:
      mydb = mysql.connector.connect(
        host="claypot-db-instance.ci3ywfy1btrn.ap-south-1.rds.amazonaws.com",
        user="claypot_db_user",
        password="claypot_db_user_password",
        database="claypot_db"
      )

      mycursor = mydb.cursor()

      timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      sql = "INSERT INTO quantum_water_tanks(tank_id,tank_name,tank_level_percentage,tank_level_litres,dt)"
      sql = sql +" VALUES (%s,%s,%s,%s,%s)"
      val = (data["id"],data["name"],data["tank_level_percentage"],data["tank_level_litres"],timestamp)
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor.rowcount, "tank record inserted.")
      mycursor.close()
      mydb = None
    except:
      print("Error while inserting tank data to the database")  

def insert_alert(msg):
  try:
    mydb = mysql.connector.connect(
      host="claypot-db-instance.ci3ywfy1btrn.ap-south-1.rds.amazonaws.com",
      user="claypot_db_user",
      password="claypot_db_user_password",
      database="claypot_db"
    )

    mycursor = mydb.cursor()

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = "INSERT INTO quantum_alerts (dt,type,message,ack)"
    sql = sql +" VALUES (%s,%s,%s,%s)"
    val = (timestamp,3,msg,0)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "alert record inserted.")
    mycursor.close()
    mydb = None
  except:
    print("Error while inserting data to the alert table")


def update_vehicle_count():
  try:
    mydb = mysql.connector.connect(
        host="claypot-db-instance.ci3ywfy1btrn.ap-south-1.rds.amazonaws.com",
      user="claypot_db_user",
      password="claypot_db_user_password",
      database="claypot_db"
    )

    # print(mydb)
    mycursor = mydb.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d')

    query = "select * from quantum_vehicle_count where dt='" + timestamp + "'"
    print(query)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(myresult)

    if len(myresult) > 0:
      vehicle_entry_count = 0
      vehicle_entry_count = myresult[0][1]
      vehicle_entry_count = vehicle_entry_count + 1
      sql = "UPDATE quantum_vehicle_count SET entry_count="
      sql = sql + str(vehicle_entry_count)
      sql = sql + " where dt='"
      sql = sql + timestamp
      sql = sql + "'"
      print(sql)
    else:
      sql = "INSERT into quantum_vehicle_count (entry_count,exit_count,dt) values (1,0,'" + timestamp + "')"

    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mydb = None
  except:
    print("Error while inserting vehicle data to the database")  