# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dada su base y altura.
    
    Parámetros:
    - base: Largo de la base del rectángulo (float).
    - altura: Altura del rectángulo (float).
    
    Retorna:
    - Área del rectángulo (float).
    """
    return base * altura

# Llamada a la función con valores de prueba
area = calcular_area_rectangulo(5, 10)
print("Área del rectángulo:", area)  # Imprime: Área del rectángulo: 50
