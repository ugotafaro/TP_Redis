
# TP_Redis
Pour utiliser le code:
on commence par lancer un serveur Redis
et ensuite on lance la page index.
vous arriver ensuite sur une page de connexion 
vous pouvez remplir les champs requis et vous connecter à la page d'acceuil si vous êtes enregistrer dans la bdd

Fonctionnalité check connection:
A chaque nouvelle connection on fait appelle à une fonction python (Predis) qui check si l'utilisateur peut se connecter ou non.
le critère et que l'utilisateur c'est connecté moins de 10 fois dans les 10 minutes.
pour cela on se sert du server redis comme base de donnée temporaire ou on stock le nombre de connection de l'utilisateur dans les 
10 dernière minutes si ce nombre et superieure à 10 on bloque la connection et si c'est inferieure on l'autorise.
 
