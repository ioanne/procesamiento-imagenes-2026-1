import io
from flask import Flask, render_template, request, send_file, abort
from PIL import Image

from src.service import BackgroundRemovalService
from src.strategies import BlackBackgroundRemover, WhiteBackgroundRemover

app = Flask(__name__, template_folder="web", static_folder="web")


def _build_service(mode: str, tolerance: int) -> BackgroundRemovalService:
    if mode == "white":
        strategy = WhiteBackgroundRemover(tolerance=tolerance)
    elif mode == "black":
        strategy = BlackBackgroundRemover(tolerance=tolerance)
    else:
        abort(400, f"Modo inválido: {mode}")
    return BackgroundRemovalService(strategy)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/remove-background")
def remove_background():
    if "image" not in request.files:
        abort(400, "Falta el archivo 'image'.")

    mode = request.form.get("mode", "white")
    try:
        tolerance = int(request.form.get("tolerance", 30))
    except ValueError:
        abort(400, "tolerance debe ser un entero.")

    try:
        image = Image.open(request.files["image"].stream).convert("RGBA")
    except Exception:
        abort(400, "No se pudo leer la imagen.")

    service = _build_service(mode, tolerance)
    result = service.process_image(image)

    buffer = io.BytesIO()
    result.save(buffer, format="PNG")
    buffer.seek(0)
    return send_file(buffer, mimetype="image/png", download_name="sin_fondo.png")


if __name__ == "__main__":
    app.run(debug=True, port=8889)
