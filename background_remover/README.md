# Background Remover

Pequeña utilidad para volver transparente el fondo **blanco** o **negro** de una imagen, usando Pillow + NumPy.

El código sigue principios **SOLID**:

- **SRP** — `ImageLoader`, `ImageSaver` y cada estrategia tienen una sola responsabilidad.
- **OCP** — para soportar un nuevo color de fondo (ej. chroma verde) se agrega una subclase de `BackgroundRemovalStrategy` sin tocar el servicio.
- **LSP** — todas las estrategias son intercambiables detrás de la misma interfaz.
- **ISP** — la interfaz `BackgroundRemovalStrategy` expone sólo `remove(image)`.
- **DIP** — `BackgroundRemovalService` depende de la abstracción `BackgroundRemovalStrategy`, no de implementaciones concretas.

## Estructura

```
background_remover/
├── src/
│   ├── image_io.py        # ImageLoader / ImageSaver
│   ├── strategies.py      # Estrategias (White, Black, Color base)
│   └── service.py         # BackgroundRemovalService (orquestador)
├── web/
│   └── index.html         # Frontend servido por Flask
├── app.py                 # Servidor Flask
├── cli.py                 # CLI con argparse
├── main.py                # Ejemplo programático
├── requirements.txt
└── README.md
```

## Uso — servidor web (Flask)

```bash
python app.py
# abrir http://127.0.0.1:5000/
```

Endpoint:

- `POST /remove-background` — `multipart/form-data` con:
  - `image` (archivo, requerido)
  - `mode` (`white` | `black`, default `white`)
  - `tolerance` (entero, default `30`)

Devuelve un `image/png` con el fondo transparente.

```bash
curl -F "image=@foto.jpg" -F "mode=white" -F "tolerance=25" \
     http://127.0.0.1:5000/remove-background --output salida.png
```

## Instalación

```bash
cd background_remover
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Uso — CLI

```bash
python cli.py <entrada> -o <salida.png> [-m white|black] [-t TOLERANCIA]
```

### Argumentos

| Argumento | Descripción | Default |
|-----------|-------------|---------|
| `input` | Ruta a la imagen de entrada. | — |
| `-o, --output` | Ruta de salida. Debe ser `.png`, `.webp` o `.tiff` (formatos con canal alfa). | — |
| `-m, --mode` | Color a transparentar: `white` o `black`. | `white` |
| `-t, --tolerance` | Tolerancia 0–441 (distancia euclídea en RGB). Valores más altos eliminan más sombras/antialiasing. | `30` |

### Ejemplos

```bash
# Fondo blanco -> transparente
python cli.py foto.jpg -o foto.png

# Fondo negro con tolerancia alta
python cli.py logo.png -o logo_transparente.png -m black -t 60
```

## Uso — programático

```python
from src.service import BackgroundRemovalService
from src.strategies import WhiteBackgroundRemover

service = BackgroundRemovalService(WhiteBackgroundRemover(tolerance=25))
service.process("entrada.jpg", "salida.png")
```

Ejecutar el ejemplo incluido:

```bash
python main.py
# Genera background_remover/ejemplos/entrada.png y salida.png
```

## Extender con un nuevo color

```python
from src.strategies import ColorBackgroundRemover
from src.service import BackgroundRemovalService

green_screen = ColorBackgroundRemover(target_rgb=(0, 255, 0), tolerance=40)
BackgroundRemovalService(green_screen).process("in.png", "out.png")
```
