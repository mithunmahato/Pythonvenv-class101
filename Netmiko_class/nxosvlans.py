from netmiko import ConnectHandler
import getpass


def configure_vlan(device,vlans):
    with ConnectHandler(**device) as connect:
        for vlan_id,vlan_name in vlans.items():
            commands = [
                f"vlan {vlan_id}",
                f"name {vlan_name}",
                'exit'
            ]
            output = connect.send_config_set(commands)
            print(f"Configured VLAN {vlan_id}: {vlan_name}")
            print(output)

if __name__ == "__main__":
    # main
    device = {
        'device_type': 'cisco_nxos',
        'host': '198.18.134.220',
        'username': 'cisco',
        'password': getpass.getpass()
    }

    vlans = {
        "10": "Maketing",
        "20": "Sales",
        "30": "Engineering",
        "40": "HR"
    }

    configure_vlan(device,vlans)
