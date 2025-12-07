# tabela assocjacyjna 
from extensions import db

Skill_Effect = db.Table(
    "Skill_Effect",
    db.Column("Skill_id", db.Integer, db.ForeignKey("Skill.Name"), primary_key=True),
    db.Column("Effect_id", db.Integer, db.ForeignKey("Effect.id"), primary_key=True),
)