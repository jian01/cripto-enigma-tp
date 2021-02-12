from typing import Optional

from .rotor_with_mapping_and_notches import RotorWithMappingAndNotches


class RotorII(RotorWithMappingAndNotches):
    """
    Engima rotor II
    """

    def __init__(self, offset: Optional[int] = 0):
        """

        :param offset: the offset of the rotor, 0 for no rotation
        """
        assert offset >= 0
        period = 1
        rotor_mapping = {}
        for l1, l2 in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "AJDKSIRUXBLHWTMCQGZNPYFVOE"):
            rotor_mapping[l1] = l2
        notches = {'E'}
        super().__init__(offset, period, rotor_mapping, notches)
