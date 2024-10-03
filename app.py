from flask import Flask
from player_model import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
db.init_app(app)


