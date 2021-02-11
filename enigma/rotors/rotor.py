from typing import NoReturn


class Rotor:
    """
    Engima rotor
    """

    def __init__(self, offset: int, period: int):
        """

        :param offset: the offset of the rotor, 0 for no rotation
        :param period: the period corresponding to adding one to the offset
        """
        assert period > 0
        assert offset >= 0
        self.offset = offset
        self.period = period
        self.cyphered_count = 0

    def forward(self, char: str) -> str:
        """
        Transforms a char through the rotor
        :param char: the char to transform
        :return: the transformed char
        """
        assert ord('A') <= ord(char) <= ord('Z')
        self.cyphered_count += 1
        if self.cyphered_count % self.period == 0:
            self.offset += 1
        transformed = chr(((ord(char) - ord('A') + self.offset) % 26) + ord('A'))
        return transformed

    def backward(self, char: str) -> str:
        """
        Applies the backward current run through the rotor

        :param char: the char to transform
        :return: the transformed char
        """
        assert ord('A') <= ord(char) <= ord('Z')
        transform = chr(((ord(char) - ord('A') - self.offset) % 26) + ord('A'))
        return transform

    def reset(self) -> NoReturn:
        """
        Resets rotor to initial state
        """
        self.offset -= self.cyphered_count // self.period
        self.cyphered_count = 0
