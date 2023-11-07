from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserInput(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=True)
    model = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    anyModel = db.Column(db.Boolean, default=False)
