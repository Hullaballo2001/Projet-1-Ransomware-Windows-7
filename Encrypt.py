# Generate a random key : The variable key will now have the value of a URL safe base64 encoded key. When using these keys
# to encrypt, make sure to keep them safe, if you lose them you will not be able to decrypt your message.
# This key will have a type of bytes, so if you want a string you can call key.decode() to convert from UTF-8 to Pythons string type.
from cryptography.fernet import Fernet
# génération d'une clé de chiffrement avec le module fernet
key = Fernet.generate_key()

# enregistrement de la clé dans un fichier_key
fichier_key = open('key.key', 'wb')  # Open the file as wb to write bytes
fichier_key.write(key)  # The key is type bytes still
fichier_key.close()

# je vais lire puis écrire dans le même fichier
input_file = 'C:\Users\Admin\Desktop\TEST P1\Test.txt'
output_file = 'C:\Users\Admin\Desktop\TEST P1\Test.txt'

# ouverture et lecture du fichier à chiffrer en mode binaire (byte)
with open(input_file, 'rb') as file:
    data = file.read()  # Read the bytes of the input file

# chiffrement du fichier en entier avec le module fernet
fernet_key = Fernet(key)

try:
    encrypted = fernet_key.encrypt(data)
    print("Valid Key - Successfully encrypted")
except:  # InvalidToken as e:  # Catch any InvalidToken exceptions if the correct key was not provided
    print("Invalid Key - Unsuccessfully encrypted")

# ecriture dans le fichier lui même de son contenu chiffré
with open(output_file, 'wb') as file:
    file.write(encrypted)  # Write the encrypted bytes to the output file


# Note: You can delete input_file here if you want

