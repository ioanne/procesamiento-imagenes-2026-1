from PIL import Image, ImageFilter

image = Image.open('proyecto_imagenes_3/naranja.jpg')

image.filter(ImageFilter.BLUR).save('proyecto_imagenes_3/naranja_blur.jpg')
