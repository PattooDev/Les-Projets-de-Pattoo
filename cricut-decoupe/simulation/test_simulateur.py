import unittest
from simulateur import construire_trajet


class TestSimulation(unittest.TestCase):
    def test_parcours(self):
        resultat = construire_trajet([(0, 0), (10, 10)])
        self.assertEqual(len(resultat["commandes"]), 2)
        self.assertFalse(resultat["connexion_usb"])

    def test_limites(self):
        with self.assertRaises(ValueError):
            construire_trajet([(0, 0), (120, 0)])


if __name__ == "__main__":
    unittest.main()
