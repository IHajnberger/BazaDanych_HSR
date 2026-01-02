from extensions import db

from models.Skill_Effect import Skill_Effect

class Skill(db.Model):
    __tablename__ = "Skill"

    Name = db.Column(db.String(100), primary_key=True)
    Description = db.Column(db.String(400), nullable=False)
    CharacterName = db.Column(db.String(100), db.ForeignKey("Character.Name"), nullable=False)

    # Relacja wiele do wielu
    Effects = db.relationship("Effect", secondary=Skill_Effect, back_populates="Skills")

    def to_dict(self):
        return {"Name": self.Name, "Description": self.Description, "Character": self.CharacterName}
