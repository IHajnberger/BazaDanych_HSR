from extensions import db

from models.Team_Character import Team_Character

from models.User_Team import User_Team

class Team(db.Model):
    __tablename__ = "Team"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Score = db.Column(db.Integer, nullable=False)

    Characters= db.relationship('Character', secondary=Team_Character, back_populates='Teams') # relacja wiele do wielu
    Users = db.relationship('User', secondary=User_Team, back_populates='Teams') # relacja wiele do wielu
    
    def to_dict(self):
        return {"id": self.id, "Name": self.Name, "Score": self.Score}
