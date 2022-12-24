from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('base.html', korisnik=current_user)

@views.route('/youtube')
@login_required
def youtube():
    return render_template('youtube.html')

@views.route('/home')
@login_required
def pocetna():
    return render_template('home.html', korisnik=current_user)

@views.route('/mpismo')
@login_required
def mpismo():
    return render_template('mpismo.html', korisnik=current_user)

@views.route('/cv')
@login_required
def cv():
    return render_template('cv.html', korisnik=current_user)