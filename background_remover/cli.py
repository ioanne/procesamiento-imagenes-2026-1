import argparse
import sys
from pathlib import Path

from src.service import BackgroundRemovalService
from src.strategies import (
    BackgroundRemovalStrategy,
    BlackBackgroundRemover,
    WhiteBackgroundRemover,
)


def _build_strategy(mode: str, tolerance: int) -> BackgroundRemovalStrategy:
    if mode == "white":
        return WhiteBackgroundRemover(tolerance=tolerance)
    if mode == "black":
        return BlackBackgroundRemover(tolerance=tolerance)
    raise ValueError(f"Modo no soportado: {mode}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="background-remover",
        description="Convierte el fondo blanco o negro de una imagen en transparente.",
    )
    parser.add_argument("input", type=Path, help="Ruta a la imagen de entrada.")
    parser.add_argument(
        "-o", "--output", type=Path, required=True,
        help="Ruta de salida (.png, .webp o .tiff).",
    )
    parser.add_argument(
        "-m", "--mode", choices=["white", "black"], default="white",
        help="Color de fondo a eliminar (default: white).",
    )
    parser.add_argument(
        "-t", "--tolerance", type=int, default=30,
        help="Tolerancia de color 0-441 (default: 30).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        strategy = _build_strategy(args.mode, args.tolerance)
        service = BackgroundRemovalService(strategy)
        result_path = service.process(args.input, args.output)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    print(f"Imagen guardada en: {result_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
