from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista temporal en memoria para almacenar los pozos
lista_pozos = []

@app.route('/')
def inicio():
# Le pasamos la lista de pozos a la plantilla HTML

 return render_template('index.html', pozos=lista_pozos)

@app.route('/crear-pozo', methods=['POST'])
def crear_pozo():
    # Capturamos los datos enviados desde el formulario

    nombre = request.form['nombre']
    capacidad = request.form['capacidad']
    especie = request.form['especie']

    # Creamos un diccionario con la información del pozo

    nuevo_pozo = {
        'nombre': nombre,
        'capacidad': capacidad,
        'especie': especie
    }
    # Agregamos el nuevo pozo a nuestra lista
    lista_pozos.append(nuevo_pozo)

# Redirigimos a la página principal para ver el resultado

    return redirect(url_for('inicio'))

if __name__ == '__main__':

 app.run(debug=True)