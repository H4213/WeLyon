# Smart-City - Serveur

##Affichage des Pins
@app.route('/pins/'rank'', methods=('GET', 'POST', 'PUT', 'DELETE'))\n
@app.route('/pins/'idPin'/'rank'')\n
@app.route('/pins/category/'category'/'rank'')\n
Affichage JSON de tous les marqueurs

##Affichage des catégories
@app.route('/categories/', methods=('GET', 'POST', 'PUT', 'DELETE'))\n
@app.route('/categories/'category'/')\n
@app.route('/categories/pin/'pin'/')\n

##Affichage des utilisateurs
@app.route('/users', methods=('GET', 'POST', 'PUT', 'DELETE'))\n
@app.route('/users/'idUser'/')\n
Affichage JSON de tous les utilisateurs (pseudo + pass)\n

##Authentification d'un utilisateur
@app.route('/authentification', methods=('GET', 'POST'))\n
Vérifie l'authentification et renvoie son id\n
POST : 	*pseudo\n
	*passw\n

##Ajout d'un objet
###pin
Vérifie qu'il n'y a pas un doublon sur la positon.\n
Renvoie l'ID du nouveau marker\n
PUT : 	*user (id)\n
	*title\n
	description\n
	idCathegorie\n
	*lng\n
	*lat\n


###user
Vérifie qu'il n'y a pas un doublon sur le pseudo.\n
Renvoie l'ID du nouvel user\n
PUT : 	*pseudo\n
	*passw\n

###Catégorie
PUT:  name\n
      description\n
      idFather (catégorie parente ex: Transport -> TCL, Velov, etc...)\n


