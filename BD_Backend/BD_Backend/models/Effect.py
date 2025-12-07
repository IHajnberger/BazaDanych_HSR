from extensions import db

from models.Skill_Effect import Skill_Effect

class Effect(db.Model):
    __tablename__ = "Effect"

    id = db.Column(db.Integer, primary_key=True)
    Name= db.Column(db.String(100), nullable=False)
    Value = db.Column(db.Integer, nullable=True)

    Skills = db.relationship('Skill', secondary=Skill_Effect, back_populates='Effects') # relacja wiele do wielu

    def to_dict(self):
        return {"id": self.id, "Name":self.Name ,"Value": self.Value}
