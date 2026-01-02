# warstwa kontaktowa z aplikacja - interfejs
from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
from models.Character import Character
from models.Team import Team


api_bp = Blueprint("api", __name__)

# healthcheck
@api_bp.route("/", methods=["GET"])
def home():
    return {"message": "API is running"}, 200

# ====================================
#             Character
# ====================================

# get all chars
@api_bp.route("/characters", methods=["GET"])
def get_characters():
    return jsonify([c.to_dict() for c in Character.query.all()]), 200

# DELETE character
@api_bp.route("/characters/<string:name>", methods=["DELETE"])
def delete_character(name):
    character = Character.query.get_or_404(name)
    db.session.delete(character)
    db.session.commit()
    return jsonify({"message": f"Character {name} deleted"})

# ====================================
#               User
# ====================================

# register
@api_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)
    if not data or "username" not in data or "password" not in data:
        return {"message": "Missing username or password"}, 400

    if User.query.filter_by(Username=data["username"]).first():
        return {"message": "Username already exists"}, 409

    user = User(Username=data["username"])
    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    return {"id": user.id, "username": user.Username}, 201


#login
@api_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)
    if not data:
        return {"message": "Invalid JSON body"}, 400

    user = User.query.filter_by(Username=data.get("username")).first()
    if not user or not user.check_password(data.get("password")):
        return {"message": "Invalid credentials"}, 401

    return {"message": "Login successful", "user_id": user.id}, 200

# ====================================
#          User-Character
# ====================================

# return list of chars
@api_bp.route("/users/<int:user_id>/characters", methods=["GET"])
def get_user_characters(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify([c.to_dict() for c in user.Characters]), 200

@api_bp.route("/users/<int:user_id>/characters", methods=["POST"])
def add_character_to_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json(silent=True)

    if not data or "Name" not in data:
        return {"message": "Missing character name"}, 400

    character = Character.query.filter_by(Name=data["Name"]).first()
    if not character:
        return {"message": "Character not found"}, 404

    if character in user.Characters:
        return {"message": "Character already assigned"}, 409

    user.Characters.append(character)
    db.session.commit()

    return {"message": "Character assigned"}, 201

# ====================================
#               Team
# ====================================

@api_bp.route("/users/<int:user_id>/teams", methods=["GET"])
def get_user_teams(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify([t.to_dict() for t in user.Teams]), 200


@api_bp.route("/users/<int:user_id>/teams", methods=["POST"])
def create_team(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json(silent=True)

    if not data or "Name" not in data or "characters" not in data:
        return {"message": "Invalid team data"}, 400

    if not 1 <= len(data["characters"]) <= 4:
        return {"message": "Team must have 4 characters"}, 400

    characters = []
    for name in data["characters"]:
        char = Character.query.filter_by(Name=name).first()
        if not char or char not in user.Characters:
            return {"message": f"Character {name} not assigned to user"}, 400
        characters.append(char)

    team = Team(Name=data["Name"], Score=data.get("Score", 0))
    team.Users.append(user)
    team.Characters = characters

    db.session.add(team)
    db.session.commit()

    return jsonify(team.to_dict()), 201

#delete team
@api_bp.route("/users/<int:user_id>/teams/<int:team_id>", methods=["DELETE"])
def delete_team(user_id, team_id):
    user = User.query.get_or_404(user_id)
    team = Team.query.get_or_404(team_id)

    if user not in team.Users:
        return {"message": "Forbidden"}, 403

    db.session.delete(team)
    db.session.commit()
    return "", 204


#Score teamu
@api_bp.route("/users/<int:user_id>/teams/<int:team_id>/dps_score", methods=["GET"])
def team_support_for_dps(user_id, team_id):
    dps_name = request.args.get("dps_name")
    if not dps_name:
        return {"message": "Missing dps_name parameter"}, 400

    user = User.query.get_or_404(user_id)
    team = Team.query.get_or_404(team_id)

    if user not in team.Users:
        return {"message": "Forbidden"}, 403

    dps = Character.query.filter_by(Name=dps_name).first()
    if not dps:
        return {"message": "DPS not found"}, 404

    if dps.Role != "DPS":
        return {"message": "Character is not a DPS"}, 400

    dps_needs = {n.Require for n in dps.Needs}
    matched = set()
    total = 0

    for char in team.Characters:
        if char == dps:
            continue
        for skill in char.Skills:
            for effect in skill.Effects:
                for need in dps_needs:
                    if effect.Name.startswith(need):
                        matched.add(need)
                        total += effect.Value or 0

    return {
        "team_id": team.id,
        "score": total,
        "matched_needs": len(matched),
        "total_needs": len(dps_needs)
    }, 200


#               HTTP codes:
#   200 OK	            poprawny GET / PUT
#   201 Created	        poprawny POST (utworzono zasób)
#   204 No Content 	    poprawny DELETE (opcjonalnie)
#   400 Bad Request	    b³êdne dane wejœciowe (brak pola, z³y typ, z³a logika)
#   401 Unauthorized	brak / b³êdne dane logowania
#   403 Forbidden	    u¿ytkownik istnieje, ale nie ma prawa
#   404 Not Found	    zasób nie istnieje
#   409 Conflict	    konflikt danych (duplikat, UNIQUE)

