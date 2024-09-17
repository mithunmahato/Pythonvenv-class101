from netmiko import ConnectHandler
import os
from dotenv import load_dotenv


devices = {
    'device_type': 'cisco_ios',
    'host':   '198.18.134.220',
    'username': os.getenv("USERNAME"),
    'password': os.getenv("PASSWORD"),
    }

with ConnectHandler(**devices) as connection:
    output = connection.send_config_from_file('vlan_commands.txt')
    connection.save_config()
    print(output)