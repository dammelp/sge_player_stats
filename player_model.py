from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Player(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    club: Mapped[str] = mapped_column(nullable=True)
    position: Mapped[str] = mapped_column(nullable=True)
    age: Mapped[str] = mapped_column(nullable=True)
    matches_played: Mapped[int] = mapped_column(nullable=True)
    starting_11: Mapped[int] = mapped_column(nullable=True)
    minutes: Mapped[int] = mapped_column(nullable=True)
    goals: Mapped[int] = mapped_column(nullable=True)
    assists: Mapped[int] = mapped_column(nullable=True)
    goal_contributions: Mapped[int] = mapped_column(nullable=True)
    yellow_cards: Mapped[int] = mapped_column(nullable=True)
    red_cards: Mapped[int] = mapped_column(nullable=True)
    xG: Mapped[float] = mapped_column(nullable=True)
    non_penalty_xG: Mapped[float] = mapped_column(nullable=True)
    xA: Mapped[float] = mapped_column(nullable=True)
    x_goal_nonpen_contributions: Mapped[float] = mapped_column(nullable=True)
    progressive_carries: Mapped[float] = mapped_column(nullable=True)
    progressive_passes: Mapped[float] = mapped_column(nullable=True)
    progressive_passes_received: Mapped[float] = mapped_column(nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self,column.name)
        return dictionary

    def serialize(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}