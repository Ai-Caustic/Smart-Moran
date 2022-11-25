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
    customerId = db.Column(db.Integer, primary_key=True)
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

    def __repr__(self):
        return '<User %s>' % self.firstName


# Create a marshmallow schema based on the User model
class CustomerSchema(ma.Schema):
    class Meta:
        fields = ("customerId", "firstName", "lastName",
                  "phoneNo" "email", "notes")
        model = Customer


post_schema = CustomerSchema
posts_schema = CustomerSchema(many=True)


# Create a Restful resource
class PostListResource(Resource):
    def get(self):
        customers = Customer.query.all()
        return posts_schema.dump(customers)

    def post(self):
        new_post = Customer(
            customerId=request.json['customerId'],
            firstName=request.json['firstName'],
            lastName=request.json['lastName'],
            phoneNo=request.json['phoneNo'],
            email=request.json['email'],
            notes=request.json['notes'],
        )
        db.session.add(new_post)
        db.session.commit()
        return post_schema.dump(new_post)


class PostResource(Resource):
    def get(self, customer_id):
        customer = Customer.query.get_or_404(customer_id)
        return post_schema.dump(customer)


api.add_resource(PostListResource, '/customers')
api.add_resource(PostResource, '/customers/<int:customer_id>')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
