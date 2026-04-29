from pathlib import Path
from PIL import Image

class ImageLoader:
    """Responsable únicamente de cargar imágenes desde disco (SRP)."""

    def load(self, path: str | Path) -> Image.Image:
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"No se encontró la imagen: {path}")
        return Image.open(path).convert("RGBA")


class EstoEsUnError(Exception):
    pass


def funcion_codigo(argumento):
    if argumento:
        raise EstoEsUnError
    print("No fallo")


try:
    print("codigo...")
    funcion_codigo(True)
except EstoEsUnError:
    print("Esto es un error")

