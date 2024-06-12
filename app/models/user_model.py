import json

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.database import db

class User(UserMixin, db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(50), nullable=False)
    roles = db.Column(db.String(50), nullable=False)
    
    def __init__(self, username, password, roles=["users"]):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.roles = json.dumps(roles)
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()
        