from PIL import Image, ImageFilter

image = Image.open('naranja.jpg')

image.filter(ImageFilter.BLUR).save('naranja_blur.jpg')
