# Escriba un programa que simule un cajero automatico.
# El usuario comienza con un saldo inicial de 1000 unidades monetarias.
# El programa debe permitir realizar depositos, retiros y mostrar el saldo actual.
# Si el usuario intenta retirar mas dinero del que tiene, se debe mostrar un mensaje de error.
# El programa finaliza cuando el usuario ingresa la opcion 4.

# INICIALIZAR SALDO
saldo = 1000

while True:
    # MOSTRAR MENU
    print("\nCajero Automatico")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")
    
    # PEDIR OPCION AL USUARIO
    opcion = input("Selecciona una opcion: ")
    
    if not opcion.isdigit():
        print("Entrada no valida. Ingresa un numero del 1 al 4.")
        continue
    
    opcion = int(opcion)
    
    # PROCESAR OPCION
    if opcion == 1:
        # DEPOSITAR DINERO
        monto = input("Ingrese el monto a depositar: ")
        
        if not monto.replace('.', '', 1).isdigit():
            print("Entrada no valida. Ingresa un monto numerico.")
            continue
        
        monto = float(monto)
        
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
            continue
        
        saldo += monto
        print(f"Has depositado {monto:.2f}. Saldo actual: {saldo:.2f}")
    
    elif opcion == 2:
        # RETIRAR DINERO
        monto = input("Ingrese el monto a retirar: ")
        
        if not monto.replace('.', '', 1).isdigit():
            print("Entrada no valida. Ingresa un monto numerico.")
            continue
        
        monto = float(monto)
        
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
            continue
        
        if monto > saldo:
            print("Fondos insuficientes.")
            continue
        
        saldo -= monto
        print(f"Has retirado {monto:.2f}. Saldo actual: {saldo:.2f}")
    
    elif opcion == 3:
        # MOSTRAR SALDO
        print(f"Saldo actual: {saldo:.2f}")
    
    elif opcion == 4:
        # SALIR DEL PROGRAMA
        print("Gracias por usar el cajero automatico. Hasta luego!")
        break
    
    else:
        print("Opcion no valida. Ingresa un numero del 1 al 4.")
