def validar_edad(edad_str):
    try:
        edad = int(edad_str)
        if 18 <= edad <= 100:
            return edad
        else:
            raise ValueError("❌ La edad debe estar entre 18 y 100 años.")
    except ValueError as e:
        raise ValueError(f"⚠️ Error en edad: {str(e)}")

def validar_correo(correo):
    if "@" not in correo or "." not in correo:
        raise ValueError("⚠️ Correo no válido. Debe contener '@' y '.'")
    return correo

def main():
    while True:
        try:
            # Pedir datos
            edad_str = input("\nIngresa tu edad: ")
            correo = input("Ingresa tu correo electrónico: ")
            
            # Validar datos (si hay error, salta al except)
            edad_validada = validar_edad(edad_str)
            correo_validado = validar_correo(correo)
            
            # Si todo está bien, salir del bucle
            break
            
        except ValueError as e:
            print(f"\n{str(e)}\nPor favor, intenta de nuevo.\n")
    
    print(f"\n✅ Registro exitoso:")
    print(f"Edad: {edad_validada}")
    print(f"Correo: {correo_validado}")

if __name__ == "__main__":
    main()