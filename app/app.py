from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, Order, Donation, Payment, Fruit  # Assuming you have a Fruit model

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app

app = create_app()
migrate = Migrate(app, db)

CORS(app)

@app.route('/')
def home():
    return 'welcome to tropical tunda'

# Retrieve all orders
@app.route('/orders', methods=['GET'])
def get_all_orders():
    orders = Order.query.all()

    order_data = [
        {"id": order.id, "order_number": order.order_number, "amount": order.amount}
        for order in orders
    ]

    return jsonify(order_data)

# Retrieve a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_specific_order(order_id):
    order = Order.query.get(order_id)

    if order is None:
        return jsonify({"error": "Order not found"}), 404

    order_data = {
        "id": order.id,
        "order_number": order.order_number,
        "amount": order.amount,
        # Add other relevant fields as needed
    }

    return jsonify(order_data)

# Retrieve all donations and payments (your existing routes)

# Retrieve all fruits
@app.route('/fruits', methods=['GET'])
def get_fruits():
    fruits = Fruit.query.all()

    fruit_data = [
        {"id": fruit.id, "name": fruit.name, "super_name": fruit.super_name}
        for fruit in fruits
    ]

    return jsonify(fruit_data)

# Retrieve a specific fruit by ID
@app.route('/fruits/<int:fruit_id>', methods=['GET'])
def get_fruit(fruit_id):
    fruit = Fruit.query.get(fruit_id)

    if fruit is None:
        return jsonify({"error": "Fruit not found"}), 404

    fruit_data = {
        "id": fruit.id,
        "name": fruit.name,
        "super_name": fruit.super_name,
        # Add other relevant fields as needed
    }

    return jsonify(fruit_data)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


