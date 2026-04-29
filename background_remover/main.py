"""
Ejemplo de uso programático del servicio de remoción de fondo.

Generamos una imagen sintética con fondo blanco y un círculo rojo,
y luego aplicamos la estrategia para volver el fondo transparente.
"""
from pathlib import Path
from PIL import Image, ImageDraw

from src.service import BackgroundRemovalService
from src.strategies import WhiteBackgroundRemover


def _crear_imagen_demo(path: Path) -> None:
    img = Image.new("RGB", (200, 200), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.ellipse((40, 40, 160, 160), fill=(220, 30, 30))
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)


def main() -> None:
    base = Path(__file__).parent / "ejemplos"
    entrada = base / "entrada.png"
    salida = base / "salida.png"

    _crear_imagen_demo(entrada)

    service = BackgroundRemovalService(WhiteBackgroundRemover(tolerance=20))
    resultado = service.process(entrada, salida)

    print(f"Imagen de entrada: {entrada}")
    print(f"Imagen con fondo transparente: {resultado}")


if __name__ == "__main__":
    main()
