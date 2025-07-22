import unittest
import math
import calculator

class TestCalculatorScientific(unittest.TestCase):

    def test_potencia(self):
        self.assertAlmostEqual(calculator.potencia(2, 3), 8)
        self.assertAlmostEqual(calculator.potencia(5, 0), 1)
        self.assertAlmostEqual(calculator.potencia(4, 0.5), 2)

    def test_raiz(self):
        self.assertAlmostEqual(calculator.raiz(9), 3)
        self.assertAlmostEqual(calculator.raiz(27, 3), 3)
        with self.assertRaises(ValueError):
            calculator.raiz(-4, 2)  # raiz par de número negativo não permitida

    def test_logaritmo(self):
        self.assertAlmostEqual(calculator.logaritmo(math.e), 1)
        self.assertAlmostEqual(calculator.logaritmo(8, 2), 3)
        with self.assertRaises(ValueError):
            calculator.logaritmo(-1)
        with self.assertRaises(ValueError):
            calculator.logaritmo(10, 1)
        with self.assertRaises(ValueError):
            calculator.logaritmo(10, -2)

    def test_seno(self):
        self.assertAlmostEqual(calculator.seno(0), 0)
        self.assertAlmostEqual(calculator.seno(math.pi/2), 1)

    def test_cosseno(self):
        self.assertAlmostEqual(calculator.cosseno(0), 1)
        self.assertAlmostEqual(calculator.cosseno(math.pi), -1)

    def test_tangente(self):
        self.assertAlmostEqual(calculator.tangente(0), 0)
        # tangente de pi/4 é aproximadamente 1
        self.assertAlmostEqual(calculator.tangente(math.pi/4), 1, places=5)

if __name__ == '__main__':
    unittest.main()
