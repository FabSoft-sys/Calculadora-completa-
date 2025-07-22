import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_adicionar(self):
        self.assertEqual(calculator.adicionar(2, 3), 5)
        self.assertEqual(calculator.adicionar(-1, 1), 0)
        self.assertEqual(calculator.adicionar(0, 0), 0)

    def test_subtrair(self):
        self.assertEqual(calculator.subtrair(5, 3), 2)
        self.assertEqual(calculator.subtrair(0, 0), 0)
        self.assertEqual(calculator.subtrair(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(calculator.multiplicar(4, 3), 12)
        self.assertEqual(calculator.multiplicar(-1, 1), -1)
        self.assertEqual(calculator.multiplicar(0, 10), 0)

    def test_dividir(self):
        self.assertEqual(calculator.dividir(10, 2), 5)
        self.assertEqual(calculator.dividir(-6, 3), -2)
        with self.assertRaises(ValueError):
            calculator.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()
