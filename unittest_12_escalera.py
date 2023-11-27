import unittest
from test_12_escalera import tirar_dado
from test_12_escalera import sube
from test_12_escalera import baja

class TestJuegoEscalera(unittest.TestCase):

    def test_tirar_dado(self):
        dado_result = tirar_dado()
        self.assertTrue(1 <= dado_result <= 6)

    def test_sube(self):
        self.assertEqual(sube(3), 11)
        self.assertEqual(sube(6), 17)
        self.assertEqual(sube(9), 18)
        self.assertEqual(sube(10), 12)

    def test_baja(self):
        self.assertEqual(baja(14), 4)
        self.assertEqual(baja(19), 8)
        self.assertEqual(baja(22), 20)
        self.assertEqual(baja(24), 16)

if __name__ == '__main__':
    unittest.main()