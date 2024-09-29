import json


class Device:
    def __init__(self,routername = None, ip = None):
        self.routername = routername
        self.ip = ip
    
    #return device name

    def name(self):
        return("Name: %s IP address: %s \n" %(self.routername,self.ip))
    

    
    def getall():
        db = open('db.json','r')
        result = []
        json_result = json.loads(db.read())
        for i in json_result:
            device = Device(i,json_result[i])
            result.append(device)
        return result
    

    