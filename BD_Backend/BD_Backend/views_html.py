# warstwa kontaktowa z HTML - interfejs - moje piek³o nr.2 (te mniejsze)
from flask import Blueprint, render_template

pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@pages_bp.route("/main", methods=["GET"])
def main_page():
    return render_template("main.html")

@pages_bp.route("/characters", methods=["GET"])
def characters_page():
    return render_template("characters.html")

@pages_bp.route("/teams", methods=["GET"])
def teams_page():
    return render_template("teams.html")
