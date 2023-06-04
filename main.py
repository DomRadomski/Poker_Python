from card import Card
from deck import Deck


def main():
    print("Welcome to Poker")

    cards = []
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


    deck = Deck(cards, suits, values)
    deck.display_deck()
    deck.shuffle()
    deck.display_deck()

main()
