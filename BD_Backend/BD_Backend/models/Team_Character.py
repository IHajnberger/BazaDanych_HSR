# tabela assocjacyjna 
from extensions import db

Team_Character= db.Table( 
    'Team_Character',
    db.Column('Character_Name', db.String(100), db.ForeignKey('Character.Name'), primary_key=True),
    db.Column('Team_id', db.Integer, db.ForeignKey('Team.id'), primary_key=True)
)