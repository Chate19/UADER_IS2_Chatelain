#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name   # nombre 'getJason' impuesto por enunciado TP6/TP7/TP8
"""
################################################################################
# copyright UADER-FCyT-IS2©2024 todos los derechos reservados
################################################################################
#
# Módulo  : getJason.py
# Versión : 1.2
# Autor   : UADER-FCyT-IS2
#
# Descripción:
#   TP6/TP7: Recupera valores desde un archivo JSON (token1/token2) mediante
#            un lector Singleton (JsonReaderSingleton) con Branching by
#            Abstraction respecto a la implementación procedural original.
#
#   TP8 (Re-Ingeniería): Se incorpora un sistema automático de ruteo de
#            pagos bancarios que reutiliza el objeto Singleton para
#            recuperar la credencial ("clave") de cada banco (token) en
#            el momento en que ese banco es seleccionado para cubrir un
#            pago. La selección automática de cuenta se implementa con
#            el patrón "Cadena de Responsabilidad" (Chain of Responsibility),
#            que es el patrón GoF correspondiente a lo que el enunciado
#            del TP8 describe como "cadena de comando": una solicitud
#            que recorre una cadena de manejadores hasta que uno de ellos
#            la satisface (cuenta con saldo suficiente). El listado
#            cronológico de pagos se expone mediante el patrón Iterator.
#
# Uso (modo TP6/TP7 - recuperación de tokens):
#   python3 getJason.py <archivo_json> [clave]
#   python3 getJason.py -v
#
# Uso (modo TP8 - demostración del ruteo de pagos):
#   python3 getJason.py -pagos [archivo_json]
#
# Códigos de salida:
#   0 : Éxito
#   1 : Error de uso / argumentos incorrectos
#   2 : Archivo no encontrado
#   3 : JSON inválido
#   4 : Clave no encontrada en el JSON
#
################################################################################
"""

import json
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime

# ─── Constantes del módulo ────────────────────────────────────────────────────
VERSION = "1.2"
DEFAULT_KEY = "token1"
EXIT_OK = 0
EXIT_USAGE = 1
EXIT_FILE = 2
EXIT_JSON = 3
EXIT_KEY = 4

PAYMENT_DEMO_REQUEST_COUNT = 7
PAYMENT_DEMO_AMOUNT = 500.0
INITIAL_BALANCES: dict[str, float] = {"token1": 1000.0, "token2": 2000.0}


# ════════════════════════════════════════════════════════════════════════════
# SECCIÓN 1 — Lectura de JSON: IJsonReader, Procedural y Singleton (TP6/TP7)
# ════════════════════════════════════════════════════════════════════════════
class IJsonReader(ABC):
    """
    Interfaz abstracta para lectores de archivos JSON.

    Define el contrato que deben cumplir todas las implementaciones
    concretas. Es el punto central de la estrategia Branching by
    Abstraction introducida en TP7. En TP8 esta misma abstracción se
    inyecta también en la Cadena de Responsabilidad de pagos
    (ConcreteAccountHandler), reutilizando sin cambios el mecanismo de
    recuperación de credenciales bancarias.
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
    def get_all_keys(self, jsonfile: str) -> list[str]:
        """
        Retorna la lista de todas las claves presentes en el archivo JSON.

        Args:
            jsonfile: Ruta al archivo JSON.

        Returns:
            Lista de strings con los nombres de todas las claves.
        """


class JsonReaderProcedural(IJsonReader):
    """
    Implementación procedural original de getJason (versión 1.0 / TP6).

    Conservada como rama antigua de Branching by Abstraction. Cualquier
    componente que dependa de IJsonReader (incluyendo la Cadena de
    Responsabilidad de TP8) puede recibir esta implementación en lugar
    de JsonReaderSingleton sin modificar su propio código.
    """

    def get_value(self, jsonfile: str, jsonkey: str = DEFAULT_KEY) -> str:
        """Lee el archivo JSON y retorna el valor de la clave indicada."""
        with open(jsonfile, 'r', encoding='utf-8') as file_handle:
            raw_data = file_handle.read()
        parsed = json.loads(raw_data)
        return str(parsed[jsonkey])

    def get_all_keys(self, jsonfile: str) -> list[str]:
        """Retorna todas las claves del archivo JSON."""
        with open(jsonfile, 'r', encoding='utf-8') as file_handle:
            raw_data = file_handle.read()
        parsed = json.loads(raw_data)
        return list(parsed.keys())


class JsonReaderSingleton(IJsonReader):
    """
    Lector de archivos JSON implementado con el patrón de diseño Singleton.

    Garantiza una única instancia durante toda la ejecución del programa.
    En TP8 es la implementación activa inyectada en cada
    ConcreteAccountHandler, de modo que la recuperación de la credencial
    bancaria ("clave") ocurre siempre a través del mismo punto de acceso
    centralizado, sin importar cuántas cuentas o manejadores existan.

    Atributos de clase:
        _instance: Referencia a la única instancia (None hasta el primer __new__).
    """

    _instance: "JsonReaderSingleton | None" = None

    def __new__(cls) -> "JsonReaderSingleton":
        """Crea la instancia solo una vez; llamadas sucesivas la reutilizan."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_value(self, jsonfile: str, jsonkey: str = DEFAULT_KEY) -> str:
        """Lee el archivo JSON y retorna el valor de la clave indicada."""
        with open(jsonfile, 'r', encoding='utf-8') as file_handle:
            raw_data = file_handle.read()
        parsed = json.loads(raw_data)
        return str(parsed[jsonkey])

    def get_all_keys(self, jsonfile: str) -> list[str]:
        """Retorna todas las claves del archivo JSON."""
        with open(jsonfile, 'r', encoding='utf-8') as file_handle:
            raw_data = file_handle.read()
        parsed = json.loads(raw_data)
        return list(parsed.keys())


