from card import Card
import random

class Deck:

    cards = []
    suits = []
    values = []

    def __init__(self, cards, suits, values):
       
        self.cards = cards
        self.suits = suits
        self.values = values
        
        for suit in self.suits:
            for value in self.values:
                card = Card(suit, value)
                self.cards.append(card)

    def display_deck(self):
        for card in self.cards:
            card.output_card()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        card = self.cards[0]
        self.cards.pop(0)
        return cardg

    
                
