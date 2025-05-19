# --- INSTALACIÓN DE FLASK ---
# Para instalar Flask se usa pip, el instalador de paquetes de Python.
# Escribe en la terminal: 
# pip install flask
# Esto descarga e instala el paquete Flask desde el repositorio de PyPI (Python Package Index).


# Importamos la clase Flask del paquete flask.
from flask import Flask

# Creamos una instancia de la aplicación Flask.
# Esta instancia representará nuestra aplicación web.
app = Flask(__name__)

# Definimos una ruta principal ('/') usando el decorador @app.route
# Cuando alguien accede a http://localhost:5000/, esta función se ejecutará.
@app.route('/')
def inicio():
    # Retornamos una cadena HTML como respuesta.
    return '<h1>Servidor Flask activo</h1>'


# Definimos una ruta dinámica que incluye un parámetro <nombre>.
# Por ejemplo, al acceder a http://localhost:5000/saludo/Ana se mostrará "Hola, Ana!"
@app.route('/saludo/<nombre>')
def saludo(nombre):
    # Usamos f-string para incluir el valor de 'nombre' en el mensaje de saludo.
    return f'<p>Hola, {nombre}!</p>'


# Este bloque garantiza que la app se ejecute solo si el script se ejecuta directamente,
# y no si se importa como un módulo desde otro archivo.
if __name__ == '__main__':
    # Ejecutamos la aplicación Flask en modo debug (útil para desarrollo).
    # El servidor correrá en http://localhost:5000
    app.run(debug=True)
