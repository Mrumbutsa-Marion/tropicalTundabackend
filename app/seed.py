from models import db, Fruit, Power, FruitPower
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
        {"image_url": "https://i.pinimg.com/564x/3f/a2/87/3fa287c717ff7a7102e6d872c68b5bda.jpg", "name": "Apple", "super_name": "Vitamin A Bomb", "description": "A juicy fruit with lots of Vitamin A", "price": 1.99, "quantity": 10, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"image_url": "https://i.pinimg.com/736x/e4/d1/17/e4d1176012dd9edaaa82ca4421fd3ba7.jpg", "name": "Orange", "super_name": "Citrus Savior", "description": "A tangy fruit packed with Vitamin C", "price": 0.99, "quantity": 15, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"image_url": "https://i.pinimg.com/564x/1c/16/62/1c1662f546cc85a1d77732c840ff9113.jpg", "name": "Banana", "super_name": "Energy Booster", "description": "A potassium-rich fruit that provides instant energy", "price": 0.5, "quantity": 20, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"image_url": "https://i.pinimg.com/736x/9f/65/ff/9f65ffbfa37d15847f626232c1ccada7.jpg", "name": "Berries", "super_name": "Antioxidant King", "description": "A mix of strawberries, blueberries, and raspberries", "price": 3.99, "quantity": 8, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"image_url": "https://i.pinimg.com/564x/39/6c/da/396cda9caf47f997e995892e42530544.jpg", "name": "Kiwi", "super_name": "Vitamin C Wonder", "description": "A fuzzy fruit loaded with Vitamin C", "price": 1.49, "quantity": 12, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"image_url": "https://i.pinimg.com/564x/d2/dd/5b/d2dd5b8ca52b3c782022fd88a2bce9c8.jpg", "name": "Pineapple", "super_name": "Digestive Hero", "description": "A tropical fruit known for its digestive properties", "price": 2.99, "quantity": 5, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"image_url": "https://i.pinimg.com/564x/3c/54/22/3c54220360d3cbe3039fbad7ba8e48d1.jpg", "name": "Grapes", "super_name": "Fiber Defender", "description": "Small juicy fruits packed with fiber", "price": 1.79, "quantity": 18, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"image_url": "https://i.pinimg.com/564x/05/65/d8/0565d85c2f78f23f75b7267dfa51ccb7.jpg", "name": "Mango", "super_name": "Vitamin E Delight", "description": "A sweet and juicy fruit loaded with Vitamin E", "price": 2.49, "quantity": 7, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"image_url": "https://i.pinimg.com/564x/db/e7/3a/dbe73a5d07a5123e5a662fc5abd49124.jpg", "name": "Papaya", "super_name": "Vitamin Rich Wonder", "description": "A tropical fruit packed with various vitamins", "price": 2.29, "quantity": 9, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
        {"image_url": "https://i.pinimg.com/564x/2c/8e/54/2c8e54fbdd8500df649fd706215bcb86.jpg", "name": "Watermelon", "super_name": "Hydration Guardian", "description": "A refreshing fruit that keeps you hydrated", "price": 4.99, "quantity": 3, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()}
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

    db.session.commit()

    print("🍏 Done seeding!")