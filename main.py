import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

from data_sge import players_data
data = players_data

app = Flask(__name__)









if __name__ == "__main__":
    app.run(debug=True)