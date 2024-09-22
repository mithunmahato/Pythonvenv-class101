#!/usr/bin/Python3

from netmiko import ConnectHandler
import csv
import os
from datetime import datetime
from dotenv import load_dotenv
import hvac
import schedule
import time
from netmikobackup import get_creds_from_vault


# 

devices = {
    'device_type': 'cisco_ios',
    'host':   '198.18.134.20',
    'username': 'cisco',
    'password': 'cisco'
    }


def sc_backup_config():
    try:
        # Print time

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        connect = ConnectHandler(**devices)

        connect.send_command("terminal length 0")

        running_config = connect.send_command("show running-config")

        timestamp_filename = f"{datetime.now().strftime('%Y-%m-%d')}_{devices['host']}.txt"

        with open(timestamp_filename,'w') as backup_file:
            backup_file.write(running_config)

        print(f"Backup of {devices['host']} is completed and Saved as {timestamp_filename} ")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        connect.disconnect()


schedule.every().day.at("08:13").do(sc_backup_config)

print("Backup scheduler is running.....")

while True:
    schedule.run_pending()
    time.sleep(60) # check every time




