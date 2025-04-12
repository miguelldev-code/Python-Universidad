# Paso 1: Mostrar bienvenida
print("🧮 Calculadora de división con manejo de errores")

# Paso 2: Usar try-except para evitar que el programa se detenga por errores
try:
    # Solicitar al usuario dos números
    num1 = int(input("Ingresa el numerador: "))
    num2 = int(input("Ingresa el denominador: "))

    # Realizar la división
    resultado = num1 / num2

# Paso 3: Capturar error si el usuario ingresa algo que no se puede convertir a entero
except ValueError:
    print("❌ Error: Debes ingresar solo números enteros.")

# Paso 4: Capturar error si intenta dividir entre cero
except ZeroDivisionError:
    print("❌ Error: No puedes dividir entre cero.")

# Paso 5: Si no ocurre ningún error, mostrar el resultado
else:
    print(f"✅ Resultado: {num1} / {num2} = {resultado}")

# Paso 6: Esta parte se ejecuta siempre, haya o no error
finally:
    print("Gracias por usar la calculadora. 👋")
