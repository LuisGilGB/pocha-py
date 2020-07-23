class Card:
    __value = None
    __suit = None
    __text = ''

    def __init__(self, cardValue, suit):
        self.__value = cardValue
        self.__suit = suit
        self.__text = '{} de {}'.format(cardValue.getText().capitalize(), suit.getText().capitalize())
        print('Created card {}'.format(self.__text))

    def getValueKey(self):
        return self.__value.getKey()

    def getSuit(self):
        return self.__suit.getKey()

    def getValue(self):
        return self.__value.getValue()

    def getValueText(self):
        return self.__value.getValueText()

    def getSuitText(self):
        return self.__suit.getText()

    def getText(self):
        return self.__text

    def print(self):
        print(self.getText())

    def __str__(self):
        return self.getText()
