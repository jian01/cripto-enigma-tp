from abc import abstractmethod

class LanguageModel:

    @abstractmethod
    def fitness(self, message) -> float:
        """
        Gets a message and returns how well fitted is to the language model

        :param message: the message to analyze
        :return: a measure of fitness (the greater the best)
        """
        pass
