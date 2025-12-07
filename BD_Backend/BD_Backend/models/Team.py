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
    
    # do_dict z automatycznym przypisaniem slotow
    def to_dict(self):
        # generowanie slotow na podstawie Character.Role
        slots = {1: None, 2: None, 3: None, 4: None}

        # DPS - slot 1
        for c in self.Characters:
            if c.Role == "DPS":
                slots[1] = c

        # Support - slot 2 i 3
        support_index = 2
        for c in self.Characters:
            if c.Role == "Support":
                if support_index <= 3:
                    slots[support_index] = c
                    support_index += 1

        # Sustain - slot 4
        for c in self.Characters:
            if c.Role == "Sustain":
                slots[4] = c

        return {"id": self.id, "Name": self.Name, "Score": self.Score,
            "Characters": 
            {
                slot: char.Name if char else None
                for slot, char in slots.items()
            }
        }
