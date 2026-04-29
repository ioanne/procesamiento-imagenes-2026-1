"""
Ajustes de tono y color
    Brillo, contraste, saturación,
    balance de blancos (desaturar, recolorear), ecualizacion de histogramas,
    escala de grises

Filtros espaciales
    Desenfoque simple, desenfoque Gaussiano,
    nitidez, detección bordes, relieve(Emboss)

Transformaciones geómetricas
    Rotación, redimension, recorte, flip h, v


Segmentación
    umbrales, detección de contornos

"""

"""
POO 
SOLID Design

S: Single Responsibility Principle
O: Open-Closed Principle
L: Liskov Substitution Principle
I: Interface Segregation Principle
D: Dependency Inversion Principle
"""

from PIL import Image, ImageEnhance, ImageFilter


class Pipeline:
    """ Pipeline de Pillow"""
    def __init__(self, url: str): # Inicializador
        # Atributo privado llamado _image
        self._image = Image.open(url)

    def save(self, new_url: str) -> "Pipeline":
        self._image.save(new_url)
        return self
    

class Tono(Pipeline):

    def brillo(self, factor: float = 2.0) -> "Tono":
        self._image = ImageEnhance.Brightness(self._image).enhance(factor)
        return self
    
    def contraste(self, factor: float = 2.0) -> "Tono":
        self._image = ImageEnhance.Contrast(self._image).enhance(factor)
        return self
    
class Filtros(Pipeline):

    def desenfoque(self) -> "Filtros":
        self._image = self._image.filter(ImageFilter.BLUR)
        return self
    
    def gausianno(self) -> "Filtros":
        self._image = self._image.filter(ImageFilter.GaussianBlur)
        return self

    
tono = Tono("naranja.jpg")
tono.brillo(1).contraste(2).save("naranja_editado.jpg")


filtros = Filtros("naranja.jpg")
filtros.desenfoque().gausianno().save("naranja_editado.jpg")


class Editor(Tono, Filtros):
    pass

editor_imagen = Editor("naranja.jpg")
editor_imagen.brillo(1).contraste(2).desenfoque().save("pepe.jpg")



"""
editor_imagen = Editor("naranja.jpg")
editor_imagen.brillo(1).contraste(2).suavizado(3).save("naranja_editado.jpg")
editor_imagen(
    {
        "brillo": 1,
        "contraste": 2,
        "suavizado": 3,
        "desenfoque": true
    }
).save("nueva_imagen.jpg")

"""