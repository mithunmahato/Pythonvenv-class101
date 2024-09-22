#!/usr/bin/Python3

from netmiko import ConnectHandler
import csv
import os
from datetime import datetime
from dotenv import load_dotenv
import hvac


load_dotenv('.envrc')

def main():
    # read device information from CSV
    with open('devices.csv','r') as file:
        reader = csv.DictReader(file)
    # Retreive creds from envrionment varibale
        for device_info in reader:
            username,password = get_creds_from_vault()
            take_backup(device_info,username,password)



def get_creds_from_vault():
    client = hvac.Client()
    vault_url = os.getenv("VAULT_URL")
    vault_token = os.getenv("VAULT_TOKEN")
    client = hvac.Client(url=vault_url,token=vault_token)
    vault_reponse=client.secrets.kv.v2.read_secret_version(path='useraccesspath',mount_point="mysecreds",raise_on_deleted_version=True)
    return vault_reponse['data']['data']['username'],vault_reponse['data']['data']['password']
    


def take_backup(device_info,username,password):
    # Establish ssh connection
    device = ConnectHandler(
        ip = device_info['ip_address'],
        username = username,
        password = password,
        device_type = device_info['device_type']
    )


    try:
        # Taking backup
        command = [
            "terminal pager 0",
            "show running-config"
        ]

        backup_output = device.send_command("show running-config")

        # Save backup with date_hostname.txt format

        backupfilename= f"{datetime.now().strftime('%Y-%m-%d')}_{device_info['hostname']}.txt"

        with open(backupfilename,'w') as backup_file:
            backup_file.write(backup_output)

        print(f"Backup of {device_info['hostname']} is completed and Saved as {backupfilename} ")


    finally:
        #Device disconnect ssh session
        device.disconnect()

if __name__ == "__main__":
    main()

