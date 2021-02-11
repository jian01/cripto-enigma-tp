import unittest

from enigma.enigma import Enigma
from enigma.plugboard import Plugboard
from enigma.reflectors.reflector import Reflector
from enigma.reflectors.ukw_b import UkwB
from enigma.reflectors.ukw_c import UkwC
from enigma.rotors.rotor import Rotor

PLUGBOARD_TUPLES = [('A', 'F'), ('G', 'H'), ('Y', 'S'), ('M', 'T')]
LOREM_IPSUM = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""


class EnigmaInvariantTests(unittest.TestCase):
    def test_encryption_decryption_no_rotors(self):
        enigma = Enigma(reflector=Reflector(),
                        plugboard=Plugboard(PLUGBOARD_TUPLES), rotors=[])
        cyphertext = enigma.encrypt("Probando")
        self.assertEqual(enigma.decrypt(cyphertext), "PROBANDO")

    def test_encryption_decryption_one_rotor_no_offset(self):
        enigma = Enigma(reflector=Reflector(),
                        plugboard=Plugboard(PLUGBOARD_TUPLES),
                        rotors=[Rotor(offset=0, period=1)])
        cyphertext = enigma.encrypt("Probando")
        self.assertEqual(enigma.decrypt(cyphertext), "PROBANDO")

    def test_encryption_decryption_one_rotor(self):
        enigma = Enigma(reflector=Reflector(),
                        plugboard=Plugboard(PLUGBOARD_TUPLES),
                        rotors=[Rotor(offset=10, period=1)])
        cyphertext = enigma.encrypt("Probando")
        self.assertEqual(enigma.decrypt(cyphertext), "PROBANDO")

    def test_encryption_decryption_multiple_rotors(self):
        enigma = Enigma(reflector=Reflector(),
                        plugboard=Plugboard(PLUGBOARD_TUPLES),
                        rotors=[Rotor(offset=10, period=1),
                                Rotor(offset=10, period=2),
                                Rotor(offset=10, period=3),
                                Rotor(offset=10, period=7),
                                Rotor(offset=10, period=26)])
        cyphertext = enigma.encrypt(LOREM_IPSUM)
        self.assertEqual(enigma.decrypt(cyphertext), "".join([c for c in LOREM_IPSUM.upper() if c.isalpha()]))

    def test_encryption_decryption_w_ukw_b(self):
        enigma = Enigma(reflector=UkwB(),
                        plugboard=Plugboard(PLUGBOARD_TUPLES),
                        rotors=[Rotor(offset=10, period=1),
                                Rotor(offset=10, period=2),
                                Rotor(offset=10, period=3),
                                Rotor(offset=10, period=7),
                                Rotor(offset=10, period=26)])
        cyphertext = enigma.encrypt(LOREM_IPSUM)
        self.assertEqual(enigma.decrypt(cyphertext), "".join([c for c in LOREM_IPSUM.upper() if c.isalpha()]))

    def test_encryption_decryption_w_ukw_c(self):
        enigma = Enigma(reflector=UkwC(),
                        plugboard=Plugboard(PLUGBOARD_TUPLES),
                        rotors=[Rotor(offset=10, period=1),
                                Rotor(offset=10, period=2),
                                Rotor(offset=10, period=3),
                                Rotor(offset=10, period=7),
                                Rotor(offset=10, period=26)])
        cyphertext = enigma.encrypt(LOREM_IPSUM)
        self.assertEqual(enigma.decrypt(cyphertext), "".join([c for c in LOREM_IPSUM.upper() if c.isalpha()]))
