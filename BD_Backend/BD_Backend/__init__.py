# centrala aplikacji Flask
from flask import Flask
from flask import redirect, request
from config import Config
from extensions import db, migrate

from models.user import User
from models.Team import Team
from models.Character import Character
from models.Need import Need
from models.Skill import Skill
from models.Effect import Effect

PROTECTED_ROUTES = {"/main", "/characters", "/teams"}

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)  # do testów
    
    # Tworzenie tabel
    with app.app_context():
        db.create_all()

    # Import i rejestracja routow
    from views import api_bp
    from views_html import pages_bp

    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(pages_bp)

    # Middleware do ochrony routow
    @app.before_request
    def require_login():
        path = request.path

        if path.startswith("/static") or path.startswith("/api"):
            return

        if path in PROTECTED_ROUTES:
            if not request.cookies.get("logged_in"):
                return redirect("/")

    return app