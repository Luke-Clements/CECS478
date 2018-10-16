import os
from allEncryption import messageEncryptMAC
from fileManagement import saveFileAsJSON
from allDecryption import fileDecrypt
from getMessage import getMessage

def flowControl():
    # bool keepChatting = True
    while True:
        userContinue = getMessage("Would you like to keep chatting(Y/N)? ").lower()

        if userContinue != "yes" and userContinue != "y":
            break
        # display list of persons from which messages have been received, but not read
        # select person to send message to
        # retrieve person and chat from local
            # user should have option to read, but not send any additional message
        message = getMessage("Luke").encode()

        ciphertext, iv, tag, ENCKey, HMACKey = messageEncryptMAC(message)
        # print("Ciphertext: " + ciphertext.decode() + "\n")

        #for testing purposes only
        testDir = os.getcwd() + "/testDir"

        saveFileAsJSON(testDir + "/message", ciphertext, iv, tag, ENCKey, HMACKey)

        messageDecrypted, ext = fileDecrypt(workingDir)
        # send message to person