# ════════════════════════════════════════════════════════════════════════════
# SECCIÓN 2 — Objetos de dominio del sistema de pagos (TP8)
# ════════════════════════════════════════════════════════════════════════════
@dataclass
class Account:
    """
    Representa una cuenta bancaria asociada a un token (banco).

    Attributes:
        token:   Nombre del token/banco (clave en sitedata.json), ej. 'token1'.
        balance: Saldo disponible en la cuenta.
    """

    token: str
    balance: float

    def has_sufficient_funds(self, amount: float) -> bool:
        """Indica si la cuenta tiene saldo suficiente para cubrir amount."""
        return self.balance >= amount

    def debit(self, amount: float) -> None:
        """
        Debita amount del saldo de la cuenta.

        Args:
            amount: Monto a debitar.

        Raises:
            ValueError: Si amount supera el saldo disponible.
        """
        if amount > self.balance:
            raise ValueError(
                f"Saldo insuficiente en cuenta '{self.token}': "
                f"disponible ${self.balance:.2f}, solicitado ${amount:.2f}."
            )
        self.balance -= amount


@dataclass(frozen=True)
class PaymentRequest:
    """
    Representa una solicitud de pago entrante.

    Attributes:
        order_number: Número de pedido (entero positivo).
        amount:       Monto solicitado (debe ser positivo).
    """

    order_number: int
    amount: float

    def __post_init__(self) -> None:
        """Valida los datos de la solicitud al construirla."""
        if self.order_number <= 0:
            raise ValueError("El número de pedido debe ser positivo.")
        if self.amount <= 0:
            raise ValueError("El monto del pago debe ser positivo.")

    def describe(self) -> str:
        """Retorna una descripción legible de la solicitud."""
        return f"Pedido #{self.order_number} por ${self.amount:.2f}"


@dataclass(frozen=True)
class PaymentRecord:
    """
    Representa el resultado de procesar una PaymentRequest.

    Attributes:
        order_number:       Número de pedido procesado.
        token:              Token/banco utilizado (None si fue rechazado).
        amount:             Monto del pago.
        status:             'OK' o 'RECHAZADO'.
        masked_credential:  Credencial bancaria enmascarada (None si rechazado).
        timestamp:          Momento en que se generó el registro.
    """

    order_number: int
    token: str | None
    amount: float
    status: str
    masked_credential: str | None
    timestamp: datetime = field(default_factory=datetime.now)

    def is_successful(self) -> bool:
        """Indica si el pago fue efectivamente cubierto por alguna cuenta."""
        return self.status == "OK"

    def __str__(self) -> str:
        hora = self.timestamp.strftime("%H:%M:%S")
        token_str = self.token if self.token else "-"
        clave_str = self.masked_credential if self.masked_credential else "-"
        return (
            f"Pedido #{self.order_number:>2} | Token: {token_str:<8} | "
            f"Monto: ${self.amount:>7.2f} | Estado: {self.status:<10} | "
            f"Clave: {clave_str:<10} | Hora: {hora}"
        )


