from enigma.rotor import Rotor
import unittest

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
        self.assertEqual(rotor.transform('A'), 'A')
        self.assertEqual(rotor.transform('A'), 'B')
        self.assertEqual(rotor.transform('A'), 'C')
        self.assertEqual(rotor.transform('A'), 'D')

    def test_offset_1_rotor(self):
        rotor = Rotor(offset=1, period=4)
        self.assertEqual(rotor.transform('A'), 'B')
        self.assertEqual(rotor.transform('B'), 'C')
        self.assertEqual(rotor.transform('C'), 'D')
        self.assertEqual(rotor.transform('D'), 'E')
        self.assertEqual(rotor.transform('E'), 'G')

    def test_offset_1_period_1(self):
        rotor = Rotor(offset=1, period=1)
        self.assertEqual(rotor.transform('A'), 'B')
        self.assertEqual(rotor.transform('B'), 'D')
        self.assertEqual(rotor.transform('C'), 'F')
        self.assertEqual(rotor.transform('D'), 'H')

    def test_invalid_char_error(self):
        rotor = Rotor(offset=1, period=1)
        with self.assertRaises(AssertionError):
            rotor.transform('a')

    def test_full_offset_rotation(self):
        rotor = Rotor(offset=0, period=1)
        for num in range(ord('Z')-ord('A')+1):
            self.assertEqual(rotor.transform('A'), chr(num+ord('A')))
        self.assertEqual(rotor.transform('A'), 'A')

    def test_rotor_reset(self):
        rotor = Rotor(offset=1, period=1)
        self.assertEqual(rotor.transform('A'), 'B')
        self.assertEqual(rotor.transform('B'), 'D')
        self.assertEqual(rotor.transform('C'), 'F')
        self.assertEqual(rotor.transform('D'), 'H')
        rotor.reset()
        self.assertEqual(rotor.transform('A'), 'B')
        self.assertEqual(rotor.transform('B'), 'D')
        self.assertEqual(rotor.transform('C'), 'F')
        self.assertEqual(rotor.transform('D'), 'H')

    def test_rotor_reset_and_inverse_transform(self):
        rotor = Rotor(offset=1, period=1)
        self.assertEqual(rotor.transform('A'), 'B')
        self.assertEqual(rotor.transform('B'), 'D')
        self.assertEqual(rotor.transform('C'), 'F')
        self.assertEqual(rotor.transform('D'), 'H')
        rotor.reset()
        self.assertEqual(rotor.inverse_transform('B'), 'A')
        self.assertEqual(rotor.inverse_transform('D'), 'B')
        self.assertEqual(rotor.inverse_transform('F'), 'C')
        self.assertEqual(rotor.inverse_transform('H'), 'D')

