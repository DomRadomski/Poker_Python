class Card:

    suit = None
    value = None

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def output_card(self):
        print(f"{self.value} of {self.suit}")

