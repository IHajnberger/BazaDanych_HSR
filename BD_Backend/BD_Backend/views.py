# warstwa kontaktowa z aplikacja - interfejs
from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
from models.Character import Character
from models.Team import Team

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

#add char
@api_bp.route("/characters", methods=["POST"])
def create_character():
    data = request.json

    # walidacja adminowa
    #if not current_user.is_admin:
    #   return {"message": "Forbidden"}, 403


    if Character.query.filter_by(Name=data["Name"]).first():
        return {"message": "Character already exists"}, 400

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

    user = User(Username=data["username"])
    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    return {"id": user.id, "username": user.Username}, 201

#login
@api_bp.route("/login", methods=["POST"])
def login():
    data = request.json or {}

    user = User.query.filter_by(Username=data["username"]).first()
    if not user or not user.check_password(data["password"]):
        return {"message": "Invalid credentials"}, 401

    return {"message": "Login successful", "user_id": user.id}


# return list of chars with owned being highlited (pozniej przy frontendzie)
@api_bp.route("/users/<int:user_id>/characters", methods=["GET"])
def get_user_characters(user_id):
    user = User.query.get_or_404(user_id)

    characters = user.Characters 
    return jsonify([c.to_dict() for c in characters])


@api_bp.route("/users/<int:user_id>/characters", methods=["POST"])
def add_character_to_user(user_id):
    # 1) pobierz usera (404 jesli nie ma)
    user = User.query.get_or_404(user_id)

    # 2) pobierz JSON i waliduj
    data = request.get_json(silent=True)
    if not data:
        return {"message": "Invalid or missing JSON body. Set Content-Type: application/json."}, 400

    # akceptujemy "Name" lub "name"
    char_name = data.get("Name") or data.get("name")
    if not char_name:
        return {"message": "Missing 'Name' in JSON body."}, 400

    # 3) znajdz character  jezeli nie ma, zwroc 404
    character = Character.query.filter_by(Name=char_name).first()
    if not character:
        return {"message": f"Character '{char_name}' not found."}, 404

    # 4) sprawdz czy juz przypisany
    # czy user.Characters jest listowalny
    try:
        already = character in user.Characters
    except Exception:
        # dodatkowa ochrona: pobieramy relacje na nowo z DB
        db.session.refresh(user)
        already = character in user.Characters

    if already:
        return {"message": "Character already assigned to user"}, 400

    # 5) przypisz i zapisz
    user.Characters.append(character)
    db.session.commit()

    return {"message": f"Character {character.Name} added to user {user.Username}"}, 201


#add team
@api_bp.route("/users/<int:user_id>/teams", methods=["POST"])
def create_team(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json or {}

    team_name = data.get("Name")
    team_score = data.get("Score", 0)  
    character_names = data.get("characters", [])

    # Walidacja liczby postaci
    if not (1 <= len(character_names) <= 4):
        return {"message": "Team must have between 1 and 4 characters"}, 400

    # Pobranie postaci uzytkownika
    characters = []
    for name in character_names:
        char = Character.query.filter_by(Name=name).first()
        if not char or char not in user.Characters:
            return {"message": f"Character {name} not assigned to user"}, 400
        characters.append(char)

    # Utworzenie druzyny
    team = Team(Name=team_name, Score=team_score)
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
    return {"message": f"Team {team.Name} deleted"}


#view teams
@api_bp.route("/users/<int:user_id>/teams", methods=["GET"])
def get_user_teams(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify([t.to_dict() for t in user.Teams])


#Score teamu
@api_bp.route("/users/<int:user_id>/teams/<int:team_id>/dps_score", methods=["GET"])
def team_support_for_dps(user_id, team_id):
    dps_name = request.args.get("dps_name")
    if not dps_name:
        return {"message": "Missing query parameter: dps_name"}, 400

    user = User.query.get_or_404(user_id)
    team = Team.query.get_or_404(team_id)

    if user not in team.Users:
        return {"message": "Forbidden"}, 403

    dps = Character.query.filter_by(Name=dps_name).first_or_404()
    if dps.Role != "DPS":
        return {"message": "Specified character is not a DPS"}, 400

    dps_need_ids = [n.id for n in dps.Needs]
    total_needs = len(dps_need_ids)

    total_percent_sum = 0
    matched_need_ids = set()

    for char in team.Characters:
        if char.Name == dps.Name:
            continue

        for skill in getattr(char, "Skills", []) or []:
            for effect in getattr(skill, "Effects", []) or []:
                if effect.id in dps_need_ids:
                    matched_need_ids.add(effect.id)
                    total_percent_sum += (effect.Value or 0)

    return jsonify({
        "team_id": team.id,
        "total_percent_sum": total_percent_sum,
        "matched_needs_count": len(matched_need_ids),
        "total_needs": total_needs
    })



