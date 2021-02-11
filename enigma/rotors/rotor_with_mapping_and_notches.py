from typing import NoReturn, Optional, Tuple, Dict, Set


class RotorWithMappingAndNotches:
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
        assert offset >= 0
        self.offset = offset
        self.period = period
        self.step_count = 0
        self.rotor_mapping = rotor_mapping
        self.notches = notches
        self.inverse_rotor_mapping = {v: k for k, v in self.rotor_mapping.items()}

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
        transformed = chr(((ord(char) - ord('A') + self.offset) % 26) + ord('A'))
        if transformed in self.rotor_mapping:
            transformed = self.rotor_mapping[transformed]
        return transformed, do_step

    def backward(self, char: str) -> str:
        """
        Applies the backward current run through the rotor

        :param char: the char to transform
        :return: the transformed char
        """
        assert ord('A') <= ord(char) <= ord('Z')
        transform = chr(((ord(char) - ord('A') - self.offset) % 26) + ord('A'))
        if transform in self.inverse_rotor_mapping:
            transform = self.inverse_rotor_mapping[transform]
        return transform

    def reset(self) -> NoReturn:
        """
        Resets rotor to initial state
        """
        self.offset -= self.step_count // self.period
        self.step_count = 0
