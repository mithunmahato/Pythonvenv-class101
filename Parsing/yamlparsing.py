import yaml

with open ("yamlfile.yml") as f:
    yamldata = f.read()

yamldict = yaml.load(yamldata,Loader=yaml.FullLoader)

print(yamldict)

yamldict["interface"]["ipv4"]["address"][0]["ip"] = "192.168.20.1"

print(yamldict)

dyaml=yaml.dump(yamldict)
print(dyaml)



