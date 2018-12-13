import json
import os
from keyPaths import loadRSAPublicKey

class friendVariables:
    infoPath = os.getcwd() + "/selfInfo.json"
    friendInfoPath = os.getcwd() + "/friendInfo.json"

def getSelfInfo():
    with open(friendVariables.infoPath, 'r') as json_file:
        user = json.load(json_file)

    public_key = loadRSAPublicKey()
    id = user["id"]

    selfInfo = {
        'friendId': id,
        'publicKey': public_key
    }

    json_file.close()
    return selfInfo
    
def saveSelfInfo(username, id):
    user = {
        'name': username,
        'id': id,
    }
    
    with open(friendVariables.infoPath, 'w') as json_file:
        json.dump(user, json_file)

    json_file.close()

def loadFriendsFromJSON(filepath):
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)

    json_file.close()
    return data

def loadFriendIdFromJSON(filepath, friendName):
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
    json_file.close()

    while True:
        if friendName == data["friend"]["friendName"]:
            return { "friendId": data["friend"]["friendId"], "publicKey": data["friend"]["publicKeyPath"] }

    return None

def loadFriendNameFromJSON(filepath, friendId):
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)

    while True:
        if friendId == data["friend"]["friendId"]:
            return { "friendId": data["friend"]["friendId"], "publicKey": data["friend"]["publicKeyPath"] }

    return None

def saveFriendToJSON (friendName, friendJSON):
    if not os.path.isfile(friendVariables.friendInfoPath):
        with open(friendVariables.friendInfoPath, 'w') as createFile:
            createFile.close()

    with open(friendVariables.friendInfoPath, 'r') as json_file:
        data = json.load(json_file)
    json_file.close()

    friend = {
        'friendName': friendName,
        'friendId': friendJSON["friendId"],
        'publicKey': friendJSON["publicKey"],
    }

    data.update(friend)

    with open(friendVariables.friendInfoPath, 'w+') as outFile:
        json.dump(data, outFile)
    outFile.close()