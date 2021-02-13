from itertools import product
from random import shuffle
from enigma.rotor import Rotor
from enigma.enigma import Enigma
from enigma.plugboard import Plugboard
from language_models.character_frequency_language_model import CharacterFrequencyLanguageModel

GERMAN_ALPHABET_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

# TODO: Is this a parameter?
HARDCODED_PERIOD = 26


class Cracker:
    def __init__(self, language_model, plugboard_pairs):
        self.language_model = language_model
        self.plugboard_pairs = plugboard_pairs

    def crack(self, encrypted_message):
        combinations = list(product(range(len(GERMAN_ALPHABET_CHARACTERS)), repeat=4))
        shuffle(combinations)
        print(combinations[:10])

        kb_divergences = {}
        i=0
        for combination in combinations:
            rotor_1 = Rotor(combination[0], HARDCODED_PERIOD)
            rotor_2 = Rotor(combination[1], HARDCODED_PERIOD)
            rotor_3 = Rotor(combination[2], HARDCODED_PERIOD)
            rotor_4 = Rotor(combination[3], HARDCODED_PERIOD)
            enigma_machine = Enigma(plugboard, [rotor_1, rotor_2, rotor_3, rotor_4])
            decrypted_message = enigma_machine.decrypt(encrypted_message)
            kb_divergences[combination] = (self.language_model.fitness(decrypted_message), decrypted_message)
            #print(i)
            i+=1
        sorted_divergences = sorted(kb_divergences.items(), key=lambda x: x[1])
        return sorted_divergences[:1000]


plugboard_pairs = []
# TODO: Discuss if plugboard pairs are random.
characters = [a.upper() for a in GERMAN_ALPHABET_CHARACTERS]
shuffle(characters)
for i in range(10):
    plugboard_pairs.append((characters[i], characters[-i - 1]))

plugboard = Plugboard(plugboard_pairs)

language_model2 = CharacterFrequencyLanguageModel("probarunanuevamaneradeescribir".upper())
cracker = Cracker(language_model2, 10)

enigma = Enigma(plugboard, [Rotor(1, HARDCODED_PERIOD), Rotor(10, HARDCODED_PERIOD), Rotor(12, HARDCODED_PERIOD),
                            Rotor(15, HARDCODED_PERIOD)])

encrypted = enigma.encrypt("probarunanuevamaneradeescribir".upper())

print(cracker.crack(encrypted))
