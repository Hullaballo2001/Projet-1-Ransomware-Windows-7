"# Projet-1-Ransomware-Windows-7" 

Fonctionne : 
la fonction F_listeFichiers récupère tous les fichiers d'un dossier dans une liste grâce au module os.walk
Plus de test à faire sur le type de fichier (file or dir)
Deux fonctions F_chiffrement et F_dechiffrement vont chiffrer/déchiffrer les fichiers (en entier pour l'instant) quelque soit le type de fichier (sauf .ini) grâce au module fernet.

Next 1 : Ne chiffrer que les 2000 premiers caractères (Magic bytes) pour gagner en rapidité et pouvoir chiffrer de gros fichiers (fernet ne le peut pas visiblement)
Next 2 : Envoyer par mail les fichier-key et fichier_liste
Next 3 : Tester en partant de la racine pour chiffrer l'esemble du DD, afficher un "tu es sûre d'être sur ta VM?":D 
Next 4 : Voir pour les .ini