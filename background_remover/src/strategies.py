from abc import ABC, abstractmethod
import numpy as np
from PIL import Image


class BackgroundRemovalStrategy(ABC):
    """
    Interfaz de estrategia para volver transparente un fondo.

    Aplica OCP: para agregar un nuevo tipo de fondo (ej. verde chroma-key)
    basta con crear una subclase sin modificar el servicio que la usa.
    """

    @abstractmethod
    def remove(self, image: Image.Image) -> Image.Image: ...


class ColorBackgroundRemover(BackgroundRemovalStrategy):
    """
    Estrategia base: vuelve transparentes los píxeles cercanos a un color objetivo
    dentro de una tolerancia (distancia euclídea en RGB).
    """

    def __init__(self, target_rgb: tuple[int, int, int], tolerance: int = 30):
        if not (0 <= tolerance <= 441):
            raise ValueError("tolerance debe estar entre 0 y 441")
        self._target = np.array(target_rgb, dtype=np.int16)
        self._tolerance = tolerance

    def remove(self, image: Image.Image) -> Image.Image:
        rgba = np.array(image.convert("RGBA"))
        rgb = rgba[..., :3].astype(np.int32)
        distance = np.sqrt(np.sum((rgb - self._target.astype(np.int32)) ** 2, axis=-1))
        mask = distance <= self._tolerance
        rgba[mask, 3] = 0
        return Image.fromarray(rgba, mode="RGBA")


class WhiteBackgroundRemover(ColorBackgroundRemover):
    def __init__(self, tolerance: int = 30):
        super().__init__(target_rgb=(255, 255, 255), tolerance=tolerance)


class BlackBackgroundRemover(ColorBackgroundRemover):
    def __init__(self, tolerance: int = 30):
        super().__init__(target_rgb=(0, 0, 0), tolerance=tolerance)
