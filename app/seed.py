# Importing necessary modules
from models import db, Fruit, Power, FruitPower, Donation
from random import choice
from app import create_app
from datetime import datetime

# Create the Flask app
app = create_app()

# Use the app context to interact with the database
with app.app_context():
    # Step 1: Check if tables exist, if not, create them
    db.create_all()

    # Step 2: Seeding powers
    print("🍏 Seeding fruits and vitamins...")
    powers_data = [
        {"name": "Vitamin A", "description": "Essential for vision and immune function", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"name": "Vitamin C", "description": "Boosts the immune system and aids in iron absorption", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"name": "Vitamin E", "description": "Acts as an antioxidant and supports skin health", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"name": "Fiber", "description": "Important for digestive health", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()}
    ]

    for data in powers_data:
        power = Power(**data)
        db.session.add(power)

    db.session.commit()

    # Step 3: Seeding fruits
    print("🍏 Seeding fruits...")
    fruits_data = [
        {"name": "Apple", "super_name": "Vitamin A Bomb", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"name": "Orange", "super_name": "Citrus Savior", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"name": "Banana", "super_name": "Energy Booster", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"name": "Berries", "super_name": "Antioxidant King", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"name": "Kiwi", "super_name": "Vitamin C Wonder", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"name": "Pineapple", "super_name": "Digestive Hero", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"name": "Grapes", "super_name": "Fiber Defender", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"name": "Mango", "super_name": "Vitamin E Delight", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"name": "Papaya", "super_name": "Vitamin Rich Wonder", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"name": "Watermelon", "super_name": "Hydration Guardian", "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()}
    ]

    for data in fruits_data:
        fruit = Fruit(**data)
        db.session.add(fruit)

    db.session.commit()

    # Step 4: Adding powers to fruits
    print("🍏 Adding powers to fruits...")

    strengths = ["Strong", "Weak", "Average"]
    fruits = Fruit.query.all()
    powers = Power.query.all()

    for fruit in fruits:
        for _ in range(choice([1, 2, 3])):
            power = choice(powers)
            strength = choice(strengths)
            fruit_power = FruitPower(fruit_id=fruit.id, power_id=power.id, strength=strength, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
            db.session.add(fruit_power)

    # Step 5: Seeding donations
    print("💰 Seeding donations...")
    donations_data = [
        {"donor_name": "John Doe", "amount": 100.00, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"donor_name": "Jane Doe", "amount": 50.00, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        # Add more donation data as needed
    ]

    for data in donations_data:
        donation = Donation(**data)
        db.session.add(donation)

    db.session.commit()

    print("🍏 Done seeding!")
