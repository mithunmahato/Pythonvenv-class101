from netmiko import ConnectHandler
import os
from dotenv import load_dotenv

load_dotenv('.envrc')

devices = {
    'device_type': 'cisco_ios',
    'host':   '198.18.134.20',
    'username': os.getenv("USERNAME"),
    'password': os.getenv("PASSWORD"),
    }

with ConnectHandler(**devices) as connection:
    output = connection.send_command("show version")
    print(output)