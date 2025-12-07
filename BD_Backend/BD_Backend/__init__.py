# centrala aplikacji Flask
from flask import Flask
from config import Config
from extensions import db

from models.user import User
from models.Team import Team
from models.Character import Character
from models.Need import Need
from models.Skill import Skill
from models.Effect import Effect


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Tworzenie tabel
    with app.app_context():
        db.create_all()

    # Import i rejestracja routow
    from views import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
