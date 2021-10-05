from src.jsonExample import jsonStr, jsonObjects

def test_json():
    myJsonStr = jsonStr({"names" : ("Ivan", "Helen", "Lara", "Ariella")})
    jsonObjs = jsonObjects(myJsonStr)

    assert(jsonObjs['names'][0] == "Ivan")
    assert("Ariell" in jsonObjs['names'])
    assert("John" not in jsonObjs['names'])
    