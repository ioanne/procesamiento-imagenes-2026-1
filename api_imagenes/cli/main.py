import argparse

def main():
    # Crear el parser
    parser = argparse.ArgumentParser(description="Ejemplo de un CLI en Python")

    # Definir argumentos
    parser.add_argument("--nombre", type=str, help="Tu nombre", required=True)
    parser.add_argument("--edad", type=int, help="Tu edad", required=True)

    # Parsear los argumentos
    args = parser.parse_args()

    # Usar los argumentos
    print(f"Hola, {args.nombre}. Tienes {args.edad} años.")

if __name__ == "__main__":
    main()