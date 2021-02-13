from collections import Counter
from .language_model import LanguageModel
import scipy.special as sp

VALID_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"


class CharacterFrequencyICLanguageModel(LanguageModel):
    """
    A simple character frequency language model that uses index of coincidence:
    Friedman, W. F. (1922). The index of coincidence and its applications in cryptography. Aegean Park Press.
    """
    def __init__(self, text: str):
        """
        :param text: the text used for training
        """
        frequencies = Counter([c for c in text if c.lower() in VALID_CHARACTERS])
        self.ic_expected = sum([f**2 for f in frequencies.values()])/(1/len(VALID_CHARACTERS))

    def fitness(self, message) -> float:
        """
        Gets a message and returns how well fitted is to the language model

        :param message: the message to analyze
        :return: a measure of fitness (the greater the best)
        """
        frequencies = Counter(message)
        ic = sum([f*(f-1) for f in frequencies.values()])/(len(message)*(len(message)-1)/len(VALID_CHARACTERS))
        return abs(ic-self.ic_expected)

