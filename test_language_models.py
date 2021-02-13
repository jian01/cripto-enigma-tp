import unittest
from language_models.character_frequency_kld_language_model import CharacterFrequencyKLDLanguageModel
from language_models.character_frequency_ic_language_model import CharacterFrequencyICLanguageModel

class LanguageModelTests(unittest.TestCase):
    def test_char_freq_KLD(self):
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            model = CharacterFrequencyKLDLanguageModel(book.read())
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            self.assertAlmostEqual(model.fitness(book.read()), 0, delta=0.001)
        with open('books/Frankenstein.txt', 'r') as book:
            self.assertAlmostEqual(model.fitness(book.read()), 0, delta=0.02)

    def test_chat_freq_IC(self):
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            model = CharacterFrequencyICLanguageModel(book.read())
        self.assertAlmostEqual(model.ic_expected, 1.73, delta=0.03)
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            self.assertAlmostEqual(model.fitness(book.read()), 0, delta=0.001)
        with open('books/Frankenstein.txt', 'r') as book:
            self.assertAlmostEqual(model.fitness(book.read()), 0, delta=0.01)