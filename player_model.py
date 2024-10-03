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
    club: Mapped[str] = mapped_column()
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

