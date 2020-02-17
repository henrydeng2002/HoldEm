import Board
import Deck
import Card
import random

class Player:
    # create a hand array for the player
    def __init__(self):
        self.hand = []

    # add a card to the hand array
    def newCard(self, card):
        self.hand.append(card)
