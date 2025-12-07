from extensions import db

from models.Team import User_Team  

from models.Character import User_Character

from werkzeug.security import generate_password_hash, check_password_hash # do bezpiecznego przechowywania hase³

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), unique=True, nullable=False)
    Password_hash = db.Column(db.String(120), nullable=False)

    Teams = db.relationship('Team', secondary=User_Team, back_populates='Users') # relacja wiele do wielu
    Characters = db.relationship('Character', secondary=User_Character, back_populates='Users') # relacja wiele do wielu
    
    def set_password(self, pwd):
        self.Password_hash = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.Password_hash, pwd)

    def to_dict(self):
        return {"id": self.id, "username": self.Username, "password": self.Password_hash}
