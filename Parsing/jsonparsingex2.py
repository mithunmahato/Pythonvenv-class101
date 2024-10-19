import json

with open("jsonfile.json") as f:
    jsondata = f.read()


mydict = json.loads(jsondata)

print(type(mydict))

mydict["interface"]["name"] = "Ethernet1"

with open ("jsonfile.json","w") as fw:
    json.dump(mydict,fw,indent=5)