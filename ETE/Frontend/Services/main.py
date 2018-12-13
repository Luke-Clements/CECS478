#from allEncryption import encryptDirectory          # call to encrypt
#from allDecryption import decryptDirectory          # call to decrypt
#from RSAKeyGen import RSAKeyGen                     # generates public + private
#from keyPaths import keyPaths                       # points to current public + private
# from fileManagement import saveFileAsJSON, saveFile  
#import chatApp
#import os                                           # used for finding directory 
import registrationLogin
import messageInteraction
import connection
import json
import os
from keyPaths import keyPaths
from RSAKeyGen import RSAKeyGen
import chatApp

def main():
    if(not os.path.isfile(keyPaths.pathToPrivateKey) and not os.path.isfile(keyPaths.pathToPublicKey)): # If no Public + Private key, generate
       RSAKeyGen(keyPaths.pathToPrivateKey, keyPaths.pathToPublicKey)

    chatApp.flowControl()

##Old tests
    # r = registrationLogin.Register("Lukecjm.me", "Luke@testmail.com", "fin")
    # r = registrationLogin.Login("Lukecjm.me", "Luke@testmail.com", "fin")
    # r = messageInteraction.postMessage("Lukecjm.me", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NDQ2ODM5NTh9.i-Y37lcMg66Q0sTKvuBismByPmz4MkfohD-KhSkilSU", "actual test", "5be22fceac402f380af73456", "5c120124802aea2548c90b9b")
    # r = messageInteraction.getMessages("Lukecjm.me", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NDQ2ODM5NTh9.i-Y37lcMg66Q0sTKvuBismByPmz4MkfohD-KhSkilSU", "5c120124802aea2548c90b9b")
    # r = messageInteraction.deleteMessages("Lukecjm.me", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NDQ2ODM5NTh9.i-Y37lcMg66Q0sTKvuBismByPmz4MkfohD-KhSkilSU", "5c120124802aea2548c90b9b")
    # data = connection.GetConnectionResult(r)
    # print(data)

if __name__ == '__main__':
    main()

# 