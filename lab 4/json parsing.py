import json
with open('sample-data.json') as file:
    jsond=json.load(file)
    
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")  
print("-------------------------------------------------- --------------------  ------  ------")
greed=jsond["imdata"]
for x in greed:
    neo=x["l1PhysIf"]
    attr=neo["attributes"]
    dni=attr["dn"]
    speed=attr["speed"]
    mtu=attr["mtu"]
    outp=" "
    if(len(dni)==42):
        outp+=dni + " "*30  +speed+"   "+ mtu
    else:
        outp += dni + " "*31 + speed + "   " + mtu
    print(outp)

    