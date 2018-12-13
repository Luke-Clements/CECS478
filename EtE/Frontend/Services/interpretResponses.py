import json

def interpretLoginResponse(r):

    data = json.load(r)

    token = data["token"]

    return token

def interpretRegistrationResponse(r):

    data = json.load(r)

    success = data["success"]
    id = data["userId"]

    return success, id

def interpretGetMessageResponse(r):

    data = json.load(r)

    fromIds = []
    datas = []
    for message in data["message"]:
        fromIds.append(message["fromId"])
        datas.append(message["data"])

    return fromIds, datas