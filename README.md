# Smart-City - Serveur

##Affichage des Pins
@app.route('/pins/'rank'', methods=('GET', 'POST', 'PUT', 'DELETE'))<br>
@app.route('/pins/'idPin'/'rank'')<br>
@app.route('/pins/category/'category'/'rank'')<br>
Affichage JSON de tous les marqueurs

##Affichage des catégories
@app.route('/categories/', methods=('GET', 'POST', 'PUT', 'DELETE'))<br>
@app.route('/categories/'category'/')<br>
@app.route('/categories/pin/'pin'/')<br>

##Affichage des utilisateurs
@app.route('/users', methods=('GET', 'POST', 'PUT', 'DELETE'))<br>
@app.route('/users/'idUser'/')<br>
Affichage JSON de tous les utilisateurs (pseudo + pass)<br>

##Authentification d'un utilisateur
@app.route('/authentification', methods=('GET', 'POST'))<br>
Vérifie l'authentification et renvoie son id<br>
POST : 	*pseudo<br>
	*passw<br>

##Ajout d'un objet
###pin
Vérifie qu'il n'y a pas un doublon sur la positon.<br>
Renvoie l'ID du nouveau marker<br>
PUT : 	*user (id)<br>
	*title<br>
	description<br>
	idCathegorie<br>
	*lng<br>
	*lat<br>


###user
Vérifie qu'il n'y a pas un doublon sur le pseudo.<br>
Renvoie l'ID du nouvel user<br>
PUT : 	*pseudo<br>
	*passw<br>

###Catégorie
PUT:  name<br>
      description<br>
      idFather (catégorie parente ex: Transport -> TCL, Velov, etc...)<br>


