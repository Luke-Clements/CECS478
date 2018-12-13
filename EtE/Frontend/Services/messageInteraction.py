import os
import http.client
import connection
from getMessage import getMessage
import interpretResponses
from allEncryption import RSAEncrypt
from allDecryption import RSADecrypt
import friendData
from keyPaths import keyPaths

class messageVariables:
    friendListFile = os.getcwd() + "FriendData.json"
    menu = "1: Get all messages from server\n" + "2: Send a new messsage to a friend" + "3: Delete all your messages on the server\n" + "4: Exit\n" + "Please choose from above: "

def messageInteraction(URL, token, userId):

    while True:
        option = getMessage(messageVariables.menu)

        if option == 1:
            fromIds, datas = getMessages(URL, token, userId)
            friends, messages = decryptMessages(messageVariables.friendListFile, fromIds, datas)
            displayMessages(friends, messages)
        elif option == 2:
            friend = getMessage("Which friend would you like to send a message to: ")
            friendId, publicKeyPath = friendData.loadFriendIdFromJSON(messageVariables.friendListFile, friend)
            message = getMessage("What message would you like to send: ")
            RSAEncrypt(message, publicKeyPath)
            postMessage(URL, token, message, friendId, userId)
        elif option == 3:
            deleteMessages(URL, token, userId)
        elif option == 4:
            return
        else: 
            print("Invalid menu input\n")

def displayMessages(friends, messages):

    i = 0
    while i < len(friends):
        print(friends[i] + "\t\t" + messages[i] + "\n\n")
        i += 1

def decryptMessages(filepath, fromIds, datas):

    friendNames = []
    messages = []
    for id in fromIds:
        friendNames.append(friendData.loadFriendNameFromJSON(filepath, id))

    for data in datas:
        messages.append(RSADecrypt(data, keyPaths.pathToPrivateKey))

    return friendNames, messages

def getMessages(URL, token, userId):

    conn, headers = connection.GetConnectionAndHeaders(URL)

    queryToken = "/Message/" + userId + "?token=" + token
    conn.request("GET", queryToken, headers=headers)

    return conn.getresponse()

def postMessage(URL, token, message, toUserId, fromId):

    conn, headers = connection.GetConnectionAndHeaders(URL)

    token = "token=" + token
    toUser = "&toId=" + toUserId
    fromUser = "&fromId=" + fromId
    message = "&data=" + message
    payload = token + toUser + fromUser + message

    conn.request("POST", "/Message", payload, headers)

    return conn.getresponse()

def deleteMessages(URL, token, userId):

    conn, headers = connection.GetConnectionAndHeaders(URL)

    payload = "token=" + token

    conn.request("DELETE", "/DeleteMessages/" + userId, payload, headers)

    return conn.getresponse()