import json
import http

def interpretLoginResponse(r):

    if r.getcode() == http.HTTPStatus.OK:
        data = json.load(r)

        token = data["token"]

        print("Login Succeeded")
        return token
    else:
        print("Login Failed")
        return None

def interpretRegistrationResponse(r):

    if(r.getcode() == http.HTTPStatus.OK):
        data = json.load(r)

        success = data["success"]
        id = data["userId"]

        print("Registration Succeeded")
        return success, id
    else:
        print("Registration Failed")
        return None, None

def interpretGetMessageResponse(r):

    if(r.getcode() == http.HTTPStatus.OK):
        data = json.load(r)

        fromIds = []
        datas = []
        for message in data["message"]:
            fromIds.append(message["fromId"])
            datas.append(message["data"])

        print("Message(s) found")
        return fromIds, datas
    else:
        print("No message(s) found")
        return None, None