from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import datetime
db = SQLAlchemy()

class User(db.Model):
    #autoincremento automático en el id
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)
    email = db.Column(db.String(40))
    #crearía un hash de 66 caracteres
    password = db.Column(db.String(150))
    create_date = db.Column(db.DateTime, default = datetime.datetime.now)
#__ significa que la función será privada
'''def __init__(self, username, email, password):
    #self.id = id
    self.username = username
    self.email = email
    self.password = self.__create_password(password)
def __create_password(self, password):

    return generate_password_hash(password)
'''
