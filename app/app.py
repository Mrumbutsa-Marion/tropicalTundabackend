from flask import Flask, request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from models import db, User, Product
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tunda.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key
migrate = Migrate(app, db)
db.init_app(app)

# Define a WTForms class for user signup
class SignupForm(FlaskForm):
    user_name = StringField('user_name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

# Define a WTForms class for user login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

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

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = []

    for product in products:
        product_list.append({
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'quantity': product.quantity,
            'image': product.image
        })

    return jsonify(product_list)

app.register_blueprint(products_bp)

if __name__ == '__main__':
    app.run()