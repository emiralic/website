from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
@views.route('home')
def home():
    return render_template('home.html')

@views.route('/youtube')
def youtube():
    return render_template('youtube.html')