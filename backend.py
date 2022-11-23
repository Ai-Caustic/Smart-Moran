import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Caustic69@localhost:5432/SM"
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = True

#os.path.join(basedir, 'database.db')


db = SQLAlchemy(app)


class Customers(db.Model):
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


# routes


@ app.route('/')
def index():
    try:
        users = User.query.order_by(User.userId).all()
        user_text = '<ul>'
        for user in users:
            user_text += '<li>' + user.firstName + '-' + user.secondName + '</li>'
            user_text += '</ul>'
            return user_text
    except Exception as e:
        # e holds a description of the error
        error_text = '<p> The error: <br>' + str(e) + '</p>'
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
