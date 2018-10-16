import os

class keyPaths:
    # these keypaths must reflect the individual system's key storage location. Keep this updated
    pathToPublicKey = os.getcwd() + '/.ssh/rsaKey.pem.pub'  # directory to public .pem
    pathToPrivateKey = os.getcwd() + '/.ssh/rsaKey.pem'     # directory to private .pem

