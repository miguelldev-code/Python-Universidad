# Importamos las clases necesarias del módulo http.server (parte de la biblioteca estándar de Python)
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs 

import json

# -----------------------------------------
# TEORÍA: ¿Qué es un servidor web?
# -----------------------------------------
# Un servidor web es un programa que recibe solicitudes HTTP (desde navegadores u otras apps)
# y responde con contenido (HTML, texto, JSON, etc.).
# En Python, podemos crear un servidor web básico con la clase HTTPServer.

# Creamos una clase manejadora de solicitudes HTTP, heredando de BaseHTTPRequestHandler
class Manejador(BaseHTTPRequestHandler):

    # -----------------------------------------
    # TEORÍA: Método GET
    # -----------------------------------------
    # El método GET se utiliza cuando un cliente (como un navegador) solicita una página o recurso.
    # Por ejemplo, cuando visitas http://localhost:8080 en tu navegador.
    def do_GET(self):
        # Parsear la URL y extraer los parámetros
        url = urlparse(self.path)
        parametros = parse_qs(url.query)
        nombre = parametros.get("nombre", ["visitante"])[0]

        # Preparar la respuesta con el nombre recibido
        respuesta = {
            "mensaje": f"Hola, {nombre}. Esta es una respuesta GET desde Python puro."
        }

        # Enviar respuesta JSON
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(respuesta).encode('utf-8'))

        
    # -----------------------------------------
    # TEORÍA: Método POST
    # -----------------------------------------
    # El método POST se utiliza para enviar datos al servidor (por ejemplo, desde un formulario).
    def do_POST(self):
        longitud = int(self.headers['Content-Length'])
        cuerpo = self.rfile.read(longitud).decode('utf-8')

        tipo_contenido = self.headers.get("Content-Type", "")

        if "application/json" in tipo_contenido:
            try:
                datos = json.loads(cuerpo)
                nombre = datos.get("nombre", "desconocido")
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "JSON inválido"}).encode('utf-8'))
                return
        else:  # Asumimos application/x-www-form-urlencoded
            datos = parse_qs(cuerpo)
            nombre = datos.get("nombre", ["desconocido"])[0]

        respuesta = {
            "mensaje": f"Hola, {nombre}. Tu información fue recibida correctamente."
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(respuesta).encode('utf-8'))


# -----------------------------------------
# TEORÍA: HTTPServer
# -----------------------------------------
# HTTPServer recibe dos argumentos:
# 1. Dirección y puerto donde correrá el servidor.
# 2. Clase que maneja las solicitudes.
servidor = HTTPServer(('localhost', 8081), Manejador)

# Informamos al usuario que el servidor está corriendo
print("Servidor corriendo en http://localhost:8081")

# Mantenemos el servidor escuchando solicitudes indefinidamente
servidor.serve_forever()

# Hacer get
# curl "http://localhost:8081?nombre=Carlos"

# Hacer post
# curl -X POST http://localhost:8081 -d "nombre=Ana"
