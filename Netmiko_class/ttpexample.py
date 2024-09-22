from netmiko import ConnectHandler
from ttp import ttp
import pprint
import tabulate

device = {
    "device_type": "cisco_nxos",
    "host": "198.18.134.220",
    "username": "cisco",
    "password": "cisco"
}

#

connect = ConnectHandler(**device)

command = "show vlan brief"

vlan_data = connect.send_command(command)

connect.disconnect()

# Define the TTP template.

ttp_template = """
<group>
{{vlan_id}}  {{vlan_name}} 
</group>
"""

parser = ttp(data=vlan_data,template=ttp_template)
parser.parse()

r = parser.result(format='tabulate')[0]

print(r)