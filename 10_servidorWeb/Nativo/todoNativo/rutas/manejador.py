from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import os

tareas = []  # Lista en memoria para las tareas

class Manejador(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.servir_html_con_tareas()
        elif self.path == "/static/css/styles.css":
            self.servir_archivo("static/css/styles.css", "text/css")
        else:
            self.send_error(404, "Página no encontrada")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        datos = parse_qs(post_data)
        nueva_tarea = datos.get('tarea', [''])[0]
        
        if nueva_tarea:
            tareas.append(nueva_tarea)
        
        self.servir_html_con_tareas()

    #SIMULAR EL TEMPLATE
    def listar_tareas(self, tareas):
        tareasHtml = """
                <!DOCTYPE html>
        <html>
        <head>
            <title>To-Do List</title>
            <link rel="stylesheet" href="/static/css/styles.css">
        </head>
        <body>
    <h1>To-Do List</h1>
        <ul>\n"""
        if len(tareas) != 0:
            for tarea in tareas:
                tareasHtml += f"<li>{ tarea }</li>\n"
        
        tareasHtml += """
        </ul>
            <form method="POST" action="/">
            <input type="text" name="tarea" placeholder="Añade una tarea" required>
            <button type="submit">Agregar</button>
        </form>
        </body>
        </html>
        """
        return tareasHtml
    

    # PARA LA PAGINA CON TAREAS
    def servir_html_con_tareas(self):
        ruta_html = os.path.join(os.path.dirname(__file__), "../templates/index.html")


        html = self.listar_tareas(tareas)

        self.send_response(200)
        self.send_header("Content-type","text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(bytes(html, "utf-8"))

    # PARA EL CSS
    def servir_archivo(self, ruta, content_type):
        ruta_completa = os.path.join(os.path.dirname(__file__), "..", ruta)
        try:
            with open(ruta_completa, 'rb') as archivo:
                self.send_response(200)
                self.send_header("Content-type", content_type)
                self.end_headers()
                self.wfile.write(archivo.read())
        except FileNotFoundError:
            self.send_error(404, "Archivo no encontrado")