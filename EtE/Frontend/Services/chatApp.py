import os                                                            # used for getting directory 
from allEncryption import RSAEncrypt                                 # calls to encrypter
# from fileManagement import saveMessageAsJSON, loadMessageFromJSON    # allows saving/loading JSON
from allDecryption import RSADecrypt                                 # calls to decrypter
from getMessage import getMessage                                    # collects user input for message
from keyPaths import keyPaths                                        # path to public + private key
import registrationLogin
import messageInteraction

siteURL = "Lukecjm.me"

def flowControl():

    id = None
    token = None
     
    while id == None or token == None:
        id, token = registrationLogin.RegistrationLogin(siteURL)
        if id == 3:
            break

    while True and id != 3:
        userContinue = getMessage("Would you like to keep chatting(Y/N)? ").lower()     # prompt user for Y/N

        if userContinue != "yes" and userContinue != "y":   # run if answer "yes" or "y", else 
            break

        messageInteraction.messageInteraction(siteURL, token, id)
        
