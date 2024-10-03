from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

from data_sge import players_data

data = players_data

# Convert the age to a float
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


app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Player(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    position: Mapped[str] = mapped_column()
    age: Mapped[str] = mapped_column()
    matches_played: Mapped[int] = mapped_column()
    starting_11: Mapped[int] = mapped_column()
    minutes: Mapped[int] = mapped_column()
    goals: Mapped[int] = mapped_column()
    assists: Mapped[int] = mapped_column()
    goal_contributions: Mapped[int] = mapped_column()
    yellow_cards: Mapped[int] = mapped_column()
    red_cards: Mapped[int] = mapped_column()
    xG: Mapped[float] = mapped_column()
    non_penalty_xG: Mapped[float] = mapped_column()
    xA: Mapped[float] = mapped_column()
    x_goal_nonpen_contributions: Mapped[float] = mapped_column()
    progressive_carries: Mapped[float] = mapped_column()
    progressive_passes: Mapped[float] = mapped_column()
    progressive_passes_received: Mapped[float] = mapped_column()


with app.app_context():
    db.drop_all()
    db.create_all()

with app.app_context():
    for player in players_data:
        new_player = Player(name=player["Spieler"],
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
