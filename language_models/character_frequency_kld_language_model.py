from collections import Counter
from .language_model import LanguageModel
import scipy.special as sp

VALID_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"


class CharacterFrequencyKLDLanguageModel(LanguageModel):
    """
    A simple character frequency language model that uses Kullback Leibler Divergence
    """
    def __init__(self, text):
        self.frequencies = Counter([c for c in text if c.lower() in VALID_CHARACTERS])
        self.total_characters = sum(self.frequencies.values())

    def fitness(self, message) -> float:
        """
        Gets a message and returns how well fitted is to the language model

        :param message: the message to analyze
        :return: a measure of fitness (the greater the best)
        """
        frequencies = Counter(message)
        VALID_CAHARACTERS = len(VALID_CHARACTERS)

        # TODO: Try with Euler correction.
        x1 = []
        x2 = []
        for c in VALID_CHARACTERS:
            x1.append((self.frequencies[c] + 1) / (self.total_characters + VALID_CAHARACTERS))
            x2.append((frequencies[c] + 1) / (len(message) + VALID_CAHARACTERS))

        # TODO: Try with modified KB divergence.
        return -sum(sp.rel_entr(x1, x2))

