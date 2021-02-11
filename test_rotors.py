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
        self.assertEqual(rotor.forward('A', True)[0], 'B')
        self.assertEqual(rotor.forward('A', True)[0], 'C')
        self.assertEqual(rotor.forward('A', True)[0], 'D')
        self.assertEqual(rotor.forward('A', True)[0], 'E')

    def test_offset_1_rotor(self):
        rotor = Rotor(offset=1, period=4)
        self.assertEqual(rotor.forward('A', True)[0], 'B')
        self.assertEqual(rotor.forward('B', True)[0], 'C')
        self.assertEqual(rotor.forward('C', True)[0], 'D')
        self.assertEqual(rotor.forward('D', True)[0], 'F')
        self.assertEqual(rotor.forward('E', True)[0], 'G')

    def test_offset_1_period_1(self):
        rotor = Rotor(offset=1, period=1)
        self.assertEqual(rotor.forward('A', True)[0], 'C')
        self.assertEqual(rotor.forward('B', True)[0], 'E')
        self.assertEqual(rotor.forward('C', True)[0], 'G')
        self.assertEqual(rotor.forward('D', True)[0], 'I')

    def test_invalid_char_error(self):
        rotor = Rotor(offset=1, period=1)
        with self.assertRaises(AssertionError):
            rotor.forward('a', True)

    def test_full_offset_rotation(self):
        rotor = Rotor(offset=0, period=1)
        for num in range(1, ord('Z') - ord('A') + 1):
            self.assertEqual(rotor.forward('A', True)[0], chr(num + ord('A')))
        self.assertEqual(rotor.forward('A', True)[0], 'A')

    def test_rotor_reset(self):
        rotor = Rotor(offset=0, period=1)
        self.assertEqual(rotor.forward('A', True)[0], 'B')
        self.assertEqual(rotor.forward('B', True)[0], 'D')
        self.assertEqual(rotor.forward('C', True)[0], 'F')
        self.assertEqual(rotor.forward('D', True)[0], 'H')
        rotor.reset()
        self.assertEqual(rotor.forward('A', True)[0], 'B')
        self.assertEqual(rotor.forward('B', True)[0], 'D')
        self.assertEqual(rotor.forward('C', True)[0], 'F')
        self.assertEqual(rotor.forward('D', True)[0], 'H')

    def test_rotor_reset_and_inverse_transform(self):
        rotor = Rotor(offset=0, period=1)
        self.assertEqual(rotor.forward('A', True)[0], 'B')
        self.assertEqual(rotor.forward('B', True)[0], 'D')
        self.assertEqual(rotor.forward('C', True)[0], 'F')
        self.assertEqual(rotor.forward('D', True)[0], 'H')
        rotor.reset()
        rotor.forward('A', True)
        self.assertEqual(rotor.backward('B'), 'A')
        rotor.forward('B', True)
        self.assertEqual(rotor.backward('D'), 'B')
        rotor.forward('C', True)
        self.assertEqual(rotor.backward('F'), 'C')
        rotor.forward('D', True)
        self.assertEqual(rotor.backward('H'), 'D')

    def test_rotor_dont_step(self):
        rotor = Rotor(offset=0, period=1)
        self.assertEqual(rotor.forward('A')[0], 'A')
        self.assertEqual(rotor.forward('A')[0], 'A')
        self.assertEqual(rotor.forward('A')[0], rotor.forward('A')[0])

    def test_rotor_orders_to_step(self):
        rotor = Rotor(offset=0, period=1)
        for _ in range(25):
            _, do_step = rotor.forward('A', True)
            self.assertEqual(do_step, False)
        self.assertEqual(rotor.forward('A', True)[1], True)
