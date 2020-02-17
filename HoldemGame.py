from Player import Player
from Board import Board
from Deck import Deck
from Card import Card
import random

# class HoldemGame:
class HoldemGame:
    def __init__(self):
        self.ended = False
        self.players = []
        self.board = Board()
        self.deck = Deck()

    def play(self):
        for x in range(5):
            player = Player()
            self.players.append(player)

        # while (ended != True):
        #     # player1.newCard
        #     # print(player1.hand)
        #     pass

        # for x in range(1, 8):
        #     self.board.addCard(Card(x, 2))

        self.board.addCard(Card(3, 1))
        self.board.addCard(Card(3, 2))
        self.board.addCard(Card(3, 3))
        self.board.addCard(Card(2, 1))
        self.board.addCard(Card(2, 2))
        self.board.addCard(Card(9, 1))
        self.board.addCard(Card(7, 1))

        self.board.all_cards.sort(reverse=True)

        for x in self.board.all_cards:
            print(x.value)

        self.board.handValue()
        self.board.fullHouse()

        print(self.board.hand_val)
        print(self.board.pair_card)

    # if __name__ == '__main__':
    #     main()
