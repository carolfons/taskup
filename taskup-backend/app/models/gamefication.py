from app.extensions import db
from datetime import datetime


class Gamefication(db.Model):
    """Gamefication model representing a gamefication entity."""
    __tablename__ = "gamefication"
    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=1)
    task_completed = db.Column(db.Integer, default=0)
    last_update = db.Column(db.DateTime, default=datetime.utcnow)