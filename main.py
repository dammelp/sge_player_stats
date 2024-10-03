from flask import jsonify, request
from app import app
from player_model import Player, db


@app.route("/players", methods=["GET"])
def retrieve_all_player():
    result = db.session.execute(db.select(Player))
    all_players = result.scalars().all()
    all_players_serialized = [player.to_dict() for player in all_players]
    return jsonify(all_players_serialized)


if __name__ == "__main__":
    app.run(debug=True)
