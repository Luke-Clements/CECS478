import os                                                            # used for getting directory 
from allEncryption import RSAEncrypt                                 # calls to encrypter
from fileManagement import saveMessageAsJSON, loadMessageFromJSON    # allows saving/loading JSON
from allDecryption import RSADecrypt                                 # calls to decrypter
from getMessage import getMessage                                    # collects user input for message
from keyPaths import keyPaths                                        # path to public + private key

def flowControl():

    while True:
        userContinue = getMessage("Would you like to keep chatting(Y/N)? ").lower()     # prompt user for Y/N

        if userContinue != "yes" and userContinue != "y":   # run if answer "yes" or "y", else 
            break
        # display list of persons from which messages have been received, but not read
        # select person to send message to
        # retrieve person and chat from local
            # user should have option to read, but not send any additional message
        message = getMessage("Luke").encode() # user input, encode
        # message.encode("utf-8")

        print(message)         # print message             
        RSACipher, ciphertext, iv, tag = RSAEncrypt(message, keyPaths.pathToPublicKey) #pass in message + pubkey to Encrypt
        print(ciphertext)      # print ciphertext
        #print(tag)             # print HMAC tag 

        #for testing purposes only
        #testDir = os.getcwd() + "\\testDir" #Windows # gets system directory + test directory
        testDir = os.getcwd() + "/testDir" # gets system directory + test directory
        
        # print(type(ciphertext))
        # need to come up with a message naming system to append to "message"
        #saveMessageAsJSON(testDir + "\\m.json", RSACipher, ciphertext, iv, tag) #Windows #saves as JSON file
        saveMessageAsJSON(testDir + "/m.json", RSACipher, ciphertext, iv, tag) #saves as JSON file

        # send message to person

        # for testing only
        #RSACipher, text, iv, tag = loadMessageFromJSON(testDir + "\\m.json") #Windows #takes from JSON file
        RSACipher, text, iv, tag = loadMessageFromJSON(testDir + "/m.json") #takes from JSON file
        messageDecrypted = RSADecrypt(RSACipher, text, iv, tag, keyPaths.pathToPrivateKey)
        print(messageDecrypted)   #prints decrypted message
        
