# tabela assocjacyjna 
from extensions import db

Character_Need = db.Table(
    'Character_Need',
    db.Column('Character_Name', db.String(100), db.ForeignKey('Character.Name'), primary_key=True),
    db.Column('Need_id', db.Integer, db.ForeignKey('Need.id'), primary_key=True)
)