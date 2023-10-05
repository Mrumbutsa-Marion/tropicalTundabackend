from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from models import db, User, Order, Donation, Payment, Fruit
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import secrets

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://marion:rq2bTOIw6EUXc0P6kMOYm4lmTQVMsCMy@dpg-ckf3n00l3its738m4ov0-a.ohio-postgres.render.com/tunda_app'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    migrate = Migrate(app, db)

    CORS(app)

    secret_key = secrets.token_hex(16)
    app.config['SECRET_KEY'] = secret_key

    return app

app = create_app()

# Define a WTForms class for user signup
class SignupForm(FlaskForm):
    user_name = StringField('user_name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

# Define a WTForms class for user login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

@app.route('/')
def home():
    return "Welcome to my app"

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json

    user_name = data.get('user_name')
    email = data.get('email')
    password = data.get('password')

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'User with this email already exists'}), 409

    hashed_password = generate_password_hash(password)

    new_user = User(user_name=user_name, email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json

    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid credentials'}), 401

    return jsonify({'message': 'Login successful'})

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

@app.route('/fruits', methods=['GET'])
def get_fruits():
    fruits = Fruit.query.all()

    fruit_data = [
        {"id": fruit.id, "image_url":fruit.image_url, "name": fruit.name, "super_name": fruit.super_name, "description": fruit.description, "price": fruit.price, "quantity": fruit.quantity}
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
        "image_url": fruit.image_url,
        "description": fruit.description,
        "price": fruit.price,
        "quantity": fruit.quantity
        # Add other relevant fields as needed
    }

    return jsonify(fruit_data)

if __name__ == '__main__':
    app.run(port=5555, debug=True)