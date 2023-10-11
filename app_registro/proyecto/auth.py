from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # comprobamos que el usuario actual existe
    # Hay que comparar la constraseña aportada por el usuario con la contraseña guardada en la base de datso
    if not user or not check_password_hash(user.password, password):
        flash('Por favor, compruebe sus datos de inicio de sesión y vuelva a intentarlo.')
        return redirect(url_for('auth.login')) # Si el usuario no existe o la contraseña es incorrecta se vuelve a la página

    # si pasa la verificación anterior, entonces sabemos que el usuario tiene las credenciales correctas
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # comprobamos si el e-mail ya existe en la bd

    if user: # si se encuentra un usuario, hay que redirigirlo a la página de registro para que el usuario pueda volver a intentarlo  
        flash('La dirección de correo ya existe.')
        return redirect(url_for('auth.signup'))

    # crear un nuevo usuario con los datos del formulario.
    # Hash de la contraseña 
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # Se añade el nuevo usuario a la base de datos
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
