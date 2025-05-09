# Sintaxis Manejo de errores Python

try:
    # Código que puede causar un error
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("❌ No se puede dividir entre cero.")
except ValueError:
    print("❌ Debes ingresar un número válido.")

# Estructura

# try:
#     # Bloque principal
# except TipoDeError1:
#     # Acción si ocurre ese error
# except TipoDeError2:
#     # Otro tipo de error
# else:
#     # Si NO ocurre ningún error
# finally:
#     # Siempre se ejecuta, haya o no error
