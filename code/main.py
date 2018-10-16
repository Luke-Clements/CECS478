from allEncryption import encryptDirectory          # call to encrypt
from allDecryption import decryptDirectory          # call to decrypt
from RSAKeyGen import RSAKeyGen                     # generates public + private
from keyPaths import keyPaths                       # points to current public + private
from fileManagement import saveFileAsJSON, saveFile  
import chatApp
import os                                           # used for finding directory 

def main():
    #-----------------------------String test-----------------------------
    #print('\n\nBEGIN MYENCRYPT AND MYDECRYPT STRING TEST')
    #string_to_enc = "This is the test string to test out the encryption and decryption $
    #print('string to encrypt: ' + string_to_enc)
    #string_enc = encrypt.encrypt(string_key, string_to_enc, string_IV)

#    print('encrypted string: ' + string_enc.decode("utf-8"))
    #string_dec = decrypt.decrypt(string_enc, string_key, string_IV)
    #print('decrypted string: ' + string_dec.decode("ascii"))
    #print('END MYENCRYPT AND MYDECRYPT STRING TEST')
    #-----------------------------/String test----------------------------

    if(not os.path.isfile(keyPaths.pathToPrivateKey) and not os.path.isfile(keyPaths.pathToPublicKey)): # If no Public + Private key, generate
        RSAKeyGen(keyPaths.pathToPrivateKey, keyPaths.pathToPublicKey)
    # workingDirectory = os.getcwd()                                        # get computer directory
    # filePathToDirectory = workingDirectory +"/testDir"                    # add computer directory with test directory

    # encryptDirectory(filePathToDirectory)        # From allEncryption, encrypt
                                                   # point to test directory

    # decryptDirectory(filePathToDirectory)        # From allDecryption, decrypt
                                                   # point to test directory 
    chatApp.flowControl()

if __name__ == '__main__':
    main()

