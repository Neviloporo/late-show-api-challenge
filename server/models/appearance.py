from server.models import db 
from sqlalchemy.orm import validates

class Appearance(db.Models):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey("guests.id"), nullable=False)
    episode_id =db.Column(db.Integer, db.ForeignKey("episode.id"), nullable=False)

    @validates
    def validate_rating(self, key, rating):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        return rating