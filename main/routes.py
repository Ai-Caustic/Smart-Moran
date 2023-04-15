from flask import Blueprint, render_template, request, url_for, redirect
from ..extensions import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/slideshow.js')
def slideshow():
    render_template('/js/slideshow.js')
