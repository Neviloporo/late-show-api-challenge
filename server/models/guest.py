from server.models import db

class Guest(db.Models):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String)

    appearance = db.relationship("Appearance", backref="guest", cascade="all, delete")