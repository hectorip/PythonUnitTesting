# -*- coding: utf-8 -*-

import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculate_iva(self):

        result = self.calc.get_iva(100) # 16
        result2 = self.calc.get_iva(200) # 32
        result3 = self.calc.get_iva(500)  # 80
        result4 = self.calc.get_iva(1000)  # 80

        self.assertEqual(result, 16)
        self.assertEqual(result2, 32)
        self.assertEqual(result3, 80)
        self.assertEqual(result4, 160)

    def test_calculate_iva_with_different_rate(self):

        result = self.calc.get_iva(100, rate=.20)

        self.assertEqual(result, 20)

    def test_calculate_interest(self):
        """
        Prueba una función que calcula el interés,
        recibiendo monto inicial, tasa de interés y periodos
        (interés simple)
        is = (mi * ir) * np 
        """

        result = self.calc.calculate_interest(100, .10, 1)
        self.assertEqual(result, 10)

        result = self.calc.calculate_interest(1000, .10, 10)
        self.assertEqual(result, 1000)

        result = self.calc.calculate_interest(500, .25, 10)
        self.assertEqual(result, 1250)

    def test_calculate_compound_interest(self):

        result = self.calc.calculate_interest(1000, .10, 10, compound=True)
        self.assertAlmostEqual(result, 1593.74)

        result = self.calc.calculate_interest(1000, .10, 1, compound=True)
        self.assertAlmostEqual(result, 100)

    """
    calcular inversion
    100, .10, 10, 100

    100 * interest_rate + 100
    210 * interest_rate + 100
    310 * interes_rate + 100


    Recibie inversión inicial, interest_rate, monto_mensual,
    periodos
    """

if __name__ == '__main__':
    unittest.main()