# ════════════════════════════════════════════════════════════════════════════
# SECCIÓN 3 — Cadena de Responsabilidad ("cadena de comando" del enunciado)
# ════════════════════════════════════════════════════════════════════════════
class AccountHandler(ABC):
    """
    Manejador abstracto de la Cadena de Responsabilidad para el ruteo
    automático de pagos (puntos b, c y d del TP8).

    Nota de diseño: el enunciado denomina a este patrón "cadena de
    comando". El patrón GoF que implementa exactamente esta lógica
    -una solicitud que recorre una cadena de manejadores hasta que
    uno de ellos la satisface- es "Chain of Responsibility" (Cadena
    de Responsabilidad), por lo que se adopta ese nombre técnico
    estándar para la implementación, preservando el comportamiento
    solicitado.

    Cada manejador concreto evalúa si puede cubrir una PaymentRequest;
    si no puede, delega automáticamente al siguiente manejador de la
    cadena, lo que materializa el punto (b): la decisión de qué banco
    usar se automatiza en función del saldo disponible.
    """

    def __init__(self) -> None:
        self._next_handler: "AccountHandler | None" = None

    def set_next(self, handler: "AccountHandler") -> "AccountHandler":
        """Encadena el siguiente manejador y lo retorna (permite chaining)."""
        self._next_handler = handler
        return handler

    def delegate(self, request: PaymentRequest) -> PaymentRecord | None:
        """Delega request al siguiente manejador, o retorna None si no hay más."""
        if self._next_handler is not None:
            return self._next_handler.handle(request)
        return None

    @abstractmethod
    def handle(self, request: PaymentRequest) -> PaymentRecord | None:
        """Intenta procesar request; si no puede, delega al siguiente."""


class ConcreteAccountHandler(AccountHandler):
    """
    Manejador concreto de la cadena: intenta cubrir el pago debitando
    la cuenta bancaria que administra.

    Integra el patrón Singleton (vía IJsonReader inyectado) para
    recuperar la credencial ("clave") del banco en el momento exacto
    en que se decide usar esa cuenta (punto c del TP8): la selección
    de cuenta y la recuperación de su credencial ocurren de forma
    automática y conjunta ante cada solicitud de pago.
    """

    def __init__(self, account: Account, reader: IJsonReader, jsonfile: str) -> None:
        super().__init__()
        self._account = account
        self._reader = reader
        self._jsonfile = jsonfile

    def handle(self, request: PaymentRequest) -> PaymentRecord | None:
        """
        Procesa request si la cuenta administrada tiene saldo suficiente.

        Si no tiene saldo suficiente, delega al siguiente manejador de
        la cadena (o retorna None si no hay más manejadores, indicando
        que ninguna cuenta pudo cubrir la solicitud).
        """
        if self._account.has_sufficient_funds(request.amount):
            credential = self._reader.get_value(self._jsonfile, self._account.token)
            self._account.debit(request.amount)
            return PaymentRecord(
                order_number=request.order_number,
                token=self._account.token,
                amount=request.amount,
                status="OK",
                masked_credential=self._mask(credential),
            )
        return self.delegate(request)

    @staticmethod
    def _mask(credential: str) -> str:
        """Enmascara una credencial dejando visibles solo los últimos 4 caracteres."""
        return f"****-{credential[-4:]}" if len(credential) >= 4 else "****"


