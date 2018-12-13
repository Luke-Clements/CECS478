import os

class keyPaths:
    pathToPublicKey = os.getcwd() + '/.ssh/rsaKey.pem.pub'  # directory to public .pem
    pathToPrivateKey = os.getcwd() + '/.ssh/rsaKey.pem'     # directory to private .pem

