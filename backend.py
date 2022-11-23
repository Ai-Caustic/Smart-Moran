import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://Victor:Caustic69@localhost:5000/SM" + \
    os.path.join(basedir, 'database.db')


db = SQLAlchemy(app)


@app.route('/')
def hello():
    return '<h1>Hello, World<h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
