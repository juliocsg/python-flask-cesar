from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

class User(db.Model):
    #autoincremento automático en el id
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)
    email = db.Column(db.String(40))
    #crearía un hash de 66 caracteres
    password = db.Column(db.String(66))
    create_date = db.Column(db.DateTime, default = datetime.datetime.now)
