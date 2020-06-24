import Player
import Board
from Card import Card
import random

class Deck:

    # generate the deck and shuffle it
    def __init__(self):
        self.cards = []
        self.total_cards = 52
        self.card_drawn = Card(0, 0);
        #since aces are the highest card, 14=ace
        for card_val in range(2, 15):
            for suit in range(1, 5):
                self.cards.append(Card(card_val, suit))

        random.shuffle(self.cards)

    # take a random card, return it, and remove it from the deck
    def drawCard(self):
        self.card_drawn = self.cards[random.randint(0, self.total_cards - 1)]
        self.cards.remove(self.card_drawn)
        self.total_cards -= 1
        return self.card_drawn
