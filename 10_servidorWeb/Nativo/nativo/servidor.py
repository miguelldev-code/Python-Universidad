from http.server import HTTPServer, BaseHTTPRequestHandler # IMPORTANTDO SERVIDOR Y MANEJADOR DE RUTAS
from urllib.parse import parse_qs # PARA PARSEAR LO QUE LLEGA DE POST



# CLASE DEBE DEFINIRSE Y TENER LOS ATRIBUTOS DE BASEHTTPREQUESTHANDLER
# PERMITIENDO
class index(BaseHTTPRequestHandler):
    def do_GET(self):
        match self.path:
            case "/":

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("<h1>SERVIDOR FUNCIONADO</h1>", "utf-8"))

            case "/html":

                self.serve_file("pagina.html", "text/html")


            case "/form":
                self.serve_file("form.html", "text/html")


            case "/formdata":
                self.serve_file("formData.html", "text/html")

            case _:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("OTRA RUTA", "utf-8"))
    
    def do_POST(self):
         # 1. Leer la longitud del cuerpo de la petición
        content_length = int(self.headers['Content-Length'])
        # 2. Leer los datos enviados (bytes) y decodificarlos a string
        post_data = self.rfile.read(content_length).decode('utf-8')
        # 3. Parsear los datos (ej: 'nombre=Juan&edad=25' → {'nombre': ['Juan'], 'edad': ['25']})
        datos = parse_qs(post_data)
        
        # 4. Procesar los datos (ej: obtener el nombre)
        nombre = datos.get('nombre', [''])[0]  # Si no hay nombre, devuelve ''
        
        # MANEJANDO LAS RUTAS PARA EL RESULTADO
        # IMPORTANTE QUE LA RUTA SEA LA QUE ESTA EN EL HTML EN EL ACTION="/ruta"
        if self.path == "/form":
            # 5. Responder con una página de resultado
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(nombre, "utf-8"))
        if self.path == "/formdata":
            ## AQui se tiene el mismo html pero en string para agregar las variables

            html = f"""<!DOCTYPE html>
            <html>
            <head>
                <title>Formulario POST</title>
                <link rel="stylesheet" href="/static/styles.css">
            </head>
            <body>
                <h1>Envía tus datos</h1>
                <form method="POST" action="/formdata">
                    <label for="nombre">Nombre:</label>
                    <input type="text" id="nombre" name="nombre" required>
                    <button type="submit">Enviar</button>
                </form>
                <p> {nombre}
            </body>
            </html>"""
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # se envie de la manera rustica
            self.wfile.write(bytes(html, "utf-8"))




    # FUNCION PARA QUE CARGE LOS ARCHIVOS Y LOS MUESTRE
    def serve_file(self, file_path, content_type, status_code=200):
        try:
            with open(file_path, 'rb') as file:
                self.send_response(status_code)
                self.send_header("Content-type", content_type)
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_error(404, "Archivo no encontrado")

# SIMPLEMENTE CONFIGURANDO EL SERVER
def startServer():
    host = "localhost"
    port = 8080
    server = HTTPServer((host, port), index)
    print(f"Servidor arranco en http://{host}:{port}")
    server.serve_forever()

# QUE SE EJECUTE SOLO SIEMPRE Y CUANDO ARRANQUE EN EL MISMO ARCHIVO
if __name__ == "__main__":
    startServer()