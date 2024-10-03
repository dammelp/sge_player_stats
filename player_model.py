from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

from data_sge import players_data

data = players_data

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

with app.app_context():
    db.drop_all()
    db.create_all()

with app.app_context():
    for player in players_data:
        new_player = Player(name=player["Spieler"],position=player["Pos"], age=player["Alt"])
        db.session.add(new_player)
        db.session.commit()
