from flask import Flask
from extensions import db, migrate
from __init__ import create_app

app = create_app()

with app.app_context():
    from flask_migrate import upgrade, migrate as flask_migrate, init, stamp
    import os

    # Jeœli jeszcze nie ma folderu migrations:
    if not os.path.exists('migrations'):
        init()
        stamp()  # oznacza obecn¹ strukturê jako aktualn¹

    flask_migrate(message="Auto migration")
    upgrade()
    print("Migration applied!")