# ════════════════════════════════════════════════════════════════════════════
# SECCIÓN 4 — Patrón Iterator: listado cronológico de pagos
# ════════════════════════════════════════════════════════════════════════════
class PaymentLedgerIterator:
    """
    Iterador concreto (patrón Iterator / GoF) sobre los registros de
    PaymentLedger, recorridos en orden cronológico de inserción.
    """

    def __init__(self, records: list[PaymentRecord]) -> None:
        self._records = records
        self._index = 0

    def __iter__(self) -> "PaymentLedgerIterator":
        return self

    def __next__(self) -> PaymentRecord:
        if self._index >= len(self._records):
            raise StopIteration
        record = self._records[self._index]
        self._index += 1
        return record

    def remaining(self) -> int:
        """Cantidad de registros aún no recorridos por este iterador."""
        return len(self._records) - self._index


class PaymentLedger:
    """
    Colección de PaymentRecord que materializa el patrón Iterator (GoF)
    para recorrer los pagos realizados en orden cronológico (punto e).
    """

    def __init__(self) -> None:
        self._records: list[PaymentRecord] = []

    def add(self, record: PaymentRecord) -> None:
        """Agrega un nuevo registro de pago al final del historial."""
        self._records.append(record)

    def __iter__(self) -> PaymentLedgerIterator:
        """Retorna un iterador (patrón Iterator) sobre los registros."""
        return PaymentLedgerIterator(self._records)

    def listado(self) -> None:
        """Imprime todos los pagos realizados, en orden cronológico."""
        for record in self:
            print(record)


# ════════════════════════════════════════════════════════════════════════════
# SECCIÓN 5 — PaymentRouter: el "nuevo componente" del punto (c)
# ════════════════════════════════════════════════════════════════════════════
class PaymentRouter:
    """
    Componente orquestador que integra JsonReaderSingleton con la Cadena
    de Responsabilidad de cuentas para automatizar la selección del
    banco desde el que se efectúa cada pago (puntos b y c del TP8).

    Mantiene las cuentas token1 ($1000 inicial) y token2 ($2000 inicial)
    y alterna cuál de ellas encabeza la cadena en cada solicitud,
    logrando una distribución balanceada de los pagos (punto b) sin
    perder el control de saldo suficiente que aporta la cadena (punto d).
    """

    def __init__(self, jsonfile: str, reader: IJsonReader | None = None) -> None:
        self._jsonfile = jsonfile
        self._reader: IJsonReader = reader if reader is not None else JsonReaderSingleton()
        self._accounts: dict[str, Account] = {
            token: Account(token, balance)
            for token, balance in INITIAL_BALANCES.items()
        }
        self._ledger = PaymentLedger()
        self._turn = 0

    def _build_chain(self) -> AccountHandler:
        """Construye la cadena de manejadores alternando el punto de entrada."""
        order = ["token1", "token2"] if self._turn == 0 else ["token2", "token1"]
        handlers = [
            ConcreteAccountHandler(self._accounts[token], self._reader, self._jsonfile)
            for token in order
        ]
        for current, nxt in zip(handlers, handlers[1:]):
            current.set_next(nxt)
        return handlers[0]

    def process_payment(self, order_number: int, amount: float) -> PaymentRecord:
        """
        Procesa una solicitud de pago, ruteándola automáticamente a la
        cuenta correspondiente según saldo disponible y balanceo de uso.

        Args:
            order_number: Número de pedido (entero positivo).
            amount:       Monto del pago (debe ser positivo).

        Returns:
            PaymentRecord con el número de pedido, el token utilizado y
            el monto del pago realizado (salida de la clase, punto e),
            con estado 'OK' o 'RECHAZADO' si ninguna cuenta alcanzaba.
        """
        request = PaymentRequest(order_number, amount)
        chain_head = self._build_chain()
        self._turn = 1 - self._turn
        record = chain_head.handle(request)
        if record is None:
            record = PaymentRecord(
                order_number=order_number,
                token=None,
                amount=amount,
                status="RECHAZADO",
                masked_credential=None,
            )
        self._ledger.add(record)
        return record

    def listado(self) -> None:
        """Muestra todos los pagos realizados, en orden cronológico."""
        self._ledger.listado()

    def balances(self) -> dict[str, float]:
        """Retorna una copia de los saldos actuales de cada cuenta."""
        return {token: acc.balance for token, acc in self._accounts.items()}


