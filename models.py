from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import LargeBinary
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    age=db.Column(db.Integer)
    location=db.Column(db.String(255))
    phone=db.Column(db.String(500))
    address=db.Column(db.String(500))


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Float)
    
    
class Image(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    data=db.Column(LargeBinary)