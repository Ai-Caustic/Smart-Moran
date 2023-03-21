from .extensions import db


# Relationships


customer_product = db.Table('customer_product',
                            db.Column('customer_id', db.Integer, db.ForeignKey(
                                'customer.id'), primary_key=True),
                            db.Column('product_id', db.Integer, db.ForeignKey(
                                'product.id'), primary_key=True)

                            )

# Tables


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.Blob)
    video = db.Column(db.Blob)
    customers = db.relationship('Customer', secondary=customer_product)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True)
