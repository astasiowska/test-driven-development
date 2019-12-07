import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_dodaj(self):
        wynik = calculator.dodaj(1, 3)
        self.assertEqual(wynik, 4)

    def zwroc_parametr(self):
        self.assertEqual(mojprogram.zwroc_parametr(124), 124)


if __name__ == '__main__':
    unittest.main()
