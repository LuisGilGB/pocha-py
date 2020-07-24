from Card import Card

class PochaCard(Card):
    __pochaValue = 0

    def __init__(self, pochaCardValue, suit):
        super(pochaCardValue, suit)
        __pochaValue = pochaCardValue.getPochaValue()

    def getPochaValue(self):
        return self.__pochaValue
