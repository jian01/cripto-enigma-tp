from typing import NoReturn, Optional, Tuple, Dict, Set

from .rotor import Rotor


class RotorWithMappingAndNotches(Rotor):
    """
    Engima rotor with a mapping for each character and a notch
    """

    def __init__(self, offset: int, period: int,
                 rotor_mapping: Dict[str, str],
                 notches: Set[str]):
        """

        :param offset: the offset of the rotor, 0 for no rotation
        :param period: the period corresponding to adding one to the offset
        :param rotor_mapping: the mapping of the rotor
        :param notches: the output chars that cause the rotor to make the next one step
        """
        assert period > 0
        assert offset >= 0 and offset <= 25
        self.rotor_mapping = rotor_mapping
        self.notches = notches
        self.inverse_rotor_mapping = {v: k for k, v in self.rotor_mapping.items()}
        super().__init__(offset, period)

    def forward(self, char: str, step: Optional[bool] = False) -> Tuple[str, bool]:
        """
        Transforms a char through the rotor
        :param char: the char to transform
        :param step: if the rotor should step before transforming
        :return: the transformed char and a tuple indicating whether the next rotor should step
        """
        assert ord('A') <= ord(char) <= ord('Z')
        do_step = False
        if step:
            self.step_count += 1
            if self.step_count % self.period == 0:
                if chr(ord('A') + (self.offset % 26)) in self.notches:
                    do_step = True
                self.offset += 1
        char = chr(((ord(char) - ord('A') + self.offset) % 26) + ord('A'))
        if char in self.rotor_mapping:
            char = self.rotor_mapping[char]
        char = chr(((ord(char) - ord('A') - self.offset) % 26) + ord('A'))
        return char, do_step

    def backward(self, char: str) -> str:
        """
        Applies the backward current run through the rotor

        :param char: the char to transform
        :return: the transformed char
        """
        assert ord('A') <= ord(char) <= ord('Z')
        char = chr(((ord(char) - ord('A') + self.offset) % 26) + ord('A'))
        if char in self.inverse_rotor_mapping:
            char = self.inverse_rotor_mapping[char]
        char = chr(((ord(char) - ord('A') - self.offset) % 26) + ord('A'))
        return char

    def reset(self) -> NoReturn:
        """
        Resets rotor to initial state
        """
        self.offset -= self.step_count // self.period
        self.step_count = 0
