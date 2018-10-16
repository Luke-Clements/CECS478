import os
from allEncryption import RSAEncrypt
from fileManagement import saveMessageAsJSON, loadMessageFromJSON
from allDecryption import RSADecrypt
from getMessage import getMessage
from keyPaths import keyPaths

def flowControl():

    while True:
        userContinue = getMessage("Would you like to keep chatting(Y/N)? ").lower()

        if userContinue != "yes" and userContinue != "y":
            break
        # display list of persons from which messages have been received, but not read
        # select person to send message to
        # retrieve person and chat from local
            # user should have option to read, but not send any additional message
        message = getMessage("Luke").encode()
        # message.encode("utf-8")

        print(message)
        RSACipher, ciphertext, iv, tag = RSAEncrypt(message, keyPaths.pathToPublicKey)
        print(ciphertext)

        #for testing purposes only
        testDir = os.getcwd() + "/testDir"

        # print(type(ciphertext))
        # need to come up with a message naming system to append to "message"
        saveMessageAsJSON(testDir + "/m.json", RSACipher, ciphertext, iv, tag)

        # send message to person

        # for testing only
        RSACipher, text, iv, tag = loadMessageFromJSON(testDir + "/m.json")
        messageDecrypted = RSADecrypt(RSACipher, text, iv, tag, keyPaths.pathToPrivateKey)
        print(messageDecrypted)
