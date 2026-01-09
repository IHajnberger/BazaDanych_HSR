# warstwa kontaktowa z API - interfejs - moje piekło nr.1
from flask import Blueprint, request, jsonify, render_template
from extensions import db
from models.user import User
from models.Character import Character
from models.Team import Team
from sqlalchemy.orm import joinedload

api_bp = Blueprint("api", __name__)

# ====================================
#             Character
# ====================================

@api_bp.route("/characters", methods=["GET"])
def get_all_characters():
    characters = (
        Character.query
        .options(joinedload(Character.Skills))
        .all()
    )
    return jsonify([c.to_dict() for c in characters])

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

#pobranie info o userze
@api_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return {
        "id": user.id,
        "username": user.Username
    }, 200

# ====================================
#          User-Character
# ====================================

@api_bp.route("/users/<int:user_id>/characters", methods=["GET"])
def get_user_characters(user_id):
    user = (
        User.query
        .options(
            joinedload(User.Characters)
            .joinedload(Character.Skills)
        )
        .get_or_404(user_id)
    )

    search = request.args.get("search", "").lower()
    path = request.args.get("path")
    role = request.args.get("role")
    element = request.args.get("element")

    characters = user.Characters  

    # search po nazwie
    if search:
        characters = [
            c for c in characters
            if search in c.Name.lower()
        ]

    # filtry
    if path:
        characters = [c for c in characters if c.Path == path]

    if role:
        characters = [c for c in characters if c.Role == role]

    if element:
        characters = [c for c in characters if c.Element == element]

    return jsonify([c.to_dict() for c in characters])


@api_bp.route("/users/<int:user_id>/characters", methods=["POST"])
def add_character_to_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    character = Character.query.filter_by(Name=data["Name"]).first_or_404()
    user.Characters.append(character)
    db.session.commit()

    return {"message": "Added"}, 201


@api_bp.route("/users/<int:user_id>/characters/<string:name>", methods=["DELETE"])
def remove_character_from_user(user_id, name):
    user = User.query.get_or_404(user_id)
    character = Character.query.filter_by(Name=name).first_or_404()

    user.Characters.remove(character)
    db.session.commit()

    return {"message": "Removed"}, 204

# ====================================
#            User-Team
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

#get 1 - edit team 
@api_bp.route("/users/<int:user_id>/teams/<int:team_id>", methods=["GET"])
def get_team(user_id, team_id):
    user = User.query.get_or_404(user_id)
    team = Team.query.get_or_404(team_id)

    if user not in team.Users:
        return {"message": "Forbidden"}, 403

    return jsonify(team.to_dict()), 200

#Update team
@api_bp.route("/users/<int:user_id>/teams/<int:team_id>", methods=["PUT"])
def update_team(user_id, team_id):
    user = User.query.get_or_404(user_id)
    team = Team.query.get_or_404(team_id)

    if user not in team.Users:
        return {"message": "Forbidden"}, 403

    data = request.get_json(silent=True)
    if not data:
        return {"message": "No data"}, 400

    # name
    if "Name" in data:
        team.Name = data["Name"]

    # characters
    if "characters" in data:
        if len(data["characters"]) != 4:
            return {"message": "Team must have 4 characters"}, 400

        characters = []
        for name in data["characters"]:
            char = Character.query.filter_by(Name=name).first()
            if not char or char not in user.Characters:
                return {"message": f"Invalid character {name}"}, 400
            characters.append(char)

        team.Characters = characters

    db.session.commit()
    return jsonify(team.to_dict()), 200


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

# Dopasowanie postaci pod DPSa
@api_bp.route("/users/<int:user_id>/dps/<string:dps_name>/candidates", methods=["GET"])
def suggest_characters_for_dps(user_id, dps_name):
    user = User.query.get_or_404(user_id)

    dps = Character.query.filter_by(Name=dps_name).first_or_404()
    if dps.Role != "DPS":
        return {"message": "Character is not a DPS"}, 400

    dps_needs = {n.Require for n in dps.Needs}

    results = []

    for char in user.Characters:
        if char.Name == dps.Name:
            continue
        if char.Role not in ("Support", "Sustain"):
            continue

        matched = set()
        total = 0

        for skill in char.Skills:
            for effect in skill.Effects:
                for need in dps_needs:
                    if effect.Name.startswith(need):
                        matched.add(need)
                        total += effect.Value or 0

        results.append({
            "Name": char.Name,
            "Role": char.Role,
            "score": total,
            "matched_needs": len(matched)
        })

    # sortujemy malejąco po score
    results.sort(key=lambda x: x["score"], reverse=True)

    return jsonify(results), 200

'''
               HTTP codes:
   200 OK	              poprawny GET / PUT
   201 Created	          poprawny POST (utworzono zasób)
   204 No Content 	      poprawny DELETE (opcjonalnie)
   400 Bad Request	      błędne dane wejściowe (brak pola, zły typ, zła logika)
   401 Unauthorized       brak / błędne dane logowania
   403 Forbidden	      użytkownik istnieje, ale nie ma prawa
   404 Not Found	      zasób nie istnieje
   409 Conflict	          konflikt danych (duplikat, UNIQUE)

'''
