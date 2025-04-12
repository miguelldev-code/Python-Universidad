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

try:
    # Bloque donde puede ocurrir un error
except TipoDeError:
    # Qué hacer si ocurre ese error
else:
    # Qué hacer si NO ocurre ningún error
finally:
    # Qué hacer SIEMPRE (ocurra o no error)
