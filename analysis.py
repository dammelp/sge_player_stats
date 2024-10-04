import pandas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from app import app, db
from player_model import Player

with app.app_context():
    players = Player.query.all()

data = [player.to_dict() for player in players]

df = pd.DataFrame(data)

print(df.head(3))
