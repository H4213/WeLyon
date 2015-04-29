#! /usr/bin/python
# -*- coding:utf-8 -*-

#constants
VELOV_DATA_SOURCE = "https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json"

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
@app.route('/pins/<rank>', methods=('GET', 'POST', 'PUT', 'DELETE'))
@app.route('/pins/<idPin>/<rank>')
@app.route('/pins/category/<category>/<rank>')
def pins(idPin = None, category = None, rank = None):
  if request.method == "POST":
    return service.majPin(request.form)

  if request.method == 'PUT':
    return service.addPin(request.form)

  if request.method == 'DELETE':
    item = Pin.query.get(id)
    if item:
      db.session.delete(Pin.query.get(id))
      db.session.commit()
      return jsonify(deleted = "1")

    return jsonify(deleted = "0")

  if "/category/" not in request.path:
    return service.getPinByIdOrAll(idPin, rank)

  return service.getPin(category, rank) #category pas indispensable


@app.route('/users', methods=('GET', 'POST', 'PUT', 'DELETE'))
@app.route('/users/<idUser>/')
def user(idUser = None):

  if request.method == "POST":
    return service.majUser(request.form)

  if request.method == 'PUT':
    return service.addUser(request.form)

  if request.method == 'DELETE':
    item = User.query.get(id)
    if item:
      db.session.delete(User.query.get(id))
      db.session.commit()
      return jsonify(deleted = "1")

    return jsonify(deleted = "0")

  return service.getAllUser(idUser) #ou un user par son id

@app.route('/categories/', methods=('GET', 'POST', 'PUT', 'DELETE'))
@app.route('/categories/<category>/')
@app.route('/categories/pin/<pin>/')
def categories(category = None, pin = None):
  if request.method == "POST":
    return service.majCategory(request.form)

  if request.method == 'PUT':
    return service.addCategory(request.form)

  if request.method == 'DELETE':
    item = Category.query.get(id)
    if item:
      db.session.delete(Category.query.get(id))
      db.session.commit()
      return jsonify(deleted = "1")

    return jsonify(deleted = "0")

  if "/pin/" not in request.path:
    return service.getCategoryByNameOrAll(category)

  return service.getCategory(idPin)


#renvoie l'id après l'authentification de l'utilisateur
@app.route('/authentification', methods=('GET', 'POST'))
def auth():
  if request.method == 'POST':
    return service.authentificaton(request.form)
  return jsonify(error="false request")


#test
@app.route('/test', methods=('GET', 'POST'))
def test():
  if request.method == 'POST':
    return service.test(request.form)
  return jsonify(error="false request")

@app.route('/test2')
def test2():
  print "0"

  cat1 = Category("&er","")

  print str(cat1.nom)

  
  db.session.add(cat1)

  print "1"
  pun = Pin("1&er", 123, 134)
  db.session.add(pun)
  cat1.pins.append(pun)

  print "2"

  print "3"

  db.session.commit()

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

@app.route('/test4')
def test4():
  cat1 = Category("1","")
  cat11= Category("11","")
  cat12= Category("12","")

  
  

  print cat1.nom
  print cat11.nom

  db.session.add(cat1)
  db.session.add(cat11)
  db.session.add(cat12)

  cat12.categoryFather = cat1
  cat1.categoriesChild.append(cat11)

 

  db.session.commit()

  return cat1.nom

@app.route('/useer')
def displaye():
  print "useer"
  return render_template('JSON.html')


@app.errorhandler(404)
def page_not_found(error):
    return jsonify(error="404"), 404
	
def start_velov_data():
	t = threading.Timer(60.0, velov.refreshVelovData, [VELOV_DATA_SOURCE])
	t.start()
	

if __name__ == '__main__':
  app.debug = True
  app.run()
  #port = int(os.environ.get("PORT", 5000))
  #app.run(host='0.0.0.0', port=port)