from netmiko import ConnectHandler
import getpass

device = {
    "ip" : "198.18.134.10",
    "device_type": "cisco_ios",
    "username": input("Username:"),
    "password": getpass.getpass(),
    "secret": "cisco"
}

connect = ConnectHandler(**device)
p = connect.find_prompt()
print(p)
print("Device got connected")

output = connect.send_command("ping",expect_string=input('Protocol: '))
output = connect.send_command("ping",expect_string=input('Target IP address: '))
output = connect.send_command("ping",expect_string=input('Repeat count(n): '))
output = connect.send_command("ping",expect_string=input('Datagram size(100): '))
output = connect.send_command("ping",expect_string=input('Timeout in seconds: '))
output = connect.send_command("ping",expect_string=input('Extended commands:  ')) 
output = connect.send_command("ping",expect_string=input('Sweep range of sizes: '))

print(output)
