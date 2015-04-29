# Smart-City - Serveur

##Affichage des marqueurs
###/pins  ou  /pins/category/"idCatégorie" (catégorie = le id de la catégorie)
###/pin/"id" (id = id de la pin)
Affichage JSON de tous les marqueurs
{
  "pins": [ 
    {
      "category": [
        {
          "id": 7, 
          "nom": "Resto"
        }
      ], 
      "description": "", 
      "id": 7, 
      "lat": 134.0, 
      "lng": 123.0, 
      "title": "10er", 
      "user": 1
    }
  ]
}

##Affichage des catégories
###/categories ou /categories/pin/"idPin" (pin = le id de la pin)
###/category/"id" (id = id de la catégorie)
Affichage JSON de toutes les catégories
{
  "categories": [
    {
      "description": "", 
      "id": 7, 
      "nom": "Resto", 
      "pins": [
        {
          "id": 5, 
          "title": "4er"
        }
      ]
    }
  ]
}

##Affichage des utilisateurs
###/user
Affichage JSON de tous les utilisateurs (pseudo + pass)
{
  "users": [
    {
      "id": 1, 
      "passw": "pass", 
      "pseudo": "Arthur"
    }
  ]
}

##Authentification d'un utilisateur
###/auth
Vérifie l'authentification et renvoie son id
POST : 	*pseudo
	*passw

{
	"id": "1",
	"pseudo": "Arthur"
}

##Ajout d'un markeur
###/add/pin
Vérifie qu'il n'y a pas un doublon sur la positon.
Renvoie l'ID du nouveau marker
POST : 	*user (id)
	*title
	description
	cathegorie
	*lng
	*lat

##Inscription d'un utilisateur
###/add/user
Vérifie qu'il n'y a pas un doublon sur le pseudo.
Renvoie l'ID du nouvel user
POST : 	*pseudo
	*passw

##Delete d'un objet
###/delete/<obj>/<id>/
obj : 'user', 'pin', 'category'
id : id de l'objet

{
	"retour" : "1" (0 si erreur)
}


