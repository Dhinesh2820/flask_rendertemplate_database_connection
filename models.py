from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import LargeBinary
from flask_migrate import Migrate

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    age=db.Column(db.Integer)
    location=db.Column(db.String(255))
    phone=db.Column(db.String(500))
    address=db.Column(db.String(500))
    data=db.Column(db.LargeBinary)
    registration_status = db.Column(db.Boolean, default=False)
    company = db.Column(db.String(255))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Float)
    discount =db.Column(db.Integer)
    
    
class Image(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    data=db.Column(db.LargeBinary)