from PIL import Image, ImageFilter

image = Image.open('proyecto_imagenes_4/naranja.jpg')

image.filter(ImageFilter.SMOOTH).save('proyecto_imagenes_4/naranja_smooth.jpg')