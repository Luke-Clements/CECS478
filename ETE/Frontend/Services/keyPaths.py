import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class keyPaths:
    pathToPublicKey = os.getcwd() + '/.ssh/rsaKey.pem.pub'  # directory to public .pem
    pathToPrivateKey = os.getcwd() + '/.ssh/rsaKey.pem'     # directory to private .pem

def loadRSAPublicKey():

    with open(keyPaths.pathToPublicKey, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key

def loadRSAPrivateKey():

    with open(keyPaths.pathToPrivateKey, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password = None,
            backend = default_backend())

    return private_key