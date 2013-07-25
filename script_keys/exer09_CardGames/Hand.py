'''
Created on Aug 12, 2010

@author: pascact1
'''

class Hand(Deck):
    pass

    def __init__(self, name = ""):
        self.cards = []
        self.name = name

    def addCard(self, card):
        self.cards.append(card)

    def deal(self, hands, nCards = 999):
        nHands = len(hands)
        for i in range(nCards):
            if self.isEmpty():
                break # break if out of cards
            card = self.popCard() # take the top card
            hand = hands[i % nHands] # whose turn is next?
            hand.addCard(card) # add the card to the hand

    # if next function not in code Deck __str__ would be called

    def __str__(self):
        s = "Hand " + self.name
        if self.isEmpty():
            return s + " is empty\n"
        else:
            return s + " contains\n" + Deck.__str__(self)
