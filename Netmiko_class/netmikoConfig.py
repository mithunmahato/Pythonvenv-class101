from netmiko import ConnectHandler
import os
from dotenv import load_dotenv


devices = {
    'device_type': 'cisco_ios',
    'host':   '198.18.134.20',
    'username': os.getenv("USERNAME"),
    'password': os.getenv("PASSWORD"),
    }

commands = [
    "int loopback0",
    "ip add 10.10.10.20 255.255.255.0",
    "description Configured by Netmiko on 15092024",
]

with ConnectHandler(**devices) as connection:
    output = connection.send_config_set(commands)
    connection.save_config()
    print(output)