from collections import Counter
from .language_model import LanguageModel
from typing import Optional
from .character_frequency_kld_language_model import CharacterFrequencyKLDLanguageModel

VALID_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"


class MarkovChainModel(LanguageModel):
    """
    Nth order markov chain using the KL divergence as fitness measure
    """
    def __init__(self, text: str, order: Optional[int]=1):
        """
        :param text: the text used for training
        """
        conditional_strings = {}
        text = [c for c in text.lower() if c in VALID_CHARACTERS]
        for i in range(len(text) - 1):
            if text[i] not in conditional_strings:
                conditional_strings[text[i]] = []
            conditional_strings[text[i]].append(text[i+1])
        self.conditional_models = {}
        for k in conditional_strings.keys():
            if order == 1:
                self.conditional_models[k] = CharacterFrequencyKLDLanguageModel("".join(conditional_strings[k]))
            else:
                self.conditional_models[k] = MarkovChainModel("".join(conditional_strings[k]), order-1)

    def fitness(self, message) -> float:
        """
        Gets a message and returns how well fitted is to the language model

        :param message: the message to analyze
        :return: a measure of fitness (the greater the best)
        """
        conditional_strings = {}
        text = [c for c in message.lower() if c in VALID_CHARACTERS]
        for i in range(len(text) - 1):
            if text[i] not in conditional_strings:
                conditional_strings[text[i]] = []
            conditional_strings[text[i]].append(text[i+1])
        fitness = 0
        for k in self.conditional_models.keys():
            fitness += self.conditional_models[k].fitness(("".join(conditional_strings[k]) if k in conditional_strings else ""))
        return fitness

