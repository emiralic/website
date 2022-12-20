from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        ime = request.form.get('ime')
        prezime = request.form.get('prezime')
        lozinka1 = request.form.get('lozinka1')
        lozinka2 = request.form.get('lozinka2')


        if len(ime) < 2:
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
            flash('Profil uspješno kreiran.', category = 'success')

    return render_template('register.html')