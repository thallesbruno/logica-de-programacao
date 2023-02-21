import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 2), 4)
    
    def test_soma_negativos(self):
        self.assertEqual(soma(-2, -2), -4)
    
    def test_soma_positivo_negativo(self):
        self.assertEqual(soma(2, -2), 0)

if __name__ == "__main__":
    unittest.main()