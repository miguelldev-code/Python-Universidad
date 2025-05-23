from flask import Flask, request, redirect, render_template, url_for
import sqlite3

app = Flask(__name__)

# Crear la tabla si no existe
with sqlite3.connect("usuarios.db") as con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    """)

# Ruta principal: muestra formulario y lista de usuarios
@app.route('/')
def inicio():
    con = sqlite3.connect("usuarios.db")
    usuarios = con.execute("SELECT * FROM usuarios").fetchall()
    con.close()
    return render_template("index.html", usuarios=usuarios)

# Agregar usuario
@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form.get("nombre")
    if nombre:
        con = sqlite3.connect("usuarios.db")
        con.execute("INSERT INTO usuarios (nombre) VALUES (?)", (nombre,))
        con.commit()
        con.close()
    return redirect(url_for('inicio'))

# Mostrar formulario para editar usuario
@app.route('/editar/<int:id>')
def editar(id):
    con = sqlite3.connect("usuarios.db")
    usuario = con.execute("SELECT * FROM usuarios WHERE id = ?", (id,)).fetchone()
    con.close()
    return render_template("editar.html", usuario=usuario)

# Actualizar usuario
@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    nombre = request.form.get("nombre")
    con = sqlite3.connect("usuarios.db")
    con.execute("UPDATE usuarios SET nombre = ? WHERE id = ?", (nombre, id))
    con.commit()
    con.close()
    return redirect(url_for('inicio'))

# Eliminar usuario
@app.route('/eliminar/<int:id>')
def eliminar(id):
    con = sqlite3.connect("usuarios.db")
    con.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    con.commit()
    con.close()
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)
