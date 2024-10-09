import matplotlib.pyplot as plt

# Datos proporcionados
deformacion = [0.00000, 0.00022, 0.00038, 0.00072, 0.00108, 0.00145, 0.00165, 0.00173, 0.00185, 0.00212, 0.00500, 0.00800, 0.01300, 0.03100, 0.14000, 0.24200]
esfuerzo = [0.00, 5092.96, 10185.92, 20371.83, 30557.75, 40743.67, 45836.62, 47873.81, 49910.99, 51438.88, 53985.36, 56022.54, 61115.50, 66208.46, 72320.01, 59842.26]

# Crear la gráfica
plt.figure(figsize=(10,6))
plt.plot(deformacion, esfuerzo, marker='o', linestyle='-', color='b')

# Etiquetas y título
plt.title('Gráfica de Esfuerzo vs Deformación Unitaria', fontsize=16)
plt.xlabel('Deformación Unitaria', fontsize=14)
plt.ylabel('Esfuerzo (psi)', fontsize=14)

# Mostrar la gráfica
plt.grid(True)
plt.show()
