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


class User(db.Model):
    __tablename__ = 'users'
    userId = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, nullable=False)
    secondName = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


# Create a marshmallow schema based on the User model
class CustomerSchema(ma.Schema):
    class Meta:
        fields = ("customerId", "firstName", "lastName",
                  "phoneNo" "email", "notes")
        model = Customer


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)


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
            notes=request.json['notes'],
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


api.add_resource(CustomerListResource, '/customers')
api.add_resource(CustomerResource, '/customers/<int:customerId>')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
