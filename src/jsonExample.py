import json


def jsonStr(data):
    return json.dumps(data)


def jsonObjects(jsonStr):
    return json.loads(jsonStr)
    
    

myJsonStr = jsonStr({"names" : ("Ivan", "Helen", "Lara", "Ariella")})
jsonObjs = jsonObjects(myJsonStr)
print(jsonObjs)
print(jsonObjs['names']) 