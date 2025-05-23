from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Función para conectar con la base de datos
def conectar_bd():
    return sqlite3.connect("/10_servidorWeb/Flask/db/usuarios.db")

# Crear la tabla si no existe
with conectar_bd() as con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    """)

# ---------------------------
# CREATE - Agregar usuario
# ---------------------------
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    nombre = datos.get('nombre')
    if not nombre:
        return jsonify({"error": "Nombre requerido"}), 400

    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute("INSERT INTO usuarios (nombre) VALUES (?)", (nombre,))
    con.commit()
    con.close()
    return jsonify({"mensaje": f"Usuario {nombre} creado"}), 201

# ---------------------------
# READ - Obtener todos
# ---------------------------
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = [{"id": fila[0], "nombre": fila[1]} for fila in cursor.fetchall()]
    con.close()
    return jsonify(usuarios)

# ---------------------------
# READ - Obtener uno por ID
# ---------------------------
@app.route('/usuarios/<int:id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))
    fila = cursor.fetchone()
    con.close()
    if fila:
        return jsonify({"id": fila[0], "nombre": fila[1]})
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

# ---------------------------
# UPDATE - Actualizar nombre
# ---------------------------
@app.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    datos = request.get_json()
    nombre = datos.get('nombre')
    if not nombre:
        return jsonify({"error": "Nombre requerido"}), 400

    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute("UPDATE usuarios SET nombre = ? WHERE id = ?", (nombre, id_usuario))
    con.commit()
    con.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"mensaje": f"Usuario {id_usuario} actualizado a {nombre}"})

# ---------------------------
# DELETE - Eliminar usuario
# ---------------------------
@app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    con = conectar_bd()
    cursor = con.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    con.commit()
    con.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"mensaje": f"Usuario {id_usuario} eliminado"})

# ---------------------------
# Ejecutar servidor
# ---------------------------
if __name__ == '__main__':
    app.run(debug=True)


'''🧪 Pruebas con curl o Postman
Crear usuario:
curl -X POST http://localhost:5000/usuarios -H "Content-Type: application/json" -d '{"nombre": "Laura"}'

Listar usuarios:
curl http://localhost:5000/usuarios

Consultar uno:
curl http://localhost:5000/usuarios/1

Actualizar usuario:
curl -X PUT http://localhost:5000/usuarios/1 -H "Content-Type: application/json" -d '{"nombre": "Laura Gómez"}'

Eliminar usuario:
curl -X DELETE http://localhost:5000/usuarios/1'''