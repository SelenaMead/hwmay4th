from enum import unique
import uuid
from datetime import datetime as dt
from app import db
from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(300))
    #posts = db.relationship('Post', backref='posts', cascade='all, delete-orphan')

    def generate_password(self, password_from_form):
        self.password = generate_password_hash(password_from_form)

    def check_password(self, password_from_form):
        return check_password_hash(self.password, password_from_form)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid.uuid4().hex

    def __repr__(self):
        return f'<User: {self.email}>'