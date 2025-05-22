from http.server import HTTPServer
from rutas.manejador import Manejador

def iniciar_servidor():
    host = "localhost"
    puerto = 8080
    servidor = HTTPServer((host, puerto), Manejador)
    print(f"Servidor activo en http://{host}:{puerto}")
    servidor.serve_forever()

if __name__ == "__main__":
    iniciar_servidor()