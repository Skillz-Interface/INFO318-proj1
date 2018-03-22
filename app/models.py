from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash



class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    biography = db.Column(db.String(140))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(80))
    location = db.Column(db.String(100))
    datecreated = db.Column(db.Date())
    
    def __init__(self,id, first_name, last_name,gender,location, biography,email,datecreated):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.location = location
        self.biography = biography
        self.email = email
        self.datecreated = datecreated