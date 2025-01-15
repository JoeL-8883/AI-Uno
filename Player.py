class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
      
    def draw(self, card):
        self.hand.append(card)

    def get_hand(self):
        return sorted(self.hand)
    
    def has_valid_card(self, current):
        for card in self.hand:
            if card[0] == current[0] or card[1] == current[1] or card[0] == "W":
                return True
        return False
    
    def play(self, card):
        self.hand.remove(card)
        return card

