# coding: utf-8

from cryptography.fernet import Fernet
input_file = 'C:\Users\Admin\Desktop\TEST P1\Test.txt'
output_file = 'C:\Users\Admin\Desktop\TEST P1\Test.txt'

# récupération de la clé de chiffrement
fichier_key = open('key.key', 'rb')
key = fichier_key.read()
fichier_key.close()

f = Fernet(key)  # An example of providing the incorrect key
# ouverture et lecture du fichier à déchiffrer en mode binaire (byte)
with open(input_file, 'rb') as file:
    data = file.read()  # Read the bytes of the input file

# déchiffrement du fichier en entier avec le module fernet
fernet = Fernet(key)

try:
    decrypted = fernet.decrypt(data)
    print("Valid Key - Successfully decrypted")
except:             #InvalidToken as e:  # Catch any InvalidToken exceptions if the correct key was not provided
    print("Invalid Key - Unsuccessfully decrypted")

# ecriture dans le fichier lui même de son contenu déchiffré
with open(output_file, 'wb') as file:
    file.write(decrypted)  # Write the encrypted bytes to the output file
