from flask import Blueprint, render_template, request,url_for, redirect
from flask_login import login_required, current_user
import folium

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/primer_mapa', methods=['GET', 'POST'])
@login_required
def primer_mapa():
    if request.method == 'POST':
        # hacer cosas cuando se envía el formulario
        # Si el usuario actua sobre el botón se redirige la página
        # la redirección puede ser a la misma ruta o a otro lugar
        return redirect(url_for('main.profile'))

    # mostrar el formulario, no fue enviado
    #Mientras el usuario no hace nada, es decir si no pulsa el botón
    #se muestra la página con el formulario/botón
    start_coords = (40.965, -5.664)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    folium_map.save('proyecto/templates/map.html')
    return render_template('mapa_web.html', nombre="Mapa de la ciudad de Salamanca")
