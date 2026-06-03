#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name   # nombre 'getJason' impuesto por enunciado TP6/TP7
"""
# Descripción:
#   Recupera el valor asociado a una clave dentro de un archivo JSON.
#   Implementa el patrón de diseño Singleton con estrategia
#   Branching by Abstraction para la convergencia con la versión
#   procedural original (TP6).
#
# Uso:
#   python3 getJason.py <archivo_json> [clave]
#   python3 getJason.py -v
#
# Argumentos:
#   archivo_json : Ruta al archivo JSON que contiene los datos.
#   clave        : Clave a recuperar del JSON (default: 'token1').
#   -v           : Muestra la versión del programa y termina.
#
# Códigos de salida:
#   0 : Éxito
#   1 : Error de uso / argumentos incorrectos
#   2 : Archivo no encontrado
#   3 : JSON inválido
#   4 : Clave no encontrada en el JSON
#
# Ejemplos:
#   python3 getJason.py sitedata.json
#   python3 getJason.py sitedata.json token1
#   python3 getJason.py sitedata.json token2
#   python3 getJason.py -v
#
################################################################################
"""

import json
import sys
from abc import ABC, abstractmethod

# ─── Constantes del módulo ────────────────────────────────────────────────────
VERSION = "1.1"
DEFAULT_KEY = "token1"
EXIT_OK = 0
EXIT_USAGE = 1
EXIT_FILE = 2
EXIT_JSON = 3
EXIT_KEY = 4


# ─── Abstracción — Branching by Abstraction ───────────────────────────────────
class IJsonReader(ABC):
    """
    Interfaz abstracta para lectores de archivos JSON.

    Define el contrato que deben cumplir todas las implementaciones
    concretas. Es el punto central de la estrategia Branching by
    Abstraction: la rama procedural original (TP6) y la nueva rama
    Singleton (TP7) implementan esta interfaz, lo que permite al
    cliente (main) operar contra la abstracción sin depender de
    ninguna implementación específica.

    Estrategia de migración:
        Rama antigua : JsonReaderProcedural  (versión 1.0, TP6)
        Rama nueva   : JsonReaderSingleton   (versión 1.1, TP7)
        Cliente      : main() — depende solo de IJsonReader
    """

    @abstractmethod
    def get_value(self, jsonfile: str, jsonkey: str = DEFAULT_KEY) -> str:
        """
        Retorna el valor asociado a jsonkey en el archivo jsonfile.

        Args:
            jsonfile: Ruta al archivo JSON.
            jsonkey:  Clave a buscar (default: 'token1').

        Returns:
            El valor como string.

        Raises:
            FileNotFoundError   : Si el archivo no existe.
            json.JSONDecodeError: Si el JSON es inválido.
            KeyError            : Si la clave no existe en el JSON.
        """

    @abstractmethod
    def get_all_keys(self, jsonfile: str) -> list:
        """
        Retorna la lista de todas las claves presentes en el archivo JSON.

        Útil para validar que una clave solicitada existe antes de
        intentar recuperarla, o para descubrimiento de claves disponibles.

        Args:
            jsonfile: Ruta al archivo JSON.

        Returns:
            Lista de strings con los nombres de todas las claves.

        Raises:
            FileNotFoundError   : Si el archivo no existe.
            json.JSONDecodeError: Si el JSON es inválido.
        """


# ─── Rama antigua: implementación procedural (TP6) ───────────────────────────
class JsonReaderProcedural(IJsonReader):
    """
    Implementación procedural original de getJason (versión 1.0 / TP6).

    Conservada durante la transición Branching by Abstraction para
    garantizar la equivalencia funcional con la nueva implementación
    Singleton. Permite revertir con un único cambio en el punto de
    instanciación dentro de main().
    """

    def get_value(self, jsonfile: str, jsonkey: str = DEFAULT_KEY) -> str:
        """
        Lee el archivo JSON y retorna el valor de la clave indicada.

        Implementación original TP6 adaptada a la interfaz IJsonReader.
        Sin estado interno ni caché.

        Args:
            jsonfile: Ruta al archivo JSON.
            jsonkey:  Clave a buscar (default: 'token1').

        Returns:
            El valor como string.
        """
        with open(jsonfile, 'r', encoding='utf-8') as file_handle:
            raw_data = file_handle.read()
        parsed = json.loads(raw_data)
        return str(parsed[jsonkey])

    def get_all_keys(self, jsonfile: str) -> list:
        """
        Retorna todas las claves del archivo JSON.

        Args:
            jsonfile: Ruta al archivo JSON.

        Returns:
            Lista de strings con los nombres de todas las claves.
        """
        with open(jsonfile, 'r', encoding='utf-8') as file_handle:
            raw_data = file_handle.read()
        parsed = json.loads(raw_data)
        return list(parsed.keys())


