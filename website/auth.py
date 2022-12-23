from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        lozinka = request.form.get('lozinka')
        korisnik = User.query.filter_by(email=email).first()
        if korisnik:
            if check_password_hash(korisnik.lozinka, lozinka):
                flash('Prijava uspješna!', category='success')
                login_user(korisnik, remember=True)
                return redirect(url_for('views.pocetna'))
            else:
                flash('Pogrešna lozinka.', category='error')
        else:
            flash('Email adresa ne postoji.', category='error')

    return render_template('login.html', korisnik=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        ime = request.form.get('ime')
        prezime = request.form.get('prezime')
        email = request.form.get('email')
        lozinka1 = request.form.get('lozinka1')
        lozinka2 = request.form.get('lozinka2')

        korisnik = User.query.filter_by(email=email).first()
        if korisnik:
            flash('Email adresa već postoji!', category='error')
        elif len(ime) < 2:
            flash('Ime mora sadržavati više od 1 slova.', category='error')
        elif len(prezime) < 2:
            flash('Prezime mora sadržavati više od 1 slova.', category = 'error')
        elif len(email) < 4:
            flash('Email adresa mora sadržavati više od 3 slova.', category='error')
        elif lozinka1 != lozinka2:
            flash('Ponovljena lozinka mora biti identična kao unešena lozinka.', category = 'error')
        elif len(lozinka1) < 6:
            flash('Lozinka mora sadržavati više od 5 znakova.', category = 'error')
        else:
            novi_korisnik=User(ime=ime, prezime=prezime, email=email, lozinka=generate_password_hash(lozinka1, method='sha256'))
            db.session.add(novi_korisnik)
            db.session.commit()
            login_user(novi_korisnik, remember=True)
            flash('Profil uspješno kreiran.', category = 'success')
            return redirect(url_for('auth.login'))


    return render_template('register.html', korisnik=current_user)