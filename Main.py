from Player import Player
from Board import Board
from Deck import Deck
from Card import Card
from HoldemGame import HoldemGame

def main():
    game = HoldemGame()
    game.startGame()
    playing = True
    while(playing):
        playing = game.play()
        game.reset()

if __name__ == '__main__':
    main()
