import unittest
import operacje_na_tekscie

class TestTDD3(unittest.TestCase):
    def test_capitalize(self):
        wynik = operacje_na_tekscie.capitalize("mala litera")
        self.assertEqual(wynik, "Mala litera")

    def test_lower(self):
        wynik = operacje_na_tekscie.lower("DUZA DUZA LITERA")
        self.assertEqual(wynik, "duza litera")

    def test_casefold(self):
        wynik = operacje_na_tekscie.casefold("Mala Litera")
        self.assertEqual(wynik, "mala litera")

    def test_upper(self):
        wynik = operacje_na_tekscie.upper("duza litera")
        self.assertEqual(wynik, "DUZA LITERA")

    def test_title(self):
        wynik = operacje_na_tekscie.title("mala litera")
        self.assertEqual(wynik, "Mala Litera")



if __name__ == '__main__':
    unittest.main()
