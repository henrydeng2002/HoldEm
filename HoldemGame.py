from Player import Player
from Board import Board
from Deck import Deck
from Card import Card
import random
import os

# class HoldemGame:
class HoldemGame:
    def __init__(self):
        self.players = []
        self.board = Board()
        self.deck = Deck()
        #check if this is needed
        self.pot = 0

    def addPlayers(self):
        adding = True
        while(adding):
            name = input("Type your name: ")
            player = Player(name)
            self.players.append(player)

            still_adding = True
            while(still_adding):
                more_players = input("Add More Players? ([Y]es or [N]o): ")
                if (len(self.players) >= 10 or more_players == "No" or more_players == "N"):
                    adding = False
                    still_adding = False
                elif (more_players == "Yes" or more_players == "Y"):
                    still_adding = False
                else:
                    print("Invalid Response. Please enter again")

        os.system('clear')

    """
    change so that pot is calculated and each player who folds still loses whatever they called
    """
    #all the good betting stuff
    def bet(self):
        prev_bet = 0
        current_bet = 0
        #becomes false when the betting stops
        betting = True
        #how many people have already betted
        person_on = 0
        #the current person that is betting
        curr_person = 0
        #check if player has enough chips to bet
        #decide on how much each player is going to bet (or fold)
        while(betting):
            if (self.players[curr_person].is_playing == True):
                print("Here are the cards on the board:")
                self.printCards(self.board.board_cards)

                print(self.players[curr_person].name+ ", here are your cards: ")
                self.printCards(self.players[curr_person].hand)
                #print(self.players[curr_person].hand)
                print(self.players[curr_person].name+ ", here are your remaining chips: " + str(self.players[curr_person].chips - prev_bet))
                #print(self.players[curr_person].chips - current_bet)

                answering = True
                while(answering):
                    next_action = input(self.players[curr_person].name + ", What's Your Move ([R]aise, [C]all, or [F]old): ")
                    if (next_action == "Raise" or next_action == "R"):
                        raise_amount = input("By How Much? ")
                        prev_bet = current_bet
                        current_bet += int(raise_amount)
                        person_on = 0
                        answering = False
                        #test if raise_amount is an int
                    elif (next_action == "Call" or next_action == "C"):
                        answering = False
                    elif (next_action == "Fold" or next_action == "F"):
                        """
                        find way to not remove the player and instead just update a status or something
                        """
                        self.players[curr_person].is_playing = False
                        self.players[curr_person].chips -= prev_bet
                        self.pot += prev_bet
                        answering = False
                    else:
                        print("Invalid Answer, Please enter again.")

                os.system('clear')

            curr_person += 1
            person_on += 1

            if (person_on >= len(self.players)):
                betting = False

            if (curr_person == len(self.players)):
                curr_person = 0

        for x in self.players:
            if (x.is_playing):
                x.chips -= current_bet
                self.pot += current_bet

        print()

    #draw a card from deck and add it to each player
    def dealPlayerCard(self):
        for x in self.players:
            x.addCard(self.deck.drawCard())

    def dealBoardCard(self):
        self.board.addCard(self.deck.drawCard())

    def findWinner(self):
        highest_val = -1
        highest_player = [Player("not player")]
        for x in self.players:
            if(x.is_playing):
                x.hand_val = self.board.handValue(x.hand)
                if (x.hand_val > highest_player[0].hand_val):
                    highest_player.clear()
                    highest_player.append(x)
                    highest_val = x.hand_val
                elif(x.hand_val == highest_player[0].hand_val):
                    winner = self.board.breakTie(x.hand, highest_player[0].hand)
                    if (winner == 1):
                        highest_player = []
                        highest_player.append(x)
                    elif (winner == 0):
                        highest_player.append(x)

        for x in highest_player:
            print(x.name + " Wins")
            #split pot evenly
            x.chips += (self.pot/len(highest_player))

    def startGame(self):
        self.addPlayers()

    def play(self):
        for x in self.players:
            x.is_playing = True

        self.bet()

        for x in range(2):
            self.dealPlayerCard()

        self.bet()

        for x in range(3):
            self.dealBoardCard()

        self.bet()

        self.dealBoardCard()

        self.bet()

        self.dealBoardCard()


        print(self.board.board_cards)

        self.findWinner()

        for x in self.players:
            print(x.chips)

        while(True):
            play_again = input("Play another round? ([Y]es or [N]o): ")
            if (play_again == "Yes" or play_again == "Y"):
                return True
            elif (play_again == "No" or play_again == "N"):
                return False
            else:
                print("Invalid Response. Please enter again:")

    def reset(self):
        self.board.board_cards.clear()
        for x in self.players:
            x.hand.clear()
        self.pot = 0

    #method to print each card on an individual line
    def printCards(self, print_cards):
        print_cards.sort()
        for x in print_cards:
            print(x)
        print()


        # quick check to see if card is correctly drawn from deck
        # temp_deck = self.deck.cards
        # temp_deck.sort()
        # print(temp_deck)



# Where do pirates get their hooks?
# From the second hand store
