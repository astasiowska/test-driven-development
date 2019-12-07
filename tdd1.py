import unittest
import mojprogram

class TestTDD1(unittest.TestCase):
    def test_zwroc_100(self):
        wynik = mojprogram.zwroc_100()
        self.assertEqual(wynik, 100)

    def zwroc_parametr(self):
        self.assertEqual(mojprogram.zwroc_parametr(124), 124)


if __name__ == '__main__':
    unittest.main()