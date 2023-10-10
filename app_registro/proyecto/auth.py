from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
	return render_template('login.html')

@auth.route('/signup',methods=['POST'])
	
def signup():
	return render_template('signup.html')
	
def signup_post():
	email = request.form.get('email')
	name = request.form.get('name')
	password = request.form.get('password')
	# comprobamos si el e-mail ya existe en la bd
	user = User.query.filter_by(email=email).first() 
	if user:
		flash('La dirección de correo ya existe')
		return redirect(url_for('auth.signup'))
# crear un nuevo usuario con los datos del formulario.
# Hash de la contraseña
	new_user = User(email=email, name=name,
			password=generate_password_hash(password, method='sha256'))
# Se añade el nuevo usuario a la base de datos
	db.session.add(new_user)
	db.session.commit()
	return redirect(url_for('auth.login'))




@auth.route('/logout')
def logout():
	return 'Logout'
