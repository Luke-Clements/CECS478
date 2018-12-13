import requests
import connection
from getMessage import getMessage
import interpretResponses
import http.client
from friendInteraction import saveSelfInfo, getSelfInfo

class regLogVariables:
    menu =  "1: Register\n" + "2: Login\n" + "3: Exit\n" + "Please choose from above: "

def RegistrationLogin(URL):

    option = getMessage(regLogVariables.menu)

    success = True
    if option == "3":
        return "3", None

    username = getMessage("Username: ")
    password = getMessage("Password: ")

    if option == "1":
        success, id = Register(URL, username, password)
        if success is None:
            return None, None
        else:
            saveSelfInfo(username, id)
            option = "2"
    if option != "2" or success == None:
        return None, None

    token = Login(URL, username, password)

    if token == None:
        return None, None
    else:
        id = getSelfInfo()["friendId"]

    return id, token
    
#returns id, token
def Login(URL, username, password):

    conn, headers = connection.GetConnectionAndHeaders(URL)

    payload = AssemblePayload(username, password)

    conn.request("POST", "/authenticate", payload, headers)

    
    return interpretResponses.interpretLoginResponse(conn.getresponse())

#returns boolean of success
def Register(URL, username, password):

    conn, headers = connection.GetConnectionAndHeaders(URL)

    payload = AssemblePayload(username, password)

    conn.request("POST", "/signup", payload, headers)

    return interpretResponses.interpretRegistrationResponse(conn.getresponse())

def AssemblePayload(username, password):
    return "name=" + username + "&password=" + password