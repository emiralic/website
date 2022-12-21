from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    podaci = db.Column(db.String(10000))
    datum = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    lozinka=db.Column(db.String(150))
    ime=db.Column(db.String(30))
    prezime=db.Column(db.String(30))
    notes=db.relationship('Note')