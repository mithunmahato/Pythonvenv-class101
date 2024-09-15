from netmiko import ConnectHandler

devices = {
    'device_type': 'cisco_ios',
    'host':   '198.18.134.220',
    'username': 'cisco',
    'password': 'cisco',
    }

connection = ConnectHandler(**devices)

print(connection.send_command('show vlan brief'))

connection.disconnect()

