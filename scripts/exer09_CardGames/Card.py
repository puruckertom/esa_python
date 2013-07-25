'''
Created on Aug 12, 2010

@author: pascact1
'''

class Card:

    suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rankList = ["Ace", "2", "3", "4", "5", "6", "7",
                "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.rankList[self.rank] + " of " + self.suitList[self.suit])

    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return - 1
        # suits are the same... check ranks 
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return - 1
        # ranks are the same... itÕs a tie 
        return 0
