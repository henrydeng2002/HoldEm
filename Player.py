import Board
import Deck
import Card
import random

class Player:
    # create a hand array for the player
    def __init__(self, name):
        self.hand = []
        #amount of chips a player has
        self.chips = 500
        self.name = name
        self.is_playing = True
        #because lowest possible hand val is 0
        self.hand_val = -1

    # add a card to the hand array
    def addCard(self, card):
        self.hand.append(card)
