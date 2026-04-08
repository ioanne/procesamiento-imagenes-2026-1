# Pillow, OpenCV
# import
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import cv2

image = Image.open('naranja.jpg')


# desenfoque
image.filter(ImageFilter.BLUR).save('naranja_blur.jpg')

image.filter(ImageFilter.SMOOTH).save('naranja_smooth.jpg')

ImageEnhance.Brightness(image).enhance(0.8).save('naranja_brightness.jpg')
ImageEnhance.Color(image).enhance(0.5).save('naranja_color.jpg')
ImageEnhance.Contrast(image).enhance(1.5).save('naranja_contrast.jpg')

ImageEnhance.Color(image).enhance(0).save('naranja_byn.jpg')


# Convertir la imagen a escala de grises
gray_image = image.convert('L')
gray_image.save('gris.jpg')

# Aumentar el contraste para resaltar los bordes
enhanced_image = ImageOps.autocontrast(gray_image)

# Aplicar un filtro de detección de bordes
edges = enhanced_image.filter(ImageFilter.CONTOUR)

# Guardar la imagen con bordes detectados
edges.save('naranja_edges_detected.jpg')


image = cv2.imread('naranja_blur.jpg')

prueba = cv2.Canny(image, 110, 200)
cv2.imwrite('naranja_edges_detected2.jpg', prueba)


import cv2

# Leer la imagen
image = cv2.imread('naranja.jpg')

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro de desenfoque para reducir el ruido
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Aplicar el detector de bordes Canny
edges = cv2.Canny(blurred_image, 50, 150)

# Encontrar los contornos
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos en la imagen original
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Guardar la imagen con los contornos dibujados
cv2.imwrite('naranja_contours_fixed.jpg', contour_image)

print("La imagen con los contornos detectados se ha guardado como 'naranja_contours_fixed.jpg'")

