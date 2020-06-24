import Player
import Deck
from Card import Card
import random

'''
hi there
'''

class Board:
    def __init__(self):
        # array for the cards already on the board
        self.board_cards = []

        self.all_cards = []

    def addCard(self, card):
        # add a card onto the board
        self.board_cards.append(card)

    def handValue(self, hand):
        # add the cards from hand
        self.all_cards.clear()
        self.all_cards.extend(self.board_cards)
        for x in hand:
            self.all_cards.append(x)

        # sort in reverse order so highest card is in front
        self.all_cards.sort(reverse=True)

        # create a variable that stores the value of the hand_val
        # 1 is the lowest (just a high card), and 10 is the highest value (royal flush)
        self.hand_val = 0

        # check to see if the cards are a pair, three, flush, straight, or four
        # store the card value (if it is pair) and
        self.pair_list = self.isX(self.all_cards, 2)
        self.three_list = self.isX(self.all_cards, 3)
        self.flush_suit = self.isFlush(self.all_cards)
        self.straight_list = self.isStraight(self.all_cards)
        self.four_card = self.isX(self.all_cards, 4)
        self.high_card = self.highCard(self.all_cards)

        if (len(self.pair_list) != 0):
            self.hand_val = 2

        if (self.twoPair(self.pair_list)):
            self.hand_val = 3

        if (len(self.three_list) != 0):
            self.hand_val = 4

        if (len(self.straight_list) != 0):
            self.hand_val = 5

        if (self.flush_suit):
            self.hand_val = 6

        if (self.fullHouse(self.three_list, self.pair_list)):
            self.hand_val = 7

        if (len(self.four_card) != 0):
            self.hand_val = 8

        if (self.flushType(self.straight_list) == 9):
            self.hand_val = 9

        if (self.flushType(self.straight_list) == 10):
            self.hand_val = 10

        return self.hand_val

    #return 1 for hand1 bigger, 2 for hand2 bigger, 0 for tie
    def breakTie(self, hand1, hand2):
        board_card_max = Card(0,0)
        hand_card_max = Card(0,0)


        hand1.extend(self.board_cards)
        hand1.sort(reverse=True)

        hand2.extend(self.board_cards)
        hand2.sort(reverse=True)

        for x in self.board_cards:
            if (x.value > board_card_max.value):
                board_card_max = x

        for x in hand1:
            if (x.value > hand_card_max.value):
                hand_card_max = x

        for x in hand2:
            if (x.value > hand_card_max.value):
                if (x.value > board_card_max.value):
                    return 2

        if (hand_card_max.value > board_card_max.value):
            return 1

        return 0

    # basic compare methods
    # returns an array with all pairs/triples/fours
    def isX(self, all_cards, x, ignore=None):
        all_pairs = []
        # if (ignore != None):
        all_cards = [card for card in all_cards if card.value != ignore]
            # for i in range(len(all_cards)):
            #     print(i)
            #     if (all_cards[i].value == ignore):
            #         all_cards.remove(all_cards[i])
            #         i -= 1

        for i in range(len(all_cards) - (x - 1)):
            if (all_cards[i] == all_cards[i + (x - 1)]):
                all_pairs.append(all_cards[i])
        return all_pairs

    # returns 1-4 to see if there's a flush in any suit
    def isFlush(self, flush_cards):
        suit_nums = [0, 0, 0, 0]
        for i in range(len(flush_cards)):
            suit_nums[flush_cards[i].suit - 1] += 1
        for i in range(4):
            if (suit_nums[i] > 4):
                return True
        return False

    # returns the whole straight(s) in an array of arrays
    def isStraight(self, all_cards):
        straight_start_index = 0
        straight_list = []
        temp_straight = []
        while (straight_start_index < 3):
            for i in range (straight_start_index, len(all_cards) - 1):
                if (all_cards[i].value == all_cards[i + 1].value + 1):
                    if(len(temp_straight) == 0):
                        straight_start_index = i + 1
                    temp_straight.append(all_cards[i])
                    if (len(temp_straight) == 4):
                        temp_straight.append(all_cards[i+1])
                        straight_list.append(temp_straight)
                        temp_straight = []
                        break
                else:
                    straight_start_index += 1
                    temp_straight = []
        return straight_list

    # returns highest card
    def highCard(self, all_cards):
        return all_cards[0]

    # determine if is straight or royal flush
    def flushType(self, all_straights):
        for x in all_straights:
            if (self.isFlush(x)):
                if (x[0].value == 13):
                    return 10
                    # royal flush
                else:
                    return 9
                    # straight flush

    """
    should work
    """
    def fullHouse(self, three_list, pair_list):
        for x in three_list:
            for y in pair_list:
                if (x.value != 0 and y.value != 0):
                    if (x.value != y.value):
                        return True

    """
    should work
    """
    def twoPair(self, two_array):
        if (len(two_array) > 1):
            for x in range (len(two_array) - 1):
                if (two_array[x].value != two_array[x+1].value):
                    return True
        return False





# Three Men enter a bar in the USSR.
# One says, "why did Stalin only write in lowercase?"
# The other one says, "Because he was afraid of capitalism"
#
# The whole bar died laughing
