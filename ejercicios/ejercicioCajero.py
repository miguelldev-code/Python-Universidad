"""
 Simulador de Cajero Automático en Python   
Este programa permite iniciar sesión con un PIN y realizar operaciones como:  
 Consultar saldo  
 Depositar dinero  
 Retirar dinero  
 Salir del sistema  
"""

# Diccionario simulando una cuenta bancaria
cuenta = {"saldo": 1000, "pin": "1234"}

def iniciar_sesion():
    """Verifica el PIN antes de acceder al sistema."""
    intentos = 3
    while intentos > 0:
        pin = input(" Ingresa tu PIN: ")
        if pin == cuenta["pin"]:
            print(" Acceso concedido.\n")
            return True
        else:
            intentos -= 1
            print(f" PIN incorrecto. Intentos restantes: {intentos}\n")
    
    print(" Cuenta bloqueada. Intenta más tarde.")
    return False

def consultar_saldo():
    """Muestra el saldo actual de la cuenta."""
    print(f" Tu saldo actual es: ${cuenta['saldo']}\n")

def depositar():
    """Permite ingresar dinero en la cuenta."""
    try:
        monto = float(input(" Ingresa el monto a depositar: "))
        if monto > 0:
            cuenta["saldo"] += monto
            print(f" Depósito exitoso. Nuevo saldo: ${cuenta['saldo']}\n")
        else:
            print(" Ingresa un monto válido.\n")
    except ValueError:
        print(" Error: Ingresa un número válido.\n")

def retirar():
    """Permite retirar dinero, validando el saldo disponible."""
    try:
        monto = float(input(" Ingresa el monto a retirar: "))
        if monto > 0 and monto <= cuenta["saldo"]:
            cuenta["saldo"] -= monto
            print(f" Retiro exitoso. Nuevo saldo: ${cuenta['saldo']}\n")
        elif monto > cuenta["saldo"]:
            print(" Fondos insuficientes.\n")
        else:
            print(" Ingresa un monto válido.\n")
    except ValueError:
        print(" Error: Ingresa un número válido.\n")

def menu():
    """Menú interactivo con opciones del cajero."""
    if not iniciar_sesion():
        return

    while True:
        print("\n🏦 **Menú del Cajero Automático**")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Salir")

        opcion = input("\nElige una opción (1-4): ")

        match opcion:
            case "1":
                consultar_saldo()
            case "2":
                depositar()
            case "3":
                retirar()
            case "4":
                print(" Gracias por usar el cajero. ¡Hasta pronto!")
                break
            case _:
                print(" Opción no válida, intenta de nuevo.\n")

menu()
