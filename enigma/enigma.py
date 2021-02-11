from typing import NoReturn, List

from enigma.reflectors.reflector import Reflector
from enigma.rotors.rotor import Rotor
from .plugboard import Plugboard


class Enigma:
    """
    Enigma machine
    """

    def __init__(self, reflector: Reflector,
                 plugboard: Plugboard, rotors: List[Rotor]):
        """
        Creates a enigma machine

        :param reflector: the reflector to use
        :param plugboard: the plugboard to use
        :param rotors: the rotors for rotate chars
        """
        self.reflector = reflector
        self.plugboard = plugboard
        self.rotors = rotors

    def encrypt(self, plaintext: str) -> str:
        """
        Transforms the given plaintext

        :param plaintext: the plaintext to encrypt
        :return: the cyphertext
        """
        plaintext = plaintext.upper()
        plaintext = "".join([c for c in plaintext if c.isalpha()])
        cyphertext = ""
        for c in plaintext:
            c = self.plugboard.transform(c)
            for rot in self.rotors:
                c = rot.forward(c)
            c = self.reflector.reflect(c)
            for rot in self.rotors:
                c = rot.backward(c)
            c = self.plugboard.transform(c)
            cyphertext += c
        self._reset()
        return cyphertext

    def decrypt(self, cyphertext: str) -> str:
        """
        Decrypts a cyphertext
        :param cyphertext: the cyphertext to decrypt
        :return: the decrypted text
        """
        return self.encrypt(cyphertext)

    def _reset(self) -> NoReturn:
        """
        Resets enigma to initial state
        """
        for rot in self.rotors:
            rot.reset()
