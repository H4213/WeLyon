#! /usr/bin/python
# -*- coding:utf-8 -*-

#constants
VELOV_DATA_SOURCE = "https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json"
VELOV_DATA_REFRESH_INTERVAL = 20

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import threading
import os
from flask import Flask, flash, render_template, request, session, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

from server import velov

from server import service

from src.model import User, Pin, Category

app = Flask(__name__)
db = service.connectToDatabase()

@app.route('/', methods=('GET', 'POST'))
def index():
  record = Pin.query.first()
  if record:
    print "test1"
  else:
    print "sdqg"
  return "Hi Bitches"

#Affichage des différents marqueurs enregistrés
@app.route('/pins/')
@app.route('/pins/<category>/')
def pins(category = None):
  return service.getAllPin(category)

@app.route('/pin/<idPin>/')
def pin(idPin = None):
  return service.getPinById(idPin)

@app.route('/user')
def user():
  print "user\n"
  return service.getAllUser()

@app.route('/categories/')
@app.route('/categories/<pin>/')
def categories(pin = None):
  return service.getAllCategory(pin)

@app.route('/category/<category>/')
def category(category = None):
  return service.getCategoryById(category)

#renvoie l'id après l'authentification de l'utilisateur
@app.route('/auth', methods=('GET', 'POST'))
def auth():
  if request.method == 'POST':
    return service.authentificaton(request.form)
  return jsonify(error="false request")

#ajout d'un marqueur
@app.route('/add/pin', methods=('GET', 'POST'))
def addPin():
  if request.method == 'POST':
    return service.addPin(request.form)
  return jsonify(error="false request")

#inscription d'un utilisateur
@app.route('/add/user', methods=('GET', 'POST'))
def addUser():
  if request.method == 'POST':
    return service.addUser(request.form)
  return jsonify(error="false request")

@app.route('/delete/<obj>/<id>/')
@app.route('/delete/<obj>/<id>/')
@app.route('/delete/<obj>/<id>/')
def delete(obj = None, id = None):
  if (obj == "user"):
    db.session.delete(User.query.get(id))
  elif(obj == "pin"):
    db.session.delete(Pin.query.get(id))
  elif(obj == "category"):
    db.session.delete(Category.query.get(id))
  else:
    return jsonify(retour = "0") #No object deleted

  db.session.commit()
  return jsonify(retour = "1") #object deleted


#test
@app.route('/test', methods=('GET', 'POST'))
def test():
  if request.method == 'POST':
    return service.test(request.form)
  return jsonify(error="false request")

@app.route('/test2')
def test2():
  print "0"

  cat1 = Category.query.get(7)

  print str(cat1.nom)

  

  print "1"
  pun = Pin("1&er", 123, 134)

  #cat1.pins.append(pun)

  print "2"
  #db.session.add(pun)
  print "3"

  #db.session.commit()

  print "5"


  return str(cat1.pins[2].title)

@app.route('/test3')
def test3():
  print "--------------------------------\n\n\n"

  pin = Pin.query.filter_by(title="1er").first()
  print str(pin.id)
  print pin.title
  print str(pin.categories)

  return pin.categories[0].id

@app.route('/useer')
def displaye():
  print "useer"
  return render_template('JSON.html')


@app.errorhandler(404)
def page_not_found(error):
    return jsonify(error="404"), 404
	

#lance le rafraichissement periodique des données velov
def start_velov_data(tempo = 60.0):
	velov.refreshVelovData(VELOV_DATA_SOURCE)
	threading.Timer(tempo, start_velov_data, [tempo]).start()
	

if __name__ == '__main__':
	
	service.logMessage("Démarrage du serveur")
	#app.debug = True
	#app.run()
	
	
	service.logMessage("Lancement du rafraichissement des donnees Velov")
	start_velov_data(VELOV_DATA_REFRESH_INTERVAL)
  #port = int(os.environ.get("PORT", 5000))
  #app.run(host='0.0.0.0', port=port)