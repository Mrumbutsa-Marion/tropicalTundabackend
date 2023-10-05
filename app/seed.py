from flask import Flask
from models import db, Product

app = Flask(__name__)
# Initialize the Flask SQLAlchemy extension
db.init_app(app)

def seed_products():
    with app.app_context():
        # Create instances of Product and add them to the session
        product1 = Product(name='Pomegranate', description='Sweet fruit with a rich red color', price=10.99, quantity=5, image='https://cdn.pixabay.com/photo/2018/05/08/20/19/pomegranate-3383814_1280.jpg')
        db.session.add(product1)
        db.session.commit()

if __name__ == '__main__':
    # Call the seed_products function
    seed_products()