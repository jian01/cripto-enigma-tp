from .plugboard import Plugboard
from .rotor import Rotor
from typing import NoReturn, List

class Enigma:
    """
    Enigma machine
    """
    def __init__(self, plugboard: Plugboard, rotors: List[Rotor]):
        """
        Creates a enigma machine

        :param plugboard: the plugboard to use
        :param rotors: the rotors for rotate chars
        """
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
                c = rot.transform(c)
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
        plaintext = ""
        for c in cyphertext:
            c = self.plugboard.inverse_transform(c)
            for rot in self.rotors:
                c = rot.inverse_transform(c)
            c = self.plugboard.inverse_transform(c)
            plaintext += c
        self._reset()
        return plaintext

    def _reset(self) -> NoReturn:
        """
        Resets enigma to initial state
        """
        for rot in self.rotors:
            rot.reset()