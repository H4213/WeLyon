#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from flask import Flask, flash, render_template, request, session, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

from controler import control

from model.modele import User, Pin, Category

app = Flask(__name__)
db = control.connectToDatabase()

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
  return control.pins(category)

@app.route('/pin/<idPin>/')
def pin(idPin = None):
  return control.pin(idPin)

@app.route('/user')
def user():
  print "user\n"
  return control.displayUser()

@app.route('/categories/')
@app.route('/categories/<pin>/')
def categories(pin = None):
  return control.displayCategories(pin)

@app.route('/category/<category>/')
def category(category = None):
  return control.displayCategory(category)

#renvoie l'id après l'authentification de l'utilisateur
@app.route('/auth', methods=('GET', 'POST'))
def auth():
  if request.method == 'POST':
    return control.authentificaton(request.form)
  return jsonify(error="false request")

#ajout d'un marqueur
@app.route('/add/pin', methods=('GET', 'POST'))
def addPin():
  if request.method == 'POST':
    return control.addPin(request.form)
  return jsonify(error="false request")

#inscription d'un utilisateur
@app.route('/add/user', methods=('GET', 'POST'))
def addUser():
  if request.method == 'POST':
    return control.addUser(request.form)
  return jsonify(error="false request")



#test
@app.route('/test', methods=('GET', 'POST'))
def test():
  if request.method == 'POST':
    return control.test(request.form)
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

if __name__ == '__main__':
  app.debug = True
  app.run()
  #port = int(os.environ.get("PORT", 5000))
  #app.run(host='0.0.0.0', port=port)