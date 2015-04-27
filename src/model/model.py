# model.py

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy import Table, Column, create_engine
from sqlalchemy import Integer, ForeignKey, String, Unicode, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tmucotknskzdvn:B5Hyna3G7I1xIhPj3i_CSdl-GS@ec2-54-163-238-96.compute-1.amazonaws.com:5432/d6fisokcj01ulm'
db = SQLAlchemy(app)
 
########################################################################
class User(db.Model):
    """"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    pseudo = db.Column(db.String(20))
    #mail = db.Column(db.String(50))
    passw = db.Column(db.String(20))

    def __init__(self, username, passw):
        self.pseudo = username
        self.passw = passw

    def serialize(self):
        return {
            'id': self.id,
            'pseudo': self.pseudo,
            'passw': self.passw,
        }

    #------------------------------------------------------------------

class Marker(db.Model):
    __tablename__ = "marker"
    id = db.Column(db.Integer, primary_key = True)
    idUser = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(20))
    cathegorie = db.Column(db.String(20))
    description = db.Column(db.String(400)) 
    lng = db.Column(db.Float)
    lat = db.Column(db.Float)

    def __init__(self, title, lng, lat, idUser = -1, cathegorie = "", description = ""):
        self.idUser = idUser
        self.title = title
        self.cathegorie = cathegorie
        self.description = description
        self.lng = lng
        self.lat = lat

    def serialize(self):
        return {
            'id': self.id,
            'user': self.idUser,
            'title': self.title,
            'cathegorie': self.cathegorie,
            'description': self.description,
            'lng': self.lng,
            'lat': self.lat,
        }
    #------------------------------------------------------------------
 
db.create_all()