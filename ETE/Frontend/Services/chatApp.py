import os                                                            # used for getting directory 
from allEncryption import RSAEncrypt                                 # calls to encrypter
# from fileManagement import saveMessageAsJSON, loadMessageFromJSON    # allows saving/loading JSON
from allDecryption import RSADecrypt                                 # calls to decrypter
from getMessage import getMessage                                    # collects user input for message
from keyPaths import keyPaths                                        # path to public + private key
import registrationLogin
import messageInteraction
import friendInteraction

siteURL = "Lukecjm.me"
class flowControlVariables:
    menu = "1: Add Friend\n" + "2: Get Your Info\n" + "3: Chat\n" + "4: Exit\n" + "Please choose from the above: "

def flowControl():

    id = None
    token = None
     
    while id == None or token == None:
        id, token = registrationLogin.RegistrationLogin(siteURL)
        if id == "3":
            break

    while True and id != "3":
        userContinue = getMessage(flowControlVariables.menu);     # prompt user for Y/N

        if userContinue == "4":   # run if answer "yes" or "y", else 
            break

        if userContinue == "1":
            friendName = getMessage("Enter your friend's name: ")
            friendJSON = getMessage("Enter your friend's generated id/publicKey raw json: ")
            friendInteraction.saveFriendToJSON(friendName, friendJSON)
        if userContinue == "2":
            print(friendInteraction.getSelfInfo())
        messageInteraction.messageInteraction(siteURL, token, id)
        
