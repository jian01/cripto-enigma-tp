from typing import Optional

from .rotor_with_mapping_and_notches import RotorWithMappingAndNotches


class RotorI(RotorWithMappingAndNotches):
    """
    Engima rotor I
    """

    def __init__(self, offset: Optional[int] = 0, ring_setting: Optional[int] = 0):
        """

        :param offset: the offset of the rotor, 0 for no rotation
        """
        assert ring_setting >= 0 and ring_setting <= 25
        period = 1
        mapping_string = list("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        for i in range(len(mapping_string)):
            mapping_string[i] = chr((ord(mapping_string[i])-ord('A')+ring_setting) % 26 + ord('A'))
        mapping_string = "".join(mapping_string[-ring_setting:] + mapping_string[:-ring_setting])
        rotor_mapping = {}
        for l1, l2 in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", mapping_string):
            rotor_mapping[l1] = l2
        notches = {'Q'}
        super().__init__(offset, period, rotor_mapping, notches)
