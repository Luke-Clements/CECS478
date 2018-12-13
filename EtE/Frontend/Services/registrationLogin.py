import requests
import connection
from getMessage import getMessage
import interpretResponses

class regLogVariables:
    menu =  "1: Register\n" + "2: Login\n" + "3: Exit\n" + "Please choose from above: "

def RegistrationLogin(URL):

    option = getMessage(regLogVariables.menu)

    if option == 3:
        return 3

    username = getMessage("Username: ")
    password = getMessage("Password: ")

    if option == 1:
        success, id = Register(URL, username, password)
        option = 2
    if option != 2 or not success:
        return 

    token = Login(URL, username, password)

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