def autenticar_usuario(usuario, contrasena):
    """Autentica al usuario verificando que el nombre de usuario y la contraseña coincidan."""
    # Diccionario que simula una base de datos de usuarios
    base_datos = {
        "admin": "12345",
        "usuario1": "contrasena123",
        "usuario2": "miClave"
    }
    # Verifica que el usuario y la contraseña coincidan
    if usuario in base_datos and base_datos[usuario] == contrasena:
        return "Autenticación exitosa"
    else:
        return "Nombre de usuario o contraseña incorrectos"

# Pruebas de autenticación
print(autenticar_usuario("admin", "12345"))  # Imprime: Autenticación exitosa
print(autenticar_usuario("usuario1", "contrasena123"))  # Imprime: Autenticación exitosa
print(autenticar_usuario("usuario1", "clave_incorrecta"))  # Imprime: Nombre de usuario o contraseña incorrectos
