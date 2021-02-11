from typing import NoReturn, Optional, Tuple


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
        self.step_count = 0

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
                self.offset += 1
                if self.offset > 0 and self.offset % 26 == 0:
                    do_step = True
        transformed = chr(((ord(char) - ord('A') + self.offset) % 26) + ord('A'))
        return transformed, do_step

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
        self.offset -= self.step_count // self.period
        self.step_count = 0
