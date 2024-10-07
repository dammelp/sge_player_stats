import json
from flask import jsonify, request
from app import app
from player_model import Player, db


# Get all players
@app.route("/players", methods=["GET"])
def retrieve_all_player():
    result = db.session.execute(db.select(Player))
    all_players = result.scalars().all()
    all_players_serialized = [player.to_dict() for player in all_players]
    return jsonify(all_players_serialized)

# Get player by ID
@app.route("/players/<int:id>", methods=["GET"])
def retrieve_player_by_id(id):
    player = Player.query.get(id)
    if player == None:
        return jsonify({'error': 'no player with this id'})
    player_serialized = player.to_dict()
    return jsonify(player_serialized)

# Add a new player
@app.route("/players", methods=["POST"])
def add_player():
    data = request.get_json()
    print(data)

    if not data:
        return jsonify({'error': 'Invalid or missing JSON'}), 400

    required_fields = ['name']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'error': f'Missing required field: {field}'}), 400

    name = data['name']
    club = data.get('club', None)
    position = data.get("position", None)
    print(f"Club: {position}")
    age = data.get('age', None)
    matches_played = data.get('matches_played', None)
    starting_11 = data.get('starting_11', None)
    minutes = data.get('minutes', None)
    goals = data.get('goals', None)
    assists = data.get('assists', None)
    goal_contributions = data.get('goal_contributions', None)
    yellow_cards = data.get('yellow_cards', None)
    red_cards = data.get('red_cards', None)
    xG = data.get('xG', None)
    non_penalty_xG = data.get('non_penalty_xG', None)
    xA = data.get('xA', None)
    x_goal_nonpen_contributions = data.get('x_goal_nonpen_contributions', None)
    progressive_carries = data.get('progressive_carries', None)
    progressive_passes = data.get('progressive_passes', None)
    progressive_passes_received = data.get('progressive_passes_received', None)

    new_player = Player(
        club=club,
        name=name,
        position=position,
        age=age,
        matches_played=matches_played,
        starting_11=starting_11,
        minutes=minutes,
        goals=goals,
        assists=assists,
        goal_contributions=goal_contributions,
        yellow_cards=yellow_cards,
        red_cards=red_cards,
        xG=xG,
        non_penalty_xG=non_penalty_xG,
        xA=xA,
        x_goal_nonpen_contributions=x_goal_nonpen_contributions,
        progressive_carries=progressive_carries,
        progressive_passes=progressive_passes,
        progressive_passes_received=progressive_passes_received
    )

    db.session.add(new_player)
    db.session.commit()

    return jsonify(new_player.serialize())

# Update player
@app.route("/players/<id>", methods=["PUT"])
def update_player(id):
    player = Player.query.get(id)

    if not player:
        return jsonify({'error': 'Player not found'}), 404

    data = request.get_json()

    if 'name' in data:
        player.name = data['name']
    if 'club' in data:
        player.club = data['club']
    if 'age' in data:
        player.age = data['age']
    if 'matches_played' in data:
        player.matches_played = data['matches_played']
    if 'starting_11' in data:
        player.starting_11 = data['starting_11']
    if 'minutes' in data:
        player.minutes = data['minutes']
    if 'goals' in data:
        player.goals = data['goals']
    if 'assists' in data:
        player.assists = data['assists']
    if 'goal_contributions' in data:
        player.goal_contributions = data['goal_contributions']
    if 'yellow_cards' in data:
        player.yellow_cards = data['yellow_cards']
    if 'red_cards' in data:
        player.red_cards = data['red_cards']
    if 'xG' in data:
        player.xG = data['xG']
    if 'non_penalty_xG' in data:
        player.non_penalty_xG = data['non_penalty_xG']
    if 'xA' in data:
        player.xA = data['xA']
    if 'x_goal_nonpen_contributions' in data:
        player.x_goal_nonpen_contributions = data['x_goal_nonpen_contributions']
    if 'progressive_carries' in data:
        player.progressive_carries = data['progressive_carries']
    if 'progressive_passes' in data:
        player.progressive_passes = data['progressive_passes']
    if 'progressive_passes_received' in data:
        player.progressive_passes_received = data['progressive_passes_received']
        # Get JSON data from the request

    return jsonify(player.serialize())

# Delete player
@app.route("/players/<id>", methods=["DELETE"])
def delete_player(id):
    player = Player.query.get(id)

    if player:
        db.session.delete(player)
        db.session.commit()
    else:
        return jsonify({"Error": "No player found."})

    db.session.delete(player)
    db.session.commit()

    return jsonify({"Success": "Player removed from database."})




if __name__ == "__main__":
    app.run(debug=True)
