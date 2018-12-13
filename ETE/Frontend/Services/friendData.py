import json
import os

def loadFriendsFromJSON(filepath):
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)

    json_file.close()
    return data

def loadFriendIdFromJSON(filepath, friendName):
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)

    while True:
        if friendName == data["friend"]["friendName"]:
            return data["friend"]["friendId"], data["friend"]["publicKeyPath"]

def loadFriendNameFromJSON(filepath, friendId):
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)

    while True:
        if friendId == data["friend"]["friendId"]:
            return data["friend"]["friendName"], data["friend"]["publicKeyPath"]

def saveFriendToJSON (filepath, friendName, friendId, publicKey):
    if not os.path.isfile(filepath):
        with open(filepath, 'w') as createFile:
            createFile.close()

    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
    json_file.close()

    friend = {
        'friendName': friendName,
        'friendId': friendId,
        'publicKey': publicKey,
    }

    data.update(friend)

    with open(filepath, 'w+') as outFile:
        json.dump(data, outFile)
    outFile.close()