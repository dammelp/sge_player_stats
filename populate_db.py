from app import app
from player_model import Player, db
from data_sge import players_data

data = players_data
# Convert the age to a float
for player in players_data:
    player['club'] = 'Eintracht Frankfurt'

for year in players_data:
    year["Alt"] = round(float(year["Alt"].split("-")[0]) + float((year["Alt"].split("-")[1])) / 365.25, 2)


# Replace the commas of decimal numbers with dots
def clean_decimal(value):
    if isinstance(value, str):
        value = value.replace(',', '.')
    try:
        return float(value)
    except ValueError:
        # Handle the case where value cannot be converted
        return None  # or raise an exception/log an error


with app.app_context():
    db.drop_all()
    db.create_all()

with app.app_context():
    for player in players_data:
        new_player = Player(name=player["Spieler"],
                            club=player["club"],
                            position=player["Pos"],
                            age=float(player["Alt"]),
                            matches_played=int(player["GS"]),
                            starting_11=int(player["Startelf"]),
                            minutes=int(player["Min."]),
                            goals=int(player["Tor"]),
                            assists=int(player["Vor"]),
                            goal_contributions=int(player["T+V"]),
                            yellow_cards=int(player["Gelb"]),
                            red_cards=int(player["Rot"]),
                            xG=float(player["xG"]),
                            non_penalty_xG=float(player["npxG"]),
                            xA=float(player["xAG"]),
                            x_goal_nonpen_contributions=clean_decimal(player["npxG+xAG"]),
                            progressive_carries=float(player["PrgC"]),
                            progressive_passes=float(player["PrgP"]),
                            progressive_passes_received=float(player["PrgR"])
                            )
        db.session.add(new_player)
        db.session.commit()