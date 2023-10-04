from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey

db = SQLAlchemy()

class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String)
    amount = db.Column(db.Float)
    created_at = db.Column(DateTime, nullable=False, default=lambda: datetime.utcnow())
    updated_at = db.Column(DateTime, nullable=False, default=lambda: datetime.utcnow())

class Donation(db.Model):
    __tablename__ = 'donation'

    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String)
    amount = db.Column(db.Float)
    created_at = db.Column(DateTime, nullable=False, default=lambda: datetime.utcnow())
    updated_at = db.Column(DateTime, nullable=False, default=lambda: datetime.utcnow())

class Payment(db.Model):
    __tablename__ = 'payment'

    id = db.Column(db.Integer, primary_key=True)
    payment_method = db.Column(db.String)
    amount = db.Column(db.Float)
    created_at = db.Column(DateTime, nullable=False, default=lambda: datetime.utcnow())
    updated_at = db.Column(DateTime, nullable=False, default=lambda: datetime.utcnow())

class Fruit(db.Model):
    __tablename__ = 'fruit'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(DateTime, nullable=False, default=lambda: datetime.utcnow())
    updated_at = db.Column(DateTime, nullable=False, default=lambda: datetime.utcnow())

class Power(db.Model):
    __tablename__ = 'power'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(DateTime, nullable=False, default=lambda: datetime.utcnow())
    updated_at = db.Column(DateTime, nullable=False, default=lambda: datetime.utcnow())

class FruitPower(db.Model):
    __tablename__ = 'fruit_power'

    id = db.Column(db.Integer, primary_key=True)
    fruit_id = db.Column(db.Integer, ForeignKey('fruit.id'), nullable=False)
    power_id = db.Column(db.Integer, ForeignKey('power.id'), nullable=False)
    strength = db.Column(db.String)
    created_at = db.Column(DateTime, nullable=False, default=lambda: datetime.utcnow())
    updated_at = db.Column(DateTime, nullable=False, default=lambda: datetime.utcnow())

# Note: You can add more fields to each model as needed, and adjust relationships accordingly.

if __name__ == '__main__':
    # This block is typically used for database creation or migration
    # For example, db.create_all()
    pass
