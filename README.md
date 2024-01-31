Ugo Tafaro et Loïs Blin

# Lien github
https://github.com/ugotafaro/TP_Redis


# TP_Redis
Pour utiliser le code:

On commence par lancer un serveur Redis et ensuite on lance la page index.
On arrive ensuite sur une page de connexion. 
vous pouvez remplir les champs requis et vous connecter à la page d'accueil si vous êtes enregistrer dans la base de données.

## Base de données 
Se créer un utilisateur



## Fonctionnalité check connection:
A chaque nouvelle connection on fait appelle à une fonction python (Predis) qui check si l'utilisateur peut se connecter ou non.
Le critère est que l'utilisateur s'est connecté moins de 10 fois dans les 10 minutes.
On va stocker la date (à la minute près de la connexion), si cela fait moins de 10 min que l'utilisateur s'est connecté pour la dernière fois alors on incrémente de 1 le nombre de connexion depuis les 10 dernières minutes, si la dernière connexion date de plus de 10 min, on remet la valeur du nombre de connexion à 1.
On se sert du server redis comme base de donnée temporaire ou on stock le nombre de connection de l'utilisateur dans les 
10 dernière minutes si ce nombre et superieure à 10 on bloque la connection et si c'est inferieure on l'autorise.


## Sur le fichier PHP
- On vérifie la connexion de l'utilisateur, à chaque fois que l'utilisateur valide le formulaire, on vérifie ses identifiants et si le résultat de notre fonction est 'true', dans ce cas-là, on peut connecter l'utilisateur sinon on renvoie une erreur
- Bien penser à modifier les informations de connexion de la base de données et mettre le bon path vers python.exe dans la variable $pythonPath