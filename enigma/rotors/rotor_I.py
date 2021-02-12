from typing import Optional

from .rotor_with_mapping_and_notches import RotorWithMappingAndNotches


class RotorI(RotorWithMappingAndNotches):
    """
    Engima rotor I
    """

    def __init__(self, offset: Optional[int] = 0):
        """

        :param offset: the offset of the rotor, 0 for no rotation
        """
        assert offset >= 0
        period = 1
        rotor_mapping = {}
        for l1, l2 in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "EKMFLGDQVZNTOWYHXUSPAIBRCJ"):
            rotor_mapping[l1] = l2
        notches = {'Q'}
        super().__init__(offset, period, rotor_mapping, notches)
