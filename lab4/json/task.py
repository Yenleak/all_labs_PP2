import json

print("Interface status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open(r'C:\Users\User\Desktop\LAB_PP2\labs\lab4\json\sample-data.json') as file:
    data = json.load(file)
interfaces = data["imdata"]

for i in interfaces:
    attributes = i["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "")
    print(f"{dn}                                {description} {speed}  {mtu}")
     
     