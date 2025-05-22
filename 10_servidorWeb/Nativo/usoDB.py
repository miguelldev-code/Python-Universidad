from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
import sqlite3
import os

# Asegurar que la base de datos exista y tenga la tabla
DB_PATH = "/10_servidorWeb/Nativo/src/usuarios.db"
if not os.path.exists(DB_PATH):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()


class Manejador(BaseHTTPRequestHandler):
    def do_GET(self):
        ruta = urlparse(self.path).path

        if ruta == "/usuarios":
            # Obtener todos los usuarios
            conexion = sqlite3.connect(DB_PATH)
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre FROM usuarios")
            usuarios = cursor.fetchall()
            conexion.close()

            # Convertir a JSON
            lista_usuarios = [{"id": u[0], "nombre": u[1]} for u in usuarios]

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(lista_usuarios).encode("utf-8"))
        else:
            # Ruta no encontrada
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode())

    def do_POST(self):
        ruta = urlparse(self.path).path

        if ruta == "/registro":
            longitud = int(self.headers.get("Content-Length", 0))
            cuerpo = self.rfile.read(longitud).decode("utf-8")

            # Asegurarse que sea JSON
            tipo_contenido = self.headers.get("Content-Type", "")
            if "application/json" not in tipo_contenido:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Se requiere JSON"}).encode())
                return

            try:
                datos = json.loads(cuerpo)
                nombre = datos.get("nombre", "").strip()

                if not nombre:
                    raise ValueError("Nombre vacío")

                # Guardar en la base de datos
                conexion = sqlite3.connect(DB_PATH)
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO usuarios (nombre) VALUES (?)", (nombre,))
                conexion.commit()
                conexion.close()

                # Respuesta
                self.send_response(201)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"mensaje": f"Usuario '{nombre}' registrado"}).encode())

            except (json.JSONDecodeError, ValueError) as e:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())

        else:
            # Ruta no válida
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode())


# Iniciar servidor
servidor = HTTPServer(('localhost', 8081), Manejador)
print("Servidor corriendo en http://localhost:8081")
servidor.serve_forever()

# Enviar usuario POST
# curl -X POST http://localhost:8081/registro \
#   -H "Content-Type: application/json" \
#   -d '{"nombre": "Carlos"}'

# Listar usuario GET
# curl http://localhost:8081/usuarios



