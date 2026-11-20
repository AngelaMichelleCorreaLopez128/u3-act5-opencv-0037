import cv2 
import numpy as np 
# 2. Lectura y visualización de imágenes
# 2.1 Ejemplo de código:
# Leer la imagen del archivo
image0037 = cv2.imread( 'Ariana Grande.jpeg' ) 
# Mostrar la imagen en una ventana
cv2.imshow( 'Image Angela Correa 0037' , image0037) 
# Esperar a que se presione una tecla y cerrar la ventana
cv2.waitKey(0) 
cv2.destroyAllWindows()
# 3. Conversión entre espacios de color
# 3.1 Ejemplo de código: Convertir una imagen a escala de grises
# Cargar la imagen
image0037 = cv2.imread( 'Ariana Grande.jpeg' ) 
# Convertir a escala de grises
gray_image = cv2.cvtColor(image0037, cv2.COLOR_BGR2GRAY) 
# Guardar la imagen en escala de grises
cv2.imwrite( 'gray0037_Ariana Grande.jpeg' , gray_image)
# 4. Cambiar el tamaño de una imagen
# 4.1 Ejemplo de código: Cambiar el tamaño de la imagen
# Cargar la imagen
image = cv2.imread( 'Ariana Grande.jpeg' ) 
# Redimensionar la imagen a 300x200
resized_image = cv2.resize(image, (300, 200)) 
# Guardar la imagen redimensionada
cv2.imwrite( 'resized0037_Ariana Grande.jpeg' , resized_image)
# 5. Rotar una imagen
# 5.1 Ejemplo de código: Girar la imagen 90 grados.
# Cargar la imagen
image = cv2.imread('Ariana Grande.jpeg') 
# Obtener la altura y el ancho de la imagen
(h, w) = image.shape[:2] 
# Definir el centro de la imagen
center = (w // 2, h // 2) 
#
Matriz_de_rotación_matrix = cv2.getRotationMatrix2D(center, 90, 1.0) 
# Realizar la rotación
rotated_image = cv2.warpAffine(image, Matriz_de_rotación_matrix, (w, h)) 
# Guardar la imagen rotada
cv2.imwrite('rotated0037_# Cargar la imagen Ariana Grande.jpeg', rotated_image)
# 6. Desenfoque de una imagen
# 6.1 Ejemplo de código: Aplicación de un desenfoque gaussiano
# Cargar la imagen
image = cv2.imread( 'Ariana Grande.jpeg' ) 
# Aplicar desenfoque gaussiano
blured_image = cv2.GaussianBlur(image, (15, 15), 0) 
# Guardar la imagen desenfocada
cv2.imwrite( 'blurred0037_Ariana Grande.jpeg' , blured_image)
# 7. Detección de bordes mediante el algoritmo de Canny
# 7.1 Ejemplo de código: Detección de bordes mediante el algoritmo de Canny
# Cargar la imagen
image = cv2.imread( 'Ariana Grande.jpeg' ) 
# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# Aplicar el detector de bordes Canny
edges = cv2.Canny(gray_image, 100 , 200 ) 
# Guardar la imagen de bordes
cv2.imwrite( 'edges0037.jpg' , edges)
# 8. Dibujar formas y añadir texto
# 8.1 Ejemplo de código: Dibujar un rectángulo y añadir texto.
# Cargar la imagen
image = cv2.imread( 'Ariana Grande.jpeg' ) 
# Dibujar un rectángulo
cv2.rectangle(image, ( 50 , 50 ), ( 200 , 200 ), ( 255 , 0 , 0 ), 3 ) 
# Agregar texto a la imagen
cv2.putText(image, 'OpenCV' , ( 60 , 40 ), cv2.FONT_HERSHEY_SIMPLEX, 1 , ( 0 , 255 , 0 ), 2 ) 
# Guardar la imagen de salida
cv2.imwrite( 'output0037_Ariana Grande.jpeg' , image)
# 9. Umbralización
# 9.1 Ejemplo de código: Aplicar umbralización binaria
# Cargar la imagen
image = cv2.imread( 'Ariana Grande.jpeg' , 0 ) 
# Aplicar umbralización
_, thresh_image = cv2.threshold(image, 127 , 255 , cv2.THRESH_BINARY) 
# Guardar la imagen umbralizada
cv2.imwrite( 'threshold0037_Ariana Grande.jpeg' , thresh_image)
# 10. Detección de contornos
# 10.1 Ejemplo de código: Detectar contornos y dibujarlos
# Cargar la imagen
image = cv2.imread('Ariana Grande.jpeg')

# Verificar que la imagen se haya cargado correctamente
if image is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta del archivo.")
else:
    # Convertir la imagen a escala de grises
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Encontrar bordes
    edges = cv2.Canny(gray_image, 100, 200)

    # Encontrar contornos
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar contornos en la imagen original
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    # Guardar la imagen de salida con contornos
    cv2.imwrite('contours0037_Ariana Grande.jpeg', image)
    print("Imagen guardada exitosamente como 'contours_image.jpg'.")