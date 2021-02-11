from typing import List, Tuple, Optional

class Plugboard:
    """
    Enigma plugboard
    """
    def __init__(self, permutations: Optional[List[Tuple[str, str]]] = None):
        """

        :param permutations: Plugboard permutations i.e. (J, A) means permutation A<->J
        """
        self.permutation_dict = {}
        if permutations:
            for perm_in, perm_out in permutations:
                if perm_in in self.permutation_dict or perm_out in self.permutation_dict:
                    raise Exception("Permutation already set")
                self.permutation_dict[perm_in] = perm_out
                self.permutation_dict[perm_out] = perm_in

    def transform(self, char: str) -> str:
        """
        Transforms a plaintext

        :param char: the char to transform
        :return: the transformed chars
        """
        return self.permutation_dict[char] if char in self.permutation_dict else char