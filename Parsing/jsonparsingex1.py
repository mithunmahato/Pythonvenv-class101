import json

data = {"name": "rtr1","ip": "192.168.1.1"}

jsonstring = json.dumps(data)

print(jsonstring)