import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_dodaj(self):
        wynik = calculator.dodaj(1, 3)
        self.assertEqual(wynik, 4)

    def test_odejmij(self):
        wynik = calculator.odejmij(10, 6)
        self.assertEqual(wynik, 4)

    def test_pomnoz(self):
        wynik = calculator.pomnoz(10, 6)
        self.assertEqual(wynik, 60)

    def test_podziel(self):
        wynik = calculator.podziel(10, 5)
        self.assertEqual(wynik, 2)




if __name__ == '__main__':
    unittest.main()
