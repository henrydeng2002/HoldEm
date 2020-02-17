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
        return "%s" % (self.value)
