from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def RSAKeyGen (pathToPrivateKey, pathToPublicKey): # generates private + public key

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend())

    pem = private_key.private_bytes(
       encoding=serialization.Encoding.PEM,
       format=serialization.PrivateFormat.TraditionalOpenSSL,
       encryption_algorithm=serialization.NoEncryption()
    )

    public_key = private_key.public_key()

    pub_pem = public_key.public_bytes(
       encoding=serialization.Encoding.PEM,
       format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open(pathToPrivateKey, 'wb') as privatePEM:
        privatePEM.write(pem)

    with open(pathToPublicKey, 'wb') as publicPEM:
        publicPEM.write(pub_pem)

    privatePEM.close()
    publicPEM.close()

