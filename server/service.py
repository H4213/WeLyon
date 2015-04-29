from src import model
from src.model import User, Pin, Category, Velov , FacebookPin
from flask import Flask, flash, render_template, request, session
from flask.ext.jsonpify import jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

def logMessage(message):
	print("[LOG]["+time.strftime("%H:%M:%S") + "] "+message)
def errorMessage(message):
	print("[ERROR]["+time.strftime("%H:%M:%S") + "] "+message)

def connectToDatabase():
    """
    Connect to our SQLite database and return a Session object
    """
    session = model.db
    return session

db = connectToDatabase()

#---------------------------------------------------
#--------------------------Pin----------------------
def getPin(idCategory):
	"""
	request for all pins
	"""
	if (category):
		cat = Category.query.get(category)
		if cat:
			items = cat.pins 
		else:
			items = []
	else:
		items = Pin.query.all()
	if items:
		print "Pins non vides"
		return jsonify(pins=[item.serialize() for item in items])
	print "pins vide"
	return jsonify(error="No pins")

def getPinById(idPin):
	print idPin
	if idPin:
		item = Pin.query.get(int(idPin))

		print item.id

		if item:
			return jsonify(pin = [item.serialize()])

		return jsonify(error="No pin")

	else:
		items = Pin.query.all()
		return jsonify(pins=[item.serialize() for item in items])

	return jsonify(error = "Invalid parameters")

def addPin(form):
	print "addPin"
	if (form['title'] and form['user'] and form['lng'] and form['lat']):
		exist = Pin.query.filter_by(title=form['title'], lng=form['lng'], lat=form['lat']).first()
		
		if exist:
			return jsonify(error="already exists")

		user = User.query.get(form['user'])

		if not(user):
			return jsonify(error="user doesn't exist")
		
		#FAUX pin = Pin(form['title'], float(form['lng']), float(form['lat']), form['user'], form['category'], form['description'])
	
		db.session.add(form)
		db.session.commit()
		
		return jsonify(pin = pin.serialize()) 
		
	return jsonify(error="invalid parameters")

def majPin(form):
	return "0"

#---------------------------------------------------
#--------------------------User---------------------
def getAllUser(idUser):
	print "getAllUser"

	items = User.query.all()

	print "query faite"

	if items :
		print "users non vide"
		return jsonify(users=[item.serialize() for item in items])

	print "user vide"
	return jsonify(error="No user")


def addUser(form):
	if (form['pseudo'] and form['passw']):

		exist = User.query.filter_by(pseudo=form['pseudo']).first()

		if exist:
	
			return jsonify(error="already exist")

		user = User(form['pseudo'], form['passw'])

		db.session.add(user)
		db.session.commit()

		return jsonify(id=user.id, pseudo=user.pseudo)

	return jsonify(error="invalid parameters")

def majUser(form):
	return "0"

#---------------------------------------------------
#--------------------------Category-----------------
def getCategory(idPin, rank = 0):
	print "displayCategories"
	#id de la pin

	if idPin:
		pin = Pin.query.get(idPin)
		if pin:
			items = pin.categories
		else:
			return jsonify(categories=[])
	else:
		items = Category.query.all()
		#items = Category.query.filter_by(rank > rank).all()

	if items :
		print "categories non vide"
		return jsonify(categories=[item.serialize() for item in items])

	print "Category vide"
	return jsonify(error="No category")

def getCategoryByName(category, rank = 0):
	print "displayCategory"
	if category:
		item = Category.query.filter_by(nom=category).first()

		if item:
			return jsonify(categories=[item.serialize()])

		return jsonify(error="No category")
	else:
		items = Category.query.all()
		#items = Category.query.filter_by(rank > rank).all()

	if items :
		print "categories non vide"
		return jsonify(categories=[item.serialize() for item in items])

	return jsonify(error = "No Category")

def addCategory(form):
	if (Category(form['name'] and form['description'] and form['idFather']):

		exist = Category.query.filter_by(nom=form['name']).first()

		if exist:
	
			return jsonify(error="already exist")

		item = Category(form['name'], form['description'])
		father = Category.query.get(form['idFather'])
		if father:
			item.categoryFather = father
			
		db.session.add(item)
		db.session.commit()

		return jsonify(categories=[item.serialize()])

	return jsonify(error="invalid parameters")
	

def majCategory(form):
	return "0"
	

def authentification(form):
	user = User.query.filter_by(pseudo=form['pseudo'], passw=form['passw']).first()
	if user:
		return jsonify(id=user.id, pseudo=user.pseudo)
	return jsonify(error="authentification error")

	
#updates or creates a velov 
def updateVelovByIdVelov(current):
	if current:
		item = Velov.query.filter_by(idVelov=current.idVelov).first()
		
		if item:
			item.velo = current.velo
			item.libre = current.libre
			db.session.commit()
		else:
			addPin(current)
		
#Creates Facebook events 
def updateFacebookByIdFacebook(current):
	if current:
		item = FacebookPin.query.filter_by(idFacebook=current.idFacebook).first()
		
		if item == None:
			addPin(current)