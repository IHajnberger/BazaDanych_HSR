# warstwa kontaktowa z aplikacja - interfejs
from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
from models.Character import Character

api_bp = Blueprint("api", __name__)

#test 
@api_bp.route("/")
def home():
    return "API dziala!"

# READ ALL characters
@api_bp.route("/characters", methods=["GET"])
def get_characters():
    characters = Character.query.all()
    return jsonify([c.to_dict() for c in characters])

# READ one character
@api_bp.route("/characters/<string:name>", methods=["GET"])
def get_character(name):
    character = Character.query.get_or_404(name)
    return jsonify(character.to_dict())

@api_bp.route("/characters", methods=["POST"])
def create_character():
    data = request.json

    # sprawdzamy, czy postaæ ju¿ istnieje
    if Character.query.filter_by(Name=data["Name"]).first():
        return {"message": "Character already exists"}, 400

    # tworzymy obiekt z wszystkimi wymaganymi polami
    character = Character(
        Name=data["Name"],
        Role=data["Role"],
        Element=data["Element"],
        Path=data["Path"]
    )

    db.session.add(character)
    db.session.commit()
    return jsonify(character.to_dict()), 201


# UPDATE character
@api_bp.route("/characters/<string:name>", methods=["PUT"])
def update_character(name):
    character = Character.query.get_or_404(name)
    data = request.json
    character.Role = data.get("Role", character.Role)
    db.session.commit()
    return jsonify(character.to_dict())

# DELETE character
@api_bp.route("/characters/<string:name>", methods=["DELETE"])
def delete_character(name):
    character = Character.query.get_or_404(name)
    db.session.delete(character)
    db.session.commit()
    return jsonify({"message": f"Character {name} deleted"})

# register
@api_bp.route("/register", methods=["POST"])
def register():
    data = request.json or {}

    if "username" not in data or "password" not in data:
        return {"message": "Missing username or password"}, 400

    if User.query.filter_by(Username=data["username"]).first():
        return {"message": "Username already exists"}, 400

    # tworzymy u¿ytkownika z poprawnym polem
    user = User(Username=data["username"])
    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    # zwracamy tylko bezpieczne dane
    return {"id": user.id, "username": user.Username}, 201

#login
@api_bp.route("/login", methods=["POST"])
def login():
    data = request.json or {}

    user = User.query.filter_by(Username=data["username"]).first()
    if not user or not user.check_password(data["password"]):
        return {"message": "Invalid credentials"}, 401

    return {"message": "Login successful", "user_id": user.id}


