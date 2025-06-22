from server.models import db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from werkzeug.security import generate_password_hash
from server.app import app

with app.app_context():
    print("Seeding database...")

    
    db.drop_all()
    db.create_all()

    
    user1 = User(username="admin")
    user1.password_hash = generate_password_hash("password123")

    user2 = User(username="jane_doe")
    user2.password_hash = generate_password_hash("securepass")

    db.session.add_all([user1, user2])
    db.session.commit()

    
    guest1 = Guest(name="Keanu Reeves", occupation="Actor")
    guest2 = Guest(name="Michelle Obama", occupation="Author")
    guest3 = Guest(name="Elon Musk", occupation="Entrepreneur")

    db.session.add_all([guest1, guest2, guest3])
    db.session.commit()

    
    episode1 = Episode(date="2024-06-01", number=1)
    episode2 = Episode(date="2024-06-02", number=2)

    db.session.add_all([episode1, episode2])
    db.session.commit()

    
    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode1.id)
    appearance3 = Appearance(rating=3, guest_id=guest3.id, episode_id=episode2.id)

    db.session.add_all([appearance1, appearance2, appearance3])
    db.session.commit()

    print("Done seeding!")
