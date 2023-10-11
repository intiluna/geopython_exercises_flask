from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

# iniciamos SQLAlchemy 
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '123456'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    ###################
    # Para crear la tabla en la base de datos
    with app.app_context():
        db.create_all()
    ###################
    @login_manager.user_loader
    def load_user(user_id):
        # Empleamos user_id, que es la clave principal
        # de la tabla usuarios para hacer la consulta
        return User.query.get(int(user_id))

    # Fabrica de rutas para las páginas de autenticación
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Fabrica de rutas para las páginas que no son de autenticación
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app