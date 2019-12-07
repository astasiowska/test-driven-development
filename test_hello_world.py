import unittest
import hello_world

class TestTDD2(unittest.TestCase):
    def test_zwroc_tekst(self):
        wynik = hello_world.zwroc_tekst()
        self.assertEqual(wynik, "Hello World")



if __name__ == '__main__':
    unittest.main()
