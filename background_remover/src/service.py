from pathlib import Path
from PIL import Image

from .image_io import ImageLoader, ImageSaver
from .strategies import BackgroundRemovalStrategy


class BackgroundRemovalService:
    """
    Orquesta carga, procesamiento y guardado.

    Depende de abstracciones (DIP): recibe la estrategia y los componentes de I/O
    por inyección, por lo que es trivial extender/testear sin tocar esta clase.
    """

    def __init__(
        self,
        strategy: BackgroundRemovalStrategy,
        loader: ImageLoader | None = None,
        saver: ImageSaver | None = None,
    ):
        self._strategy = strategy
        self._loader = loader or ImageLoader()
        self._saver = saver or ImageSaver()

    def process(self, input_path: str | Path, output_path: str | Path) -> Path:
        image = self._loader.load(input_path)
        result = self._strategy.remove(image)
        return self._saver.save(result, output_path)

    def process_image(self, image: Image.Image) -> Image.Image:
        return self._strategy.remove(image)
