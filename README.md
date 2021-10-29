"# Projet-1-Ransomware-Windows-7" 

- Création de 2 modules Chiffrement.py et SendMail.py, refonte de Main.py pour appeler les fonctions/modules (29/10)
- Vérifier qu'on est bien sur windows sinon exit (29/10)
- Lister l'ensemble des fichiers du dossier cible grâce au module os.walk
- Pour l'instant je ne chiffre que dans un dossier de test car trop long sur C:/Users (17 min, 4472 fichiers, 1.8 Go)
- Chiffrement symétrique avec fernet
- Ne chiffrer que les 5000 premiers caractères pour gagner en rapidité tout en rendant le fichier inexpoitable (29/10)
- Fonctionne sur bcp de types de fichiers, quand ne fonctionne pas poursuite du traitement grâce à la gestion des exceptions avec try/except
- Que ce soit OK ou KO j'alimente un .txt avec le résultat et le chemin pour chaque fichier (29/10)
- Je m'envoie un mail avec 1 PJ sur une adresse gmail bidon et j'efface le .txt joint (29/10) 
- Pour les tests je déchiffre avec un prompt "voulez-vous déchiffrer O/N ?" 
- Si oui demande la clef et déchiffre (29/10) 
- Attention doit déchiffrer les 6756 premiers caractères et non 5000 (29/10) merci Alexandre pour l'info
- (les fichiers qui n'ont pas été chiffrés sont en échec de déchiffrement mais ça ne pose aucun soucis)
- Restauration de l'état initial OK

Axes d'amélioration :
1. Envoyer 2 PJ (la clef et l'historique des chiffrements et effacer les 2 .txt)
2. Améliorer la boucle os.walk pour changer d'echelle et travailler sur C:\Users
3. Change l'extension de l'ensmble des fichiers pour les rendre ininterprétables par Windows/tronquer la fin du nom pour déchiffrement
4. Gérer une liste de fichiers ou dossiers à ne pas chiffrer
5. Changer le fond d'écran avec une image downloadée via une url https://wallpapercave.com/w/wp1914178 ?? = processus
6. "Le code source contient au moins 1 classe"
7. "Le malware affiche un message de Ranson à l’utilisateur avec les instructions à suivre." (et la même ou une autre avec input clef et bouton déchiffrer)
8. "Le malware forme 1 seul exécutable sur son format final"
9. "Le malware s’approprie au moins ~~1 répertoire~~ et 1 processus" (explorer en affichant arborescence dans fenêtre installeur ?)
10. "Le malware écrit dans le registre de Windows" (pour supprimer defender ?)
11. "Le malware s’attaque à des processus en cours d’exécution" (reboot après install/exec + écriture bdd ?)

