import Player
import Deck
from Card import Card
import random


class Board:
    def __init__(self):
        # array for the cards already on the board
        self.all_cards = []
        self.board_cards = []

    def addCard(self, card):
        # add a card onto the board
        """
        change into board_cards after testing
        """
        self.all_cards.append(card)

    def handValue(self):
        # # add the cards from hand
        # self.all_cards = self.board_cards
        # for x in hand:
        #     self.all_cards.append(hand[x])

        # sort in reverse order so highest card is in front
        self.all_cards.sort(reverse=True)

        # create a variable that stores the value of the hand_val
        # 1 is the lowest (just a high card), and 10 is the highest value (royal flush)
        self.hand_val = 0

        # check to see if the cards are a pair, three, flush, straight, or four
        # store the card value (if it is pair) and
        self.pair_card = self.isX(self.all_cards, 2)
        self.three_card = self.isX(self.all_cards, 3)
        self.flush_suit = self.isFlush(self.all_cards)
        self.straight_card = self.isStraight(self.all_cards)
        self.four_card = self.isX(self.all_cards, 4)
        self.high_card = self.highCard(self.all_cards)



        return self.hand_val

    # basic compare methods
    # returns the value of the card pair
    def isX(self, all_cards, x):
        null_card = Card(0, 0)
        for i in range(7 - (x - 1)):
            if (all_cards[i] == all_cards[i + (x - 1)]):
                return all_cards[i]
        return null_card
    """
    make something that can find the second highest pair
    """

    # returns 1-4 to see if there's a flush in any suit
    def isFlush(self, all_cards):
        suit_nums = [0, 0, 0, 0]
        for i in range(7):
            suit_nums[all_cards[i].suit] + 1
        for i in range(4):
            if (suit_nums[i] > 4):
                return suit_nums[i]
        return 0

    """
    unfinished
    """
    # returns smallest (first) card of the straight
    def isStraight(self, all_cards):
        straight_list = []
        for i in range(6):
            if (all_cards[i].value == all_cards[i + 1].value + 1):
                straight_list.append(all_cards[i])
        return straight_list
    """
    rewrite: currently the straight can jump and the method will still count it as a straight
    find a way to find multiple straights (if there's a 6 straight, there are technically two straights, and the lower one
    could have the flush, so I need to keep track of both)
    """

    # returns highest card
    def highCard(self, all_cards):
        return all_cards[0]

    # determine if is straight or royal flush
    def flushType(self):
        isStraightFlush = True
        for x in self.straight_card:
            if (x.suit != flush_suit):
                isStraightFlush = False
        # straight flush
        if (isStraightFlush):
            self.hand_val = 9
        if (self.straight_card[4].value == 10):
            # royal flush
            self.hand_val = 10
    """
    rewrite: take in an array
    """


    def fullHouse(self):
        if (self.three_card.value != 0 and self.pair_card.value != 0):
            if (self.three_card.value != self.pair_card.value):
                self.hand_val = 8









# Three Men enter a bar in the USSR.
# One says, "why did Stalin only write in lowercase?"
# The other one says, "Because he was afraid of capitalism"
#
# The whole bar died laughing
