# warstwa kontaktowa z aplikacj¹ - interfejs
from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User

api_bp = Blueprint("api", __name__)

#test 
@api_bp.route("/")
def home():
    return "API dziala!"

@api_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    if User.query.filter_by(username=data["username"]).first():
        return {"message": "Username already exists"}, 400

    user = User(username=data["username"])
    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    return user.to_dict(), 201

@api_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()

    if not user or not user.check_password(data["password"]):
        return {"message": "Invalid credentials"}, 401

    return {"message": "Login successful", "user_id": user.id}

