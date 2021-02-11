import unittest

from enigma.rotors.rotor import Rotor


class RotorUnitTests(unittest.TestCase):
    def test_rotor_period_larger_than_0(self):
        with self.assertRaises(AssertionError):
            Rotor(offset=0, period=0)
        with self.assertRaises(AssertionError):
            Rotor(offset=0, period=-1)

    def test_rotor_offset_leq_than_0(self):
        with self.assertRaises(AssertionError):
            Rotor(offset=-1, period=1)

    def test_no_offset_rotor(self):
        rotor = Rotor(offset=0, period=1)
        self.assertEqual(rotor.backward('A'), 'A')
        self.assertEqual(rotor.forward('A'), 'B')
        self.assertEqual(rotor.forward('A'), 'C')
        self.assertEqual(rotor.forward('A'), 'D')
        self.assertEqual(rotor.forward('A'), 'E')

    def test_offset_1_rotor(self):
        rotor = Rotor(offset=1, period=4)
        self.assertEqual(rotor.forward('A'), 'B')
        self.assertEqual(rotor.forward('B'), 'C')
        self.assertEqual(rotor.forward('C'), 'D')
        self.assertEqual(rotor.forward('D'), 'F')
        self.assertEqual(rotor.forward('E'), 'G')

    def test_offset_1_period_1(self):
        rotor = Rotor(offset=1, period=1)
        self.assertEqual(rotor.forward('A'), 'C')
        self.assertEqual(rotor.forward('B'), 'E')
        self.assertEqual(rotor.forward('C'), 'G')
        self.assertEqual(rotor.forward('D'), 'I')

    def test_invalid_char_error(self):
        rotor = Rotor(offset=1, period=1)
        with self.assertRaises(AssertionError):
            rotor.forward('a')

    def test_full_offset_rotation(self):
        rotor = Rotor(offset=0, period=1)
        for num in range(1, ord('Z') - ord('A') + 1):
            self.assertEqual(rotor.forward('A'), chr(num + ord('A')))
        self.assertEqual(rotor.forward('A'), 'A')

    def test_rotor_reset(self):
        rotor = Rotor(offset=0, period=1)
        self.assertEqual(rotor.forward('A'), 'B')
        self.assertEqual(rotor.forward('B'), 'D')
        self.assertEqual(rotor.forward('C'), 'F')
        self.assertEqual(rotor.forward('D'), 'H')
        rotor.reset()
        self.assertEqual(rotor.forward('A'), 'B')
        self.assertEqual(rotor.forward('B'), 'D')
        self.assertEqual(rotor.forward('C'), 'F')
        self.assertEqual(rotor.forward('D'), 'H')

    def test_rotor_reset_and_inverse_transform(self):
        rotor = Rotor(offset=0, period=1)
        self.assertEqual(rotor.forward('A'), 'B')
        self.assertEqual(rotor.forward('B'), 'D')
        self.assertEqual(rotor.forward('C'), 'F')
        self.assertEqual(rotor.forward('D'), 'H')
        rotor.reset()
        rotor.forward('A')
        self.assertEqual(rotor.backward('B'), 'A')
        rotor.forward('B')
        self.assertEqual(rotor.backward('D'), 'B')
        rotor.forward('C')
        self.assertEqual(rotor.backward('F'), 'C')
        rotor.forward('D')
        self.assertEqual(rotor.backward('H'), 'D')
