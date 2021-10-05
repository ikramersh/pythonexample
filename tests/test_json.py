from src.jsonExample import jsonStr, jsonObjects

def test_json():
    myJsonStr = jsonStr({"names" : ("Ivan", "Helen", "Lara", "Ariella")})
    jsonObjs = jsonObjects(myJsonStr)

    assert(jsonObjs['names'][0] == "Ivan")
    