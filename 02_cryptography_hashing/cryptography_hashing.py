import hashlib

# Open the file in binary mode
with open('yourfile.txt', 'rb') as file:
    file_content = file.read()

# Create a hash object
hash_object = hashlib.sha512()

# Update the hash object with the file content
hash_object.update(file_content)

# Get the hexadecimal digest of the hash
hash_hex = hash_object.hexdigest()
print(hash_hex)
