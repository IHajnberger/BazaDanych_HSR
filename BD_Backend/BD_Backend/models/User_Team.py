# tabela assocjacyjna 
from extensions import db

User_Team = db.Table( 
    'User_Team',
    db.Column('User_id', db.Integer, db.ForeignKey('User.id'), primary_key=True),
    db.Column('Team_id', db.Integer, db.ForeignKey('Team.id'), primary_key=True)
)
