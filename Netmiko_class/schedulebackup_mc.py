#!/usr/bin/Python3

from netmiko import ConnectHandler
import os
from datetime import datetime
import hvac
import schedule
import time
import threading

# Defube the device details:
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '198.18.134.10',
    'username': 'cisco',
    'password': 'cisco',
    'global_delay_factor' : 4
}

# File to store the last config:

start_time = time.time()

last_config_file = 'last_config.txt'



def load_last_config():
    """Last config load"""

    if os.path.exists(last_config_file):
        with open(last_config_file,'r') as f:
            return f.read()
    return ""

def save_last_config(config):
    """Save the current config to the last config """
    with open(last_config_file,'w') as f:
        f.write(config)


def backup_config():

    try:

      # Print the current time
      current_time = datetime.now().strftime('%Y%m%d_%H%M%s')
      print(f"Starting backup at {current_time}")

      # Connection the device

      connection = ConnectHandler(**cisco_device)
  
      # Disbale pager lenth

      connection.send_command("terminal length 0")

      # Getting Running config

      running_config = connection.send_command("show running-config")

      # Load last config

      last_config = load_last_config()

      # Compare current and last conifgguration

      if running_config != last_config:
        # Create a filename with current timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%s')
        backup_filename = f"backup_{cisco_device['host']}_{timestamp}.txt"

        # Write the new config to the backup file

        with open(backup_filename,'w') as backup_file:
            backup_file.write(running_config)

        # Save the current config as the last config
        save_last_config(running_config)

      else:
        print("No changes detected. Backup Skipped")

    except Exception as e:
       print(f"Error: {e}")

    finally:
       connection.disconnect()

def schedule_backup():
   # Run the backup based on the schedule:
   global last_checked_config
   last_checked_backup = backup_config()


schedule.every().day.at("06:59").do(schedule_backup)
       

last_checked_config = load_last_config()


def monitor_config_changes():
   global last_checked_config
   while True:
    
    try:
      
      connection = ConnectHandler(**cisco_device)
      connection.send_command("terminal length 0")
      running_config = connection.send_command("show running-config")

      if running_config != last_checked_config:
         print("Configuration changes detected")
         last_checked_config = backup_config()
      
      connection.disconnect()
    except Exception as e:
      print(f"Error during monitoring: {e}")

      time.sleep(60)

# Start monitoring in seprate thread:

monitor_thread = threading.Thread(target=monitor_config_changes,daemon=True)
monitor_thread.start()

print("Backup schedular is running.....")


while True:
    schedule.run_pending()
    time.sleep(60) # check every time
    
    
    total_compile_Time = (time.time() - start_time)*1000 

    print(f"Total execution time: {total_compile_Time:.3f} ms")


