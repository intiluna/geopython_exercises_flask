from flask import Flask, render_template, request

app = Flask(__name__)

datos_formulario = {}

@app.route('/', methods=['GET', 'POST'])
def formulario():
	if request.method == 'POST':
		nombre = request.form['nombre']
		apellidos = request.form['apellidos']
		ciudad = request.form['ciudad']
		
		# Guardar los datos en el diccionario
		datos_formulario['nombre'] = nombre
		datos_formulario['apellidos'] = apellidos
		datos_formulario['ciudad'] = ciudad
		
		return 'Formulario enviado con éxito.'

	return render_template('formulario.html')

@app.route('/datos')
def ver_datos():
	return render_template('datos.html', datos=datos_formulario)

if __name__ == '__main__':
	app.run(debug=True)
