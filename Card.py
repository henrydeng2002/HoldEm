class Card:
    # basic card structure
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # all the comparison methods
    def __eq__(self, card):
        return (self.value == card.value)

    def __ne__(self, card):
        return not (self.value == card.value)

    def __lt__(self, card):
        return (self.value < card.value)

    def __repr__(self):
        suit_str = "spades"
        if(self.suit == 2):
            suit_str = "diamonds"
        elif(self.suit == 3):
            suit_str = "clubs"
        elif(self.suit == 4):
            suit_str = "hearts"

        value_str = str(self.value)

        if(value_str == "14"):
            value_str = "A"
        elif(value_str == "13"):
            value_str = "K"
        elif(value_str == "12"):
            value_str = "Q"
        elif(value_str == "11"):
            value_str = "J"

        return "%s" % (value_str + " of " + suit_str)
