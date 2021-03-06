from models.CardValue import *
from models.Suit import *
from models.Card import *

OROS = 'OROS'
COPAS = 'COPAS'
ESPADAS = 'ESPADAS'
BASTOS = 'BASTOS'

CardValue('AS', 1, 'as')
CardValue('DOS', 2, 'dos')
CardValue('TRES', 3, 'tres')
CardValue('CUATRO', 4, 'cuatro')
CardValue('CINCO', 5, 'cinco')
CardValue('SEIS', 6, 'seis')
CardValue('SIETE', 7, 'siete')
CardValue('SOTA', 10, 'sota')
CardValue('CABALLO', 11, 'caballo')
lastCardValue = CardValue('REY', 12, 'rey')
print(lastCardValue)

oros = Suit(OROS, 'oros')
Suit(COPAS, 'copas')
Suit(ESPADAS, 'espadas')
Suit(BASTOS, 'bastos')

card = Card(lastCardValue, oros)
print(card)