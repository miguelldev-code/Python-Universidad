# ZeroDivisionError: dividir entre cero
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError ➜ {e}")

# ValueError: convertir algo inválido (como texto a número)
try:
    numero = int("hola")
except ValueError as e:
    print(f"ValueError ➜ {e}")

# TypeError: operar con tipos incompatibles
try:
    suma = "texto" + 5
except TypeError as e:
    print(f"TypeError ➜ {e}")

# IndexError: acceder a un índice fuera del rango
try:
    lista = [1, 2, 3]
    valor = lista[5]
except IndexError as e:
    print(f"IndexError {e}")

# KeyError: acceder a una clave que no existe en un diccionario
try:
    persona = {"nombre": "Ana"}
    print(persona["edad"])
except KeyError as e:
    print(f"KeyError ➜ {e}")

# FileNotFoundError: intentar abrir un archivo que no existe
try:
    with open("archivo_inexistente.txt") as f:
        contenido = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError ➜ {e}")

# AttributeError: llamar un método que no existe para un tipo de dato
try:
    numero = 5
    numero.append(10)
except AttributeError as e:
    print(f"AttributeError ➜ {e}")

# NameError: usar una variable que no ha sido definida
try:
    print(valor_que_no_existe)
except NameError as e:
    print(f"NameError ➜ {e}")

# ImportError: intentar importar un módulo que no existe
try:
    import modulo_que_no_existe
except ImportError as e:
    print(f"ImportError ➜ {e}")

# IndentationError (este no se puede capturar con try-except, ocurre al escribir mal el código)
# Mal ejemplo que causaría error si se descomenta:
# def saludar():
# print("Hola")  # ← Indentación incorrecta
