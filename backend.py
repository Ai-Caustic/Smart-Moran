import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_restful import Resource, Api
from flask_marshmallow import Marshmallow


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Caustic69@localhost:5432/SM"
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


class Customer(db.Model):
    __tablename__ = 'customers'
    customerId = db.Column(db.Integer, primary_key=True, nullable=False)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    phoneNo = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String)
    notes = db.Column(db.String)


class Product(db.Model):
    __tablename__ = 'products'
    productId = db.Column(db.Integer, primary_key=True, nullable=False)
    productName = db.Column(db.String, nullable=False)
    productDesc = db.Column(db.String, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey(
        'users.userId'), nullable=False)
    productImg = db.Column(db.String)
    productVid = db.Column(db.String)


class User(db.Model):
    __tablename__ = 'users'
    userId = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, nullable=False)
    secondName = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


'''
class CustomerProduct(db.Model):
    __tablename__ = 'customerProducts'
    productId = db.Column(db.Integer, db.ForeignKey(
        'products.productId'), nullable=False)
    CustomerId = db.Column(db.Integer, db.ForeignKey(
        'customers.customerId'), nullable=False)
'''


class Role(db.Model):
    __tablename__ = 'roles'
    roleId = db.Column(db.Integer, primary_key=True)
    roleName = db.Column(db.String, unique=True)

# Create a marshmallow schema based on the model


class CustomerSchema(ma.Schema):
    class Meta:
        fields = ("customerId", "firstName", "lastName",
                  "phoneNo", "email", "notes")
        model = Customer


class ProductSchema(ma.Schema):
    class Meta:
        fields = ("productId", "productName", "productDesc",
                  "userId", "productImg", "productVid")
        model = Product


class UserSchema(ma.Schema):
    class Meta:
        fields = ("userId", "firstName", "secondName", "email", "password")
        model = User


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)


# Create a Restful resource
class CustomerListResource(Resource):
    def get(self):
        customers = Customer.query.all()
        return customers_schema.dump(customers)

    def post(self):
        new_customer = Customer(
            customerId=request.json['customerId'],
            firstName=request.json['firstName'],
            lastName=request.json['lastName'],
            phoneNo=request.json['phoneNo'],
            email=request.json['email'],
            notes=request.json['notes']
        )
        db.session.add(new_customer)
        db.session.commit()
        return customer_schema.dump(new_customer)


class CustomerResource(Resource):
    def get(self, customerId):
        customer = Customer.query.get_or_404(customerId)
        return customer_schema.dump(customer)

    def patch(self, customerId):
        customer = Customer.query.get_or_404(customerId)

        if 'customerId' in request.json:
            customer.customerId = request.json['customerId']
        if 'firstName' in request.json:
            customer.firstName = request.json['firstName']
        if 'lastName' in request.json:
            customer.lastName = request.json['lastName']
        if 'phoneNo' in request.json:
            customer.phoneNo = request.json['phoneNo']
        if 'email' in request.json:
            customer.email = request.json['email']
        if 'notes' in request.json:
            customer.notes = request.json['notes']

        db.session.commit()
        return customer_schema.dump(customer)

    def delete(self, customerId):
        customer = Customer.query.get_or_404(customerId)
        db.session.delete(customer)
        db.session.commit()
        return '', 204


class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return products_schema.dump(products)

    def post(self):
        new_product = Product(
            productId=request.json['productId'],
            productName=request.json['productName'],
            productDesc=request.json['productDesc'],
            userId=request.json['userId'],
            productImg=request.json['productImg'],
            productVid=request.json['productVid']
        )
        db.session.add(new_product)
        db.session.commit()
        return customer_schema.dump(new_product)


class ProductResource(Resource):
    def get(self, productId):
        product = Product.query.get_or_404(productId)
        return product_schema.dump(product)

    def patch(self, productId):
        product = Product.query.get_or_404(productId)

        if 'productId' in request.json:
            product.productId = request.json['productId']
        if 'productName' in request.json:
            product.productName = request.json['productName']
        if 'productDesc' in request.json:
            product.lastName = request.json['productDesc']
        if 'userId' in request.json:
            product.userId = request.json['userId']
        if 'productImg' in request.json:
            product.productImg = request.json['productImg']
        if 'productVid' in request.json:
            product.productVid = request.json['productVid']

        db.session.commit()
        return product_schema.dump(product)

    def delete(self, productId):
        product = Product.query.get_or_404(productId)
        db.session.delete(product)
        db.session.commit()
        return '', 204


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)

    def post(self):
        new_user = User(
            userId=request.json['userId'],
            firstName=request.json['firstName'],
            secondName=request.json['secondName'],
            email=request.json['email'],
            password=request.json['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)


class UserResource(Resource):
    def get(self, userId):
        user = User.query.get_or_404(userId)
        return user_schema.dump(user)

    def patch(self, userId):
        user = User.query.get_or_404(userId)

        if 'UserId' in request.json:
            user.userId = request.json['userId']
        if 'firstName' in request.json:
            user.firstName = request.json['firstName']
        if 'secondName' in request.json:
            user.secondName = request.json['secondName']
        if 'email' in request.json:
            user.email = request.json['email']
        if 'password' in request.json:
            user.password = request.json['password']

        db.session.commit()
        return user_schema.dump(user)

    def delete(self, userId):
        user = User.query.get_or_404(userId)
        db.session.delete(user)
        db.session.commit()
        return '', 204


api.add_resource(CustomerListResource, '/customers')
api.add_resource(CustomerResource, '/customers/<int:customerId>')
api.add_resource(ProductListResource, '/products')
api.add_resource(ProductResource, '/products/<int:productId>')
api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:userId>')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
