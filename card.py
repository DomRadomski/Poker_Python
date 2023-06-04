class Card:

    suit = ""
    value = ""

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def output_card(self, suit, value):
        print(return f"{self.value} of {self.suit}")

