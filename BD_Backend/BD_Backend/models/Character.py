from extensions import db

from models.Character_Need import Character_Need

from models.User_Character import User_Character

from models.Team_Character import Team_Character

class Character(db.Model):
    __tablename__ = "Character"
    Name = db.Column(db.String(100), primary_key=True) # unikalna nazwa postaci jako klucz g³ówny
    Role = db.Column(db.String(100), nullable=False)
    Element = db.Column(db.String(100), nullable=False)
    Path = db.Column(db.String(100), nullable=False)

    Needs = db.relationship('Need',secondary=Character_Need, back_populates='Characters') # relacja wiele do wielu
    Users = db.relationship('User', secondary=User_Character, back_populates='Characters') # relacja wiele do wielu
    Teams = db.relationship('Team', secondary=Team_Character, back_populates='Characters') # relacja wiele do wielu
    Skills = db.relationship('Skill', back_populates="Character", cascade="all, delete-orphan") # relacja jeden do wielu
    
    def to_dict(self):
        return {"Name": self.Name, "Role": self.Role, "Element": self.Element, "Path": self.Path, "Skills": [s.to_dict() for s in self.Skills]}
