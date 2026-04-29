from pathlib import Path
from PIL import Image


class ImageLoader:
    """Responsable únicamente de cargar imágenes desde disco (SRP)."""

    def load(self, path: str | Path) -> Image.Image:
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"No se encontró la imagen: {path}")
        return Image.open(path).convert("RGBA")


class ImageSaver:
    """Responsable únicamente de persistir imágenes en disco (SRP)."""

    def save(self, image: Image.Image, path: str | Path) -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix.lower() not in {".png", ".webp", ".tiff"}:
            raise ValueError(
                f"Formato '{path.suffix}' no soporta transparencia. Usá .png, .webp o .tiff"
            )
        image.save(path)
        return path
