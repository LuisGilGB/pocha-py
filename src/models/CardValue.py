class CardValue:
    __key = ''
    __value = 0
    __text = ''
    __valueText = ''
    
    def __init__(self, key, value, text):
        self.__key = key
        self.__value = value
        self.__text = text
        self.__valueText = str(value)
        print('Created a card value with key {} and value {}, read as {}.'.format(key, self.__valueText, text))

    def getKey(self):
        return self.__key

    def getValue(self):
        return self.__value

    def getText(self):
        return self.__text

    def getValueText(self):
        return self.__valueText

    def print(self):
        return self.getText()

    def __str__(self):
        return '{} ({})'.format(self.getText(), self.getValueText())
