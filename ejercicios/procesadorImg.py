# Capturar foto desde la camara con OpenCV
# Guardan la imagen en una carpeta
# Aplicar ediciones con OpenCV

import cv2
import os

# Definir ruta de salida para guardar la imagen
output_dir = r"C:\Users\elsup\Documentos\Programacion\Lenguaje Python\Computacion 1\dfs\processImg\imgs"
output_path = os.path.join(output_dir, "captured_image.jpg")

# Capturar imagen desde la cámara
cap = cv2.VideoCapture(0)  # 0 indica la cámara por defecto

if not cap.isOpened():
    print("[ERROR] No se pudo acceder a la cámara.")
else:
    print("[INFO] Presiona 'Espacio' para tomar la foto o 'ESC' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] No se pudo capturar la imagen.")
            break

        # Mostrar la vista de la cámara en tiempo real
        cv2.imshow("Captura de Imagen", frame)

        # Controles: Espacio para capturar, ESC para salir
        key = cv2.waitKey(1) & 0xFF
        if key == 32:  # Tecla 'Espacio'
            cv2.imwrite(output_path, frame)
            print(f"[INFO] Imagen guardada en: {output_path}")
            break
        elif key == 27:  # Tecla 'ESC'
            print("[INFO] Captura cancelada.")
            break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()

# ----------- PROCESAR LA IMAGEN CAPTURADA --------------
# Cargar la imagen capturada
image = cv2.imread(output_path)

# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar el detector de bordes Canny
edges = cv2.Canny(gray_image, 100, 200)

# Mostrar las imágenes procesadas
cv2.imshow("Imagen Original", image)
cv2.imshow("Escala de Grises", gray_image)
cv2.imshow("Bordes Detectados (Canny)", edges)

# Guardar las imágenes procesadas
cv2.imwrite(os.path.join(output_dir, "gray_image.jpg"), gray_image)
cv2.imwrite(os.path.join(output_dir, "edges.jpg"), edges)

print("[INFO] Procesamiento completado. Presiona cualquier tecla para salir.")
cv2.waitKey(0)
cv2.destroyAllWindows()

        
  