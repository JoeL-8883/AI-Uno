from Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.current = None
        self.build()
        self.discards = []


    def __getitem__(self, index):
        return self.cards[index]

    def cards(self):
        return self.cards

    def build(self):
        colors = ['R', 'Y', 'G', 'B']
        values2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'd', 'R', 'S']
        wilds = ['C', 'D']

        # Coloured cards
        for color in colors:
            for value in values2:
                for i in range(2):
                    self.cards.append(color + value)
                    #self.cards.append(Card(color, value))

        # Zero cards
        for color in colors:
            self.cards.append(color + '0')
            #self.cards.append(Card(color, '0'))

        # Wild cards
        for i in range(4):
            for wild in wilds:
                self.cards.append('W' + wild)
                #self.cards.append(Card('W', wild))
        
        # Shuffle the cards
        random.shuffle(self.cards)

        # Put the first card on the discard pile
        self.current = self.draw_card()
    
    def initial_draw(self, player):
        for i in range(7):
            player.draw(self.cards.pop(0))

    def draw_card(self):
        card = self.cards.pop(0)
        return card
    
    def remove_card(self, card):
        self.cards.remove(card)

