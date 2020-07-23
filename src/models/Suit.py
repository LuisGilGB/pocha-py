class Suit:
    __key = ''
    __text = ''

    def __init__(self, key, text):
        self.__key = key
        self.__text = text
        print('Created a new suit with key {} and text {}'.format(key, text))
    
    def getKey(self):
        return self.__key

    def getText(self):
        return self.__text
    
    def print(self):
        print(self.getText())
    
    def __str__(self):
        return self.getText()