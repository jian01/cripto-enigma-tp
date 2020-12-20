from enigma.plugboard import Plugboard
import unittest

class PlugboardUnitTests(unittest.TestCase):
    def test_empty_plugboard(self):
        plugboard = Plugboard()
        self.assertEqual(plugboard.transform('A'), 'A')
        self.assertEqual(plugboard.transform('Z'), 'Z')
        self.assertEqual(plugboard.transform('C'), 'C')

    def test_simple_plugboard(self):
        plugboard = Plugboard([('A', 'Z')])
        self.assertEqual(plugboard.transform('A'), 'Z')
        self.assertEqual(plugboard.transform('Z'), 'A')
        self.assertEqual(plugboard.transform('C'), 'C')

    def test_simple_inverse_transforms(self):
        plugboard = Plugboard([('A', 'Z')])
        self.assertEqual(plugboard.inverse_transform('A'), 'Z')
        self.assertEqual(plugboard.inverse_transform('Z'), 'A')
        self.assertEqual(plugboard.inverse_transform('C'), 'C')

    def test_plugboard_transform_to_the_same(self):
        plugboard = Plugboard([('A', 'A')])
        self.assertEqual(plugboard.transform('A'), 'A')
        self.assertEqual(plugboard.transform('Z'), 'Z')
        self.assertEqual(plugboard.transform('C'), 'C')

    def test_plugboard_double_wiring_error(self):
        with self.assertRaises(Exception):
            Plugboard([('A', 'C'), ('A', 'B')])

