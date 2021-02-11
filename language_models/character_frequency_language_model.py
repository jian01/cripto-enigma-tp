from collections import Counter

import scipy.special as sp

GERMAN_ALPHABET_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"


class CharacterFrequencyLanguageModel:
    def __init__(self, text):
        self.frequencies = Counter(text)
        self.total_characters = sum(self.frequencies.values())

    def kullback_leibler_divergence(self, message):
        frequencies = Counter(message)

        # TODO: Try with Euler correction.
        x1 = []
        x2 = []
        for c in GERMAN_ALPHABET_CHARACTERS:
            x1.append((self.frequencies[c] + 1) / self.total_characters)
            x2.append((frequencies[c] + 1) / len(message))

        # TODO: Try with modified KB divergence.
        return sum(sp.rel_entr(x1, x2))

