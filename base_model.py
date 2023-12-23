from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def password_hash(self, password):
        self.password = generate_password_hash(password)
    
    def __repr__(self) -> str:
        return f'User(username={self.username}, last_name={self.last_name}, password={self.password}, email={self.email})'