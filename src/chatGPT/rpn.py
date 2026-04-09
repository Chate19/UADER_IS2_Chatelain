"""
Módulo rpn.py: Versión final con tipado moderno (Python 3.10+).
Cumple con todas las reglas UP (Pyupgrade) de Ruff y Pylint 10/10.
"""

import math
import sys
from collections.abc import Callable
from typing import NoReturn


class RPNError(Exception):
    """Excepción personalizada para errores lógicos de la calculadora RPN."""


# pylint: disable=too-few-public-methods
class RPNCalculator:
    """
    Calculadora RPN con arquitectura basada en despacho de funciones
    y gestión de memoria persistente.
    """

    def __init__(self) -> None:
        # En Python 3.9+ se usa 'list' y 'dict' directamente para tipos
        self.stack: list[float] = []
        self.mem: dict[str, float] = {f"{i:02d}": 0.0 for i in range(10)}
        self.consts: dict[str, float] = {
            "p": math.pi,
            "e": math.e,
            "j": (1 + 5**0.5) / 2,
        }
        self.ops: dict[str, Callable[[], None]] = self._initialize_operations()

    def _initialize_operations(self) -> dict[str, Callable[[], None]]:
        """Define y organiza el conjunto de instrucciones soportadas."""
        return {
            "+": lambda: self._op2(lambda a, b: a + b),
            "-": lambda: self._op2(lambda a, b: a - b),
            "*": lambda: self._op2(lambda a, b: a * b),
            "/": lambda: self._op2(self._div),
            "sqrt": lambda: self._op1(math.sqrt),
            "sin": lambda: self._op1(lambda x: math.sin(math.radians(x))),
            "cos": lambda: self._op1(lambda x: math.cos(math.radians(x))),
            "tg": lambda: self._op1(lambda x: math.tan(math.radians(x))),
            "yx": lambda: self._op2(lambda a, b: a**b),
            "1/x": lambda: self._op1(self._inv),
            "dup": self._dup,
            "swap": self._swap,
            "drop": self._drop,
            "clear": self._clear,
        }

    def _op1(self, func: Callable[[float], float]) -> None:
        """Aplica una función unaria."""
        if not self.stack:
            raise RPNError("Pila insuficiente")
        self.stack.append(float(func(self.stack.pop())))

    def _op2(self, func: Callable[[float, float], float]) -> None:
        """Aplica una función binaria."""
        if len(self.stack) < 2:
            raise RPNError("Pila insuficiente")
        val_b, val_a = self.stack.pop(), self.stack.pop()
        self.stack.append(float(func(val_a, val_b)))

    def _div(self, a: float, b: float) -> float:
        if b == 0:
            raise RPNError("División por cero")
        return a / b

    def _inv(self, x: float) -> float:
        if x == 0:
            raise RPNError("División por cero en 1/x")
        return 1 / x

    def _dup(self) -> None:
        if not self.stack:
            raise RPNError("Pila vacía")
        self.stack.append(self.stack[-1])

    def _swap(self) -> None:
        if len(self.stack) < 2:
            raise RPNError("Pila insuficiente")
        self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    def _drop(self) -> None:
        if not self.stack:
            raise RPNError("Pila vacía")
        self.stack.pop()

    def _clear(self) -> None:
        self.stack.clear()

    def evaluate(self, expression: str, clear_stack: bool = True) -> float:
        """Procesa una cadena RPN y retorna el tope de la pila."""
        if clear_stack:
            self.stack.clear()

        expr = expression.lower().replace("sto", "sto ").replace("rcl", "rcl ")
        it = iter(expr.split())
        for token in it:
            try:
                if token in self.ops:
                    self.ops[token]()
                elif token in self.consts:
                    self.stack.append(self.consts[token])
                elif token in ("sto", "rcl"):
                    reg = next(it)
                    if reg not in self.mem:
                        raise RPNError(f"Registro inválido: {reg}")
                    if token == "sto":
                        if not self.stack:
                            raise RPNError("Pila vacía para sto")
                        self.mem[reg] = self.stack[-1]
                    else:
                        self.stack.append(self.mem[reg])
                else:
                    self.stack.append(float(token))
            except RPNError:
                raise
            except (ValueError, KeyError):
                raise RPNError(f"Token desconocido: {token}") from None
            except StopIteration:
                raise RPNError(f"Falta registro para {token}") from None

        if not self.stack:
            raise RPNError("La pila está vacía.")
        return self.stack[-1]


def run_repl(calc: RPNCalculator) -> None:
    """Inicia el modo interactivo (REPL) con visualización de pila."""
    print("Calculadora RPN (Modo Interactivo). Escriba 'exit' para salir.")
    while True:
        try:
            line = input(f"Stack {calc.stack} > ").strip()
            if line.lower() in ("exit", "quit"):
                break
            if line:
                res = calc.evaluate(line, clear_stack=False)
                print(f"Resultado parcial: {res:g}")
        except RPNError as err:
            print(f"Error: {err}")
        except EOFError:
            break


def main() -> NoReturn | None:
    """
    Punto de entrada principal.
    Usa la sintaxis 'Type | None' de Python 3.10.
    """
    calc = RPNCalculator()
    if len(sys.argv) > 1:
        try:
            input_str = " ".join(sys.argv[1:])
            print(f"{calc.evaluate(input_str):g}")
        except Exception as err:  # pylint: disable=broad-except
            print(f"Error: {err}")
            sys.exit(1)
    else:
        run_repl(calc)
    return None


if __name__ == "__main__":
    main()
