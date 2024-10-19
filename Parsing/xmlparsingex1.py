import xmltodict
import pretty

with open ("xmlfile.xml") as f:
    xmldata = f.read()

xmldict = xmltodict.parse(xmldata)

print(xmldict)

xmldict["device"]["hostname"] = "RTR4"

with open ("xmlfile.xml","w") as fw:
   fw.write(xmltodict.unparse(xmldict,pretty=True))