# tabela assocjacyjna 
from extensions import db

User_Character = db.Table( 
    'User_Character',
    db.Column('User_id', db.Integer, db.ForeignKey('User.id'), primary_key=True),
    db.Column('Character_Name', db.Integer, db.ForeignKey('Character.Name'), primary_key=True)
)