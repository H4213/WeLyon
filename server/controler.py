from model import modele
from model.modele import User, Marker
from flask import Flask, flash, render_template, request, session, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connectToDatabase():
    """
    Connect to our SQLite database and return a Session object
    """
    session = modele.db
    return session

db = connectToDatabase()

def marker(cathegorie):
	"""
	request for all markers
	"""
	if (cathegorie):
		items = Marker.query.filter_by(cathegorie=cathegorie).all()
	else:
		items = Marker.query.all()

	if not(items):
		print "Markers vides"

	return jsonify(markers=[item.serialize() for item in items])

def displayUser():
	print "displayUser()"

	items = User.query.all()

	print "query faite"

	if items :
		print "users non vide"
		return jsonify(users=[item.serialize() for item in items])

	print "user vide"
	return jsonify(error="No user")

	

def authentification(form):
	user = User.query.filter_by(pseudo=form['pseudo'], passw=form['passw']).first()
	if user:
		return jsonify(id=user.id, pseudo=user.pseudo)
	return jsonify(error="authentification error")

def addMarker(form):
	print "addMarker"
	if (form['title'] and form['user'] and form['lng'] and form['lat']):
		exist = Marker.query.filter_by(title=form['title'], lng=form['lng'], lat=form['lat']).first()
		
		if exist:
			return jsonify(error="already exists")

		user = User.query.get(form['user'])

		if not(user):
			return jsonify(error="user doesn't exist")
		
		marker = Marker(form['title'], float(form['lng']), float(form['lat']), form['user'], form['cathegorie'], form['description'])
		
		db.session.add(marker)
		db.session.commit()
		
		return jsonify(marker = marker.serialize) 
		
	return jsonify(error="invalid parameters")

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



def test(form):
	return form['name']

"""def paiment():"""