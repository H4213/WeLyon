# model.py

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy import Table, Column, create_engine
from sqlalchemy import Integer, ForeignKey, String, Unicode, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tmucotknskzdvn:B5Hyna3G7I1xIhPj3i_CSdl-GS@ec2-54-163-238-96.compute-1.amazonaws.com:5432/d6fisokcj01ulm'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://H4213:SabreESS32@82.241.33.248:3306/WeLyon-dev'
db = SQLAlchemy(app)
 
########################################################################
class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    pseudo = db.Column(db.String(20))
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
association_table = Table('associationPinCategory', db.Model.metadata,
    Column('pin_id', Integer, ForeignKey('pins.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

class Category(db.Model):

    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(20))
    description = db.Column(db.String(20))
    #categoryFather = db.Column(db.Integer, db.ForeignKey("categories.id"))
    #pins = db.relationship('Pin', backref='categories',lazy='dynamic')
    #categoriesChild = db.relationship('Category',lazy='dynamic')

    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

    def serialize(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'description': self.description,
            'pins' : [item.serializeSmall() for item in self.pins]
        }

    def serializeSmall(self):
        return {
            'id': self.id,
            'nom': self.nom,
        }

    #------------------------------------------------------------------

class Pin(db.Model):
    __tablename__ = "pins"
    id = db.Column(db.Integer, primary_key = True)
    idUser = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(20))
    categories = db.relationship("Category",
                    secondary=association_table,
                    backref="pins")
    description = db.Column(db.String(400)) 
    lng = db.Column(db.Float)
    lat = db.Column(db.Float)

    __mapper_args__ = {
        'polymorphic_identity':'pins',
        #'polymorphic_on':type
    }

    def __init__(self, title, lng, lat, idUser = 1, categories = [], description = ""):
        self.idUser = idUser
        self.title = title
        self.categories = categories
        self.description = description
        self.lng = lng
        self.lat = lat

    def serialize(self):
        return {
            'id': self.id,
            'user': self.idUser,
            'title': self.title,
            'category': [item.serializeSmall() for item in self.categories],
            'description': self.description,
            'lng': self.lng,
            'lat': self.lat,
        }

    def serializeSmall(self):
        return {
            'id': self.id,
            'title': self.title,
        }
    #------------------------------------------------------------------

class DynamicPin(Pin):
    __tablename__ = "dynamicpins"
    id = Column(db.Integer, db.ForeignKey('pins.id'), primary_key=True)
    dateBegin = Column(db.DateTime)
    dateEnd = Column(db.DateTime)

    __mapper_args__ = {
        'polymorphic_identity':'dynamicpins',
    }

 
db.create_all()
