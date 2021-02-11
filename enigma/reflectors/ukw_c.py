from .reflector import Reflector


class UkwC(Reflector):
    """
    Engima reflector C
    """

    def __init__(self):
        self.reflection_map = {}
        for l1, l2 in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "RDOBJNTKVEHMLFCWZAXGYIPSUQ"):
            self.reflection_map[l1] = l2

    def reflect(self, char: str) -> str:
        """
        Reflects a char through the reflector
        :param char: the char to reflect
        :return: the reflected char
        """
        return self.reflection_map[char]
