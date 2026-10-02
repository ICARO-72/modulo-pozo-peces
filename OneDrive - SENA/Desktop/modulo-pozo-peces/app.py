from flask import Flask, render_template
#crear la ap[licacion web con flask
app = Flask(__name__)

# Definir la ruta principal (la pagina de inicio)

@app.route('/')
def inicio():
# Esta funcion carga y muestra el archivo HTML

 return render_template('index.html')
# Punto de entrada para ejecutar la aplicacion  

if __name__ == '__main__':
# debug=True permite que el servidor se actualice solo al hacer cambios

 app.run(debug=True)