import unittest
import math
import sys
from io import StringIO
from unittest.mock import patch
from rpn import RPNCalculator, RPNError, main

class TestRPNCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = RPNCalculator()

    def test_arithmetic(self):
        self.assertEqual(self.calc.evaluate("3 4 +"), 7.0)
        self.assertEqual(self.calc.evaluate("2 3 4 * +"), 14.0)
        self.assertEqual(self.calc.evaluate("10 2 yx"), 100.0)
        self.assertEqual(self.calc.evaluate("5 chs"), -5.0)

    def test_trigonometry(self):
        self.assertAlmostEqual(self.calc.evaluate("90 sin"), 1.0)
        self.assertAlmostEqual(self.calc.evaluate("0 cos"), 1.0)
        self.assertAlmostEqual(self.calc.evaluate("1 asin"), 90.0)
        self.assertAlmostEqual(self.calc.evaluate("45 tg"), 1.0)
        self.assertAlmostEqual(self.calc.evaluate("1 atg"), 45.0)

    def test_math_functions(self):
        self.assertAlmostEqual(self.calc.evaluate("e ln"), 1.0)
        self.assertAlmostEqual(self.calc.evaluate("100 log"), 2.0)
        self.assertAlmostEqual(self.calc.evaluate("2 10x"), 100.0)
        self.assertAlmostEqual(self.calc.evaluate("16 sqrt"), 4.0)
        self.assertAlmostEqual(self.calc.evaluate("0.5 1/x"), 2.0)

    def test_stack_ops(self):
        self.assertEqual(self.calc.evaluate("1 2 swap drop"), 2.0)
        self.assertEqual(self.calc.evaluate("5 dup +"), 10.0)
        self.assertEqual(self.calc.evaluate("1 2 3 clear 5"), 5.0)

    def test_memory(self):
        self.assertEqual(self.calc.evaluate("42 sto 00"), 42.0)
        self.assertEqual(self.calc.evaluate("10 sto 01 drop rcl 01"), 10.0)

    def test_error_cases(self):
        cases = [
            ("3 0 /", "División por cero"),
            ("+", "insuficiente"),
            ("sto", "Falta argumento"),
            ("rcl 99", "Memoria inválida"),
            ("abc", "inválido"),
            ("1 2", "terminó con 2 elementos"),
            ("drop", "Pila vacía")
        ]
        for expr, msg in cases:
            with self.subTest(e=expr):
                try:
                    self.calc.evaluate(expr)
                except RPNError as e:
                    self.assertIn(msg, str(e))

    def test_main_execution(self):
        """Este test ejecuta el bloque main() para subir la cobertura al máximo."""
        # Simula: python rpn.py "3 4 +"
        with patch.object(sys, 'argv', ['rpn.py', '3', '4', '+']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main()
                self.assertEqual(fake_out.getvalue().strip(), "7")

        # Simula un error en el main: python rpn.py "3 0 /"
        with patch.object(sys, 'argv', ['rpn.py', '3', '0', '/']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                with self.assertRaises(SystemExit):
                    main()
                self.assertIn("Error", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()