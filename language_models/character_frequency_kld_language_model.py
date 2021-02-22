from collections import Counter
from .language_model import LanguageModel
from scipy.special import kl_div

VALID_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"


class CharacterFrequencyKLDLanguageModel(LanguageModel):
    """
    A simple character frequency language model that uses Kullback Leibler Divergence
    """
    def __init__(self, text: str):
        text = [c for c in text.lower() if c in VALID_CHARACTERS]
        self.frequencies = Counter(text)
        self.total_characters = sum(self.frequencies.values())

    def fitness(self, message) -> float:
        """
        Gets a message and returns how well fitted is to the language model

        :param message: the message to analyze
        :return: a measure of fitness (the greater the best)
        """
        message = [c for c in message.lower() if c in VALID_CHARACTERS]
        frequencies = Counter(message)

        x1 = []
        x2 = []
        for c in VALID_CHARACTERS:
            euler1 = (1 if self.frequencies[c] == 0 else 0)
            euler2 = (1 if frequencies[c] == 0 else 0)
            x1.append((self.frequencies[c]+euler1) / (self.total_characters+euler1))
            x2.append((frequencies[c]+euler2) / (len(message)+euler2))

        # TODO: Try with modified KB divergence.
        return -sum(kl_div(x1, x2))

