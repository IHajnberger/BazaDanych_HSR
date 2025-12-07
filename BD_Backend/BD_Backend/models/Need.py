from extensions import db

from models.Character_Need import Character_Need

class Need(db.Model):
    __tablename__ = "Need"
    id = db.Column(db.Integer, primary_key=True)
    Require = db.Column(db.String(100), nullable=True)

    Characters = db.relationship('Character', secondary=Character_Need, back_populates='Needs') # relacja wiele do wielu

    def to_dict(self):
        return {"id": self.id, "Require": self.Require}
