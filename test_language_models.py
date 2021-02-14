import unittest
from language_models.character_frequency_kld_language_model import CharacterFrequencyKLDLanguageModel
from language_models.character_frequency_ic_language_model import CharacterFrequencyICLanguageModel
from language_models.markov_chain_model import MarkovChainModel
import random

class LanguageModelTests(unittest.TestCase):
    def test_char_freq_KLD(self):
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            model = CharacterFrequencyKLDLanguageModel(book.read())
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            self.assertEqual(model.fitness(book.read()), 0)
        with open('books/Frankenstein.txt', 'r') as book:
            frank = book.read()
        with open('books/Through_the_Looking-Glass.txt', 'r') as book:
            carol2 = book.read()
        self.assertAlmostEqual(model.fitness(frank), 0, delta=0.02)
        self.assertGreater(model.fitness(carol2), model.fitness(frank))
        self.assertLess(model.fitness("sadasjgfjasgfjsadf"), 0)

    def test_chat_freq_IC(self):
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            model = CharacterFrequencyICLanguageModel(book.read())
        self.assertAlmostEqual(model.ic_expected, 1.73, delta=0.03)
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            self.assertAlmostEqual(model.fitness(book.read()), 0, delta=0.001)
        with open('books/Frankenstein.txt', 'r') as book:
            frank = book.read()
        self.assertAlmostEqual(model.fitness(frank), 0, delta=0.01)
        self.assertLess(model.fitness("sadasjgfjasgfjsadf"), 0)

    def test_markov_chain_order_1(self):
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            model = MarkovChainModel(book.read())
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            self.assertEqual(model.fitness(book.read()), 0)
        with open('books/Frankenstein.txt', 'r') as book:
            frank = book.read()
        with open('books/Through_the_Looking-Glass.txt', 'r') as book:
            carol2 = book.read()
        self.assertGreater(model.fitness(carol2), model.fitness(frank))
        self.assertLess(model.fitness("sadasjgfjasgfjsadf"), 0)
        self.assertGreater(model.fitness("".join([c for c in carol2 if c.isalpha()][:1000])),
                           model.fitness("".join([chr(ord('A') + random.randint(0, 25)) for _ in range(1000)])))

    def test_markov_chain_order_3(self):
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            model = MarkovChainModel(book.read(), order=3)
        with open('books/Alices_Adventures_in_Wonderland.txt', 'r') as book:
            self.assertEqual(model.fitness(book.read()), 0)
        with open('books/Frankenstein.txt', 'r') as book:
            frank = book.read()
        with open('books/Through_the_Looking-Glass.txt', 'r') as book:
            carol2 = book.read()
        self.assertGreater(model.fitness(carol2), model.fitness(frank))
        self.assertLess(model.fitness("sadasjgfjasgfjsadf"), 0)
        self.assertGreater(model.fitness("".join([c for c in carol2 if c.isalpha()][:1000])),
                           model.fitness("".join([chr(ord('A') + random.randint(0, 25)) for _ in range(1000)])))