from Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()

    def __getitem__(self, index):
        return self.cards[index]

    def cards(self):
        return self.cards
    
    def print_deck(self):
        print([card.get_card() for card in self.cards])

    def build(self):
        colors = ['R', 'Y', 'G', 'B']
        values2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'd', 'R', 'S']
        wilds = ['C', 'D']

        # Coloured cards
        for color in colors:
            for value in values2:
                for i in range(2):
                    self.cards.append(Card(color, value))

        # Zero cards
        for color in colors:
            self.cards.append(Card(color, '0'))

        # Wild cards
        for i in range(4):
            for wild in wilds:
                self.cards.append(Card('W', wild))

    def shuffle(self):
        random.shuffle(self.cards)
