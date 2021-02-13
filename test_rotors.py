import unittest

from enigma.rotors.rotor import Rotor
from enigma.rotors.rotor_I import RotorI
from enigma.rotors.rotor_with_mapping_and_notches import RotorWithMappingAndNotches


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

    def test_rotor_with_mapping_and_notches(self):
        rotor_mapping = {chr(ord('A') + i): chr(ord('A') + i)
                         for i in range(26)
                         if chr(ord('A') + i) not in ['A', 'F']}
        rotor_mapping['A'] = 'F'
        rotor_mapping['F'] = 'A'
        rotor = RotorWithMappingAndNotches(offset=0, period=1,
                                           rotor_mapping=rotor_mapping,
                                           notches={'A', 'F'})
        self.assertEqual(rotor.forward('A'), ('F', False))  # offset A
        self.assertEqual(rotor.forward('A', True), ('A', True))  # off: B
        self.assertEqual(rotor.forward('F', True), ('F', False))  # off: C
        self.assertEqual(rotor.forward('A', True), ('A', False))  # off: D
        self.assertEqual(rotor.forward('A', True), ('A', False))  # off: E
        self.assertEqual(rotor.forward('A', True), ('V', False))  # off: F
        self.assertEqual(rotor.forward('A', False), ('V', False))  # off: F
        self.assertEqual(rotor.forward('A', True), ('A', True))  # off: G

    def test_rotorI(self):
        rotor = RotorI()
        self.assertEqual(rotor.forward('A'), ('E', False))  # offset A
        self.assertEqual(rotor.backward('E'), 'A')  # offset A
        self.assertEqual(rotor.forward('Q', True), ('T', False))  # offset B
        self.assertEqual(rotor.forward('B', True), ('D', False))  # offset C
        self.assertEqual(rotor.forward('C', True), ('D', False))  # offset D or 3
        self.assertEqual(rotor.forward('D', True), ('M', False))  # offset 4
        self.assertEqual(rotor.forward('E', True), ('U', False))  # offset 5
        self.assertEqual(rotor.forward('F', True), ('N', False))  # offset 6
        self.assertEqual(rotor.forward('G', True), ('P', False))  # offset 7
        self.assertEqual(rotor.forward('H', True), ('Z', False))  # offset 8
        self.assertEqual(rotor.forward('I', True), ('L', False))  # offset 9
        self.assertEqual(rotor.forward('J', True), ('F', False))  # offset 10
        self.assertEqual(rotor.forward('K', True), ('X', False))  # offset 11
        self.assertEqual(rotor.forward('L', True), ('F', False))  # offset 12
        self.assertEqual(rotor.forward('M', True), ('W', False))  # offset 13
        self.assertEqual(rotor.forward('N', True), ('W', False))  # offset 14
        self.assertEqual(rotor.forward('O', True), ('Q', False))  # offset 15
        self.assertEqual(rotor.forward('P', True), ('Q', False))  # offset 16
        self.assertEqual(rotor.forward('Q', True), ('Z', True))  # offset 17 or Q
        self.assertEqual(rotor.forward('R', True), ('H', False))  # offset 18 or R
        self.assertEqual(rotor.forward('S', True), ('A', False))  # offset 19

    def test_rotorI_backward(self):
        rotor = RotorI()
        self.assertEqual(rotor.forward('A'), ('E', False))
        self.assertEqual(rotor.backward('E'), 'A')
        self.assertEqual(rotor.forward('A', True), ('J', False))
        self.assertEqual(rotor.backward('J'), 'A')
