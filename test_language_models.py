import unittest
from language_models.character_frequency_kld_language_model import CharacterFrequencyKLDLanguageModel

class LanguageModelTests(unittest.TestCase):
    def test_char_freq_KLD(self):
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            model = CharacterFrequencyKLDLanguageModel(book.read())
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            self.assertEqual(model.fitness(book.read()), 0)