from CardValue import import CardValue

class PochaCardValue(CardValue):
    __pochaValue = 0

    def __init__(self, key, value, text, pochaValue):
        super().__init__(key, value, text)
        self.__pochaValue = pochaValue

    def getPochaValue(self):
        return self.__pochaValue
