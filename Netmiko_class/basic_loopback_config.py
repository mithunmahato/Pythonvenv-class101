#!/usr/devcl-venv/bin/python3

import csv
from netmiko import ConnectHandler
import os
from dotenv import load_dotenv

# Load environment variable from .envrc file
load_dotenv('.envrc')


# Function to  Parse device info from CSV file

def main():
    # read device information from CSV
    with open('devices.csv','r') as file:
        reader = csv.DictReader(file)
    # Retreive creds from envrionment varibale
        for device_info in reader:
            username = os.getenv('USERNAME')
            password = os.getenv('PASSWORD')
            configure_devices(device_info,username,password)
         


# Function to configure Cisco Devices

def configure_devices(device_info,username,password):
    # Establish ssh connection
    device = ConnectHandler(
        ip = device_info['ip_address'],
        username = username,
        password = password,
        device_type = device_info['device_type']

    )
    # Config commands
    ip_add_mask = f"10.10.10.{device_info['pod_id']} 255.255.255.0"
    commands = [
        'interface loopback0',
        f'ip address {ip_add_mask}',
        'description created by Netmiko',
        'exit'
    ]

    # sending configguration commands

    output = device.send_config_set(commands)
    device.save_config()
    print(output)
    print(f"Configuration of device {device_info['hostname']} completed")

    # Disconnect ssh session
    device.disconnect()


if __name__ == '__main__':
    main()




