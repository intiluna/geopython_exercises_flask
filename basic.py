from flask import Flask
import folium

app = Flask(__name__)

@app.route("/")
def saludo():
    return "<p>Bienvenidos al curso de Flask...primera flask basica de Inti Luna</p>"
    
@app.route("/contacto")
def contacto_respuesta():
    return "<p>Esta es la pagina de contacto...test adicional</p>"

@app.route('/maps')
def index():
	start_coords = (42.9540700, -5.7360300)
	folium_map = folium.Map(location=start_coords, zoom_start=14)
	return folium_map._repr_html_()
	

