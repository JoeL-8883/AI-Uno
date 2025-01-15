class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.str = color + number

    def get_card(self):
        return self.str
    
    def get_color(self):
        return self.color
    
    def get_number(self):
        return self.number