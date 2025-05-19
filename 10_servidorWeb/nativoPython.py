# Importamos las clases necesarias del módulo http.server de la biblioteca estándar de Python
from http.server import BaseHTTPRequestHandler, HTTPServer

# Creamos una clase que hereda de BaseHTTPRequestHandler.
# Esta clase se encargará de manejar las solicitudes HTTP que reciba el servidor.
class ManejadorHttp(BaseHTTPRequestHandler):

    # Método que se ejecuta automáticamente cuando el servidor recibe una solicitud GET.
    def do_GET(self):
        # Enviamos el código de estado HTTP 200 (OK) como respuesta al cliente.
        self.send_response(200)
        
        # Indicamos que el contenido de la respuesta será de tipo HTML.
        self.send_header("Content-type", "text/html")
        
        # Indicamos que ya terminamos de enviar las cabeceras de la respuesta.
        self.end_headers()
        
        # Enviamos el contenido (cuerpo de la respuesta) en formato HTML como bytes.
        self.wfile.write(b"<h1>Hola desde Python!</h1>")

# Creamos una instancia del servidor HTTP.
# Escuchará peticiones en localhost (127.0.0.1) y en el puerto 8080.
# Usará la clase ManejadorHttp para manejar las solicitudes entrantes.
server = HTTPServer(('localhost', 8080), ManejadorHttp)

# Imprimimos en consola que el servidor está corriendo.
print("Servidor corriendo en http://localhost:8080")

# Iniciamos el servidor para que quede escuchando indefinidamente.
server.serve_forever()