# ════════════════════════════════════════════════════════════════════════════
# SECCIÓN 6 — Funciones auxiliares de CLI (TP6/TP7)
# ════════════════════════════════════════════════════════════════════════════
def print_usage() -> None:
    """Imprime el mensaje de uso correcto del programa en stderr."""
    print(
        "Uso: python3 getJason.py <archivo_json> [clave]\n"
        "     python3 getJason.py -v\n"
        "     python3 getJason.py -pagos [archivo_json]\n"
        "Ejemplo: python3 getJason.py sitedata.json token1",
        file=sys.stderr
    )


def validate_args(args: list[str]) -> tuple[str | None, str | None]:
    """
    Valida y parsea los argumentos de línea de comandos (modo TP6/TP7).

    Args:
        args: Lista de strings con los argumentos (sys.argv[1:]).

    Returns:
        Tupla (jsonfile, jsonkey). jsonfile puede ser '-v' para indicar
        solicitud de versión, o None si los argumentos son inválidos.
    """
    if not args:
        return None, None

    first_arg = args[0]

    if first_arg == '-v':
        return '-v', None

    if first_arg.startswith('-'):
        return None, None

    jsonfile = first_arg
    jsonkey = args[1] if len(args) >= 2 else DEFAULT_KEY
    return jsonfile, jsonkey


def run_payment_demo(jsonfile: str) -> None:
    """
    Ejecuta una demostración del sistema de ruteo de pagos (TP8, punto e).

    Genera PAYMENT_DEMO_REQUEST_COUNT solicitudes de PAYMENT_DEMO_AMOUNT
    cada una, las procesa a través de PaymentRouter (que las rutea
    automáticamente alternando entre token1 y token2 según saldo
    disponible), imprime cada resultado a medida que ocurre y finalmente
    exhibe el listado cronológico completo (patrón Iterator) junto con
    los saldos finales de cada cuenta.

    Args:
        jsonfile: Ruta al archivo JSON con las credenciales bancarias.
    """
    router = PaymentRouter(jsonfile)

    print(f"=== Demostración de ruteo de pagos (getJason v{VERSION}) ===")
    print(f"Saldos iniciales: {router.balances()}\n")

    for order_number in range(1, PAYMENT_DEMO_REQUEST_COUNT + 1):
        record = router.process_payment(order_number, PAYMENT_DEMO_AMOUNT)
        print(record)

    print("\n=== Listado cronológico (patrón Iterator) ===")
    router.listado()

    print(f"\nSaldos finales: {router.balances()}")


# ════════════════════════════════════════════════════════════════════════════
# SECCIÓN 7 — Punto de entrada
# ════════════════════════════════════════════════════════════════════════════
def main() -> None:
    """
    Punto de entrada principal del programa.

    Soporta tres modos de uso:
      1. Recuperación de tokens (TP6/TP7): getJason.py <archivo_json> [clave]
      2. Versión: getJason.py -v
      3. Demostración de pagos (TP8): getJason.py -pagos [archivo_json]

    El programa nunca termina con una excepción no capturada: todo
    error se convierte en un mensaje descriptivo en stderr y un código
    de salida numérico documentado.
    """
    args = sys.argv[1:]

    if args and args[0] == '-pagos':
        payment_jsonfile = args[1] if len(args) >= 2 else 'sitedata.json'
        run_payment_demo(payment_jsonfile)
        sys.exit(EXIT_OK)

    jsonfile, jsonkey = validate_args(args)

    if jsonfile == '-v':
        print(f"getJason versión {VERSION}")
        sys.exit(EXIT_OK)

    if jsonfile is None:
        print_usage()
        sys.exit(EXIT_USAGE)

    reader: IJsonReader = JsonReaderSingleton()   # Implementación activa: v1.2

    try:
        print(reader.get_value(jsonfile, jsonkey or DEFAULT_KEY))

    except FileNotFoundError:
        print(f"Error [2]: archivo '{jsonfile}' no encontrado.", file=sys.stderr)
        sys.exit(EXIT_FILE)

    except json.JSONDecodeError as exc:
        print(f"Error [3]: JSON inválido en '{jsonfile}': {exc}", file=sys.stderr)
        sys.exit(EXIT_JSON)

    except KeyError:
        print(f"Error [4]: clave '{jsonkey}' no existe en '{jsonfile}'.", file=sys.stderr)
        sys.exit(EXIT_KEY)


if __name__ == '__main__':
    main()