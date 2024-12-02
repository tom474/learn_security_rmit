from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# Generate RSA keys
private_key = rsa.generate_private_key(
     public_exponent=65537,
     key_size=2048,
)

public_key = private_key.public_key()

# Serialize keys to PEM format
pem_private_key = private_key.private_bytes(
     encoding=serialization.Encoding.PEM,
     format=serialization.PrivateFormat.PKCS8,
     encryption_algorithm=serialization.NoEncryption()
)

pem_public_key = public_key.public_bytes(
     encoding=serialization.Encoding.PEM,
     format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Encrypt a message using the public key
message = b"Secret message"
ciphertext = public_key.encrypt(
     message,
     padding.OAEP(
         mgf=padding.MGF1(algorithm=hashes.SHA256()),
         algorithm=hashes.SHA256(),
         label=None
     )
)

# Decrypt the message using the private key
decrypted_message = private_key.decrypt(
     ciphertext,
     padding.OAEP(
         mgf=padding.MGF1(algorithm=hashes.SHA256()),
         algorithm=hashes.SHA256(),
         label=None
     )
)

print("Original message:", message)
print("Encrypted message:", ciphertext)
print("Decrypted message:", decrypted_message)
