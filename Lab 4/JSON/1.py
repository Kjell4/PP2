import json

f = open('sample.py').read()
dictdata = json.loads(f)
print(
    "Interface Status" "\n"
    "=======================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n" 
    "-------------------------------------------------- --------------------  ------  ------")
imdata = dictdata["imdata"]
for i in imdata:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    des = i["l1PhysIf"]["attributes"]["descr"]
    speed = i["l1PhysIf"]["attributes"]["speed"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    print("{0:50} {1:20} {2:7} {3:6}".format(dn, des, speed, mtu))