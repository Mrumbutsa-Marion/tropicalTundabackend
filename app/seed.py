from models import db, User, Order, Donation

# Create a few sample users
user1 = User(username='user1', email='user1@example.com')
user2 = User(username='user2', email='user2@example.com')

# Add users to the session
db.session.add_all([user1, user2])
db.session.commit()

# Create sample orders for users
order1 = Order(user_id=user1.id, total_amount=50.0)
order2 = Order(user_id=user2.id, total_amount=30.0)

# Add orders to the session
db.session.add_all([order1, order2])
db.session.commit()

# Create sample donations for users
donation1 = Donation(user_id=user1.id, amount=20.0)
donation2 = Donation(user_id=user2.id, amount=10.0)

# Add donations to the session
db.session.add_all([donation1, donation2])
db.session.commit()

print("Sample data added to the database.")
