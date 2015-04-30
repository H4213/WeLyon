# Smart-City - Serveur

##Affichage des Pins
@app.route('/pins/<rank>', methods=('GET', 'POST', 'PUT', 'DELETE'))
@app.route('/pins/<idPin>/<rank>')
@app.route('/pins/category/<category>/<rank>')
Affichage JSON de tous les marqueurs

##Affichage des catégories
@app.route('/categories/', methods=('GET', 'POST', 'PUT', 'DELETE'))
@app.route('/categories/<category>/')
@app.route('/categories/pin/<pin>/')

##Affichage des utilisateurs
@app.route('/users', methods=('GET', 'POST', 'PUT', 'DELETE'))
@app.route('/users/<idUser>/')
Affichage JSON de tous les utilisateurs (pseudo + pass)

##Authentification d'un utilisateur
@app.route('/authentification', methods=('GET', 'POST'))
Vérifie l'authentification et renvoie son id
POST : 	*pseudo
	*passw

##Ajout d'un objet
###pin
Vérifie qu'il n'y a pas un doublon sur la positon.
Renvoie l'ID du nouveau marker
PUT : 	*user (id)
	*title
	description
	idCathegorie
	*lng
	*lat


###user
Vérifie qu'il n'y a pas un doublon sur le pseudo.
Renvoie l'ID du nouvel user
PUT : 	*pseudo
	*passw

###Catégorie
PUT:  name
      description
      idFather (catégorie parente ex: Transport -> TCL, Velov, etc...)