# ─── Rama nueva: patrón Singleton (TP7) ──────────────────────────────────────
class JsonReaderSingleton(IJsonReader):
    """
    Lector de archivos JSON implementado con el patrón de diseño Singleton.

    Garantiza que exista una única instancia de la clase durante toda
    la ejecución del programa. Relevante en entornos de alta concurrencia
    o cuando la construcción del objeto resulta costosa.

    Patrón: Singleton (Gang of Four — Creational Patterns)
    Implementado mediante sobreescritura de __new__ para interceptar
    la creación de instancias y retornar siempre la misma referencia.

    Atributos de clase:
        _instance: Referencia a la única instancia (None hasta el primer __new__).
    """

    _instance = None  # Almacena la única instancia permitida por el patrón

    def __new__(cls):
        """
        Controla la creación de instancias: crea solo una vez.

        Si _instance es None (primera llamada), crea la instancia y la
        almacena. En llamadas sucesivas retorna la instancia existente.

        Returns:
            La única instancia de JsonReaderSingleton.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_value(self, jsonfile: str, jsonkey: str = DEFAULT_KEY) -> str:
        """
        Lee el archivo JSON y retorna el valor de la clave indicada.

        Implementación activa en la versión 1.1. Funcionalmente equivalente
        a JsonReaderProcedural pero ejecutada sobre la instancia Singleton,
        lo que permite agregar estado compartido (caché, logging, métricas)
        en futuras versiones sin cambiar la interfaz pública.

        Args:
            jsonfile: Ruta al archivo JSON.
            jsonkey:  Clave a buscar (default: 'token1').

        Returns:
            El valor como string.
        """
        with open(jsonfile, 'r', encoding='utf-8') as file_handle:
            raw_data = file_handle.read()
        parsed = json.loads(raw_data)
        return str(parsed[jsonkey])

    def get_all_keys(self, jsonfile: str) -> list:
        """
        Retorna todas las claves del archivo JSON.

        Args:
            jsonfile: Ruta al archivo JSON.

        Returns:
            Lista de strings con los nombres de todas las claves.
        """
        with open(jsonfile, 'r', encoding='utf-8') as file_handle:
            raw_data = file_handle.read()
        parsed = json.loads(raw_data)
        return list(parsed.keys())


# ─── Funciones auxiliares ─────────────────────────────────────────────────────
def print_usage():
    """Imprime el mensaje de uso correcto del programa en stderr."""
    print(
        "Uso: python3 getJason.py <archivo_json> [clave]\n"
        "     python3 getJason.py -v\n"
        "Ejemplo: python3 getJason.py sitedata.json token1",
        file=sys.stderr
    )


def validate_args(args):
    """
    Valida y parsea los argumentos de línea de comandos.

    Controla que los argumentos sean correctos antes de invocar cualquier
    lógica de negocio, garantizando que errores de uso produzcan mensajes
    descriptivos y códigos de salida controlados, sin excepciones sin capturar.

    Args:
        args: Lista de strings con los argumentos recibidos (sys.argv[1:]).

    Returns:
        Tupla (jsonfile, jsonkey). jsonfile puede ser '-v' para indicar
        solicitud de versión, o None si los argumentos son inválidos.
    """
    if not args:
        return None, None

    first_arg = args[0]

    # Solicitud de versión
    if first_arg == '-v':
        return '-v', None

    # Flag desconocido
    if first_arg.startswith('-'):
        return None, None

    jsonfile = first_arg
    jsonkey = args[1] if len(args) >= 2 else DEFAULT_KEY
    return jsonfile, jsonkey


# ─── Punto de entrada ─────────────────────────────────────────────────────────
def main():
    """
    Punto de entrada principal del programa.

    Parsea y valida los argumentos de ejecución, instancia el lector
    JSON activo mediante la abstracción IJsonReader, y gestiona todos
    los errores de forma controlada. El programa nunca termina con una
    excepción no capturada: todo error se convierte en un mensaje
    descriptivo en stderr y un código de salida numérico documentado.

    Branching by Abstraction:
        La variable 'reader' es de tipo IJsonReader. Para alternar entre
        implementaciones basta cambiar la clase instanciada en una sola
        línea sin modificar ninguna otra parte del código cliente.
    """
    jsonfile, jsonkey = validate_args(sys.argv[1:])

    # Modo versión: emitir y terminar limpiamente
    if jsonfile == '-v':
        print(f"getJason versión {VERSION}")
        sys.exit(EXIT_OK)

    # Argumentos insuficientes o inválidos
    if jsonfile is None:
        print_usage()
        sys.exit(EXIT_USAGE)

    # ── Branching by Abstraction: punto de selección de implementación ──────
    # Para activar la rama antigua (TP6): reader = JsonReaderProcedural()
    # Para activar la rama nueva  (TP7): reader = JsonReaderSingleton()
    reader = JsonReaderSingleton()          # Implementación activa: v1.1
    # ─────────────────────────────────────────────────────────────────────────

    try:
        print(reader.get_value(jsonfile, jsonkey))

    except FileNotFoundError:
        print(
            f"Error [2]: archivo '{jsonfile}' no encontrado.",
            file=sys.stderr
        )
        sys.exit(EXIT_FILE)

    except json.JSONDecodeError as exc:
        print(
            f"Error [3]: JSON inválido en '{jsonfile}': {exc}",
            file=sys.stderr
        )
        sys.exit(EXIT_JSON)

    except KeyError:
        print(
            f"Error [4]: clave '{jsonkey}' no existe en '{jsonfile}'.",
            file=sys.stderr
        )
        sys.exit(EXIT_KEY)


if __name__ == '__main__':
    main()