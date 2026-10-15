import argparse
import json
import csv
import sys

def json_to_csv(input_data, output_file, delimiter):
    try:
        # Cargar los datos JSON
        data = json.loads(input_data)
        
        # Estrategia de Filtro: Asegurar que la data sea una lista de diccionarios
        if isinstance(data, dict):
            data = [data]
        elif not isinstance(data, list) or not all(isinstance(i, dict) for i in data):
            raise ValueError("El JSON debe ser un diccionario o una lista de diccionarios con un nivel de profundidad (flat).")

        if not data:
            print("Advertencia: El JSON proporcionado esta vacio.", file=sys.stderr)
            return

        # Extraer cabeceras dinámicamente desde el primer elemento
        headers = list(data[0].keys())

        # Escribir salida CSV
        writer = csv.DictWriter(output_file, fieldnames=headers, delimiter=delimiter)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    except json.JSONDecodeError as e:
        print(f"Error critico de formato JSON: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error de ejecucion: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Filtro para convertir formato JSON a CSV.")
    parser.add_argument("-i", "--input", help="Archivo de entrada. Si se omite, utiliza entrada estandar (stdin).")
    parser.add_argument("-o", "--output", help="Archivo de salida. Si se omite, utiliza salida estandar (stdout).")
    parser.add_argument("-d", "--delimiter", default=",", help="Caracter delimitador. Por defecto es coma (,).")

    args = parser.parse_args()

    # Manejo robusto de la entrada (Archivo o Stdin)
    if args.input:
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                input_data = f.read()
        except FileNotFoundError:
            print(f"Excepcion: El archivo de entrada '{args.input}' no fue encontrado.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Excepcion al leer el archivo de entrada: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        input_data = sys.stdin.read()

    # Manejo robusto de la salida (Archivo o Stdout)
    if args.output:
        try:
            output_file = open(args.output, 'w', newline='', encoding='utf-8')
        except Exception as e:
            print(f"Excepcion al abrir el archivo de salida: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        output_file = sys.stdout

    # Ejecucion principal del filtro
    json_to_csv(input_data, output_file, args.delimiter)

    # Cierre de recursos
    if args.output:
        output_file.close()

if __name__ == "__main__":
    main()