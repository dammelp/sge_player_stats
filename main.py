import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from app import app
from player_model import Player, db





@app.route("/players", methods=["GET"])
def retrieve_all_player():
    result = db.session.execute(db.select(Player))
    all_players = result.scalars().all()
    return 'hello'






if __name__ == "__main__":
    app.run(debug=True)