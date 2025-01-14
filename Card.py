class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def get_card(self):
        return self.color + self.number
    
    def get_color(self):
        return self.color
    
    def get_number(self):
        return self.number