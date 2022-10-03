from cgitb import reset
from hashlib import new
import random

# List of Suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# List of Ranks
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Dictionary of values
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# Suit, Rank, Value of Cards
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

#two_hearts = Card("Hearts","Two")
#print(two_hearts.value)

# Deck contains 52 cards
class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create a Card Object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
        
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

new_deck = Deck()
new_deck.shuffle()
mycard = new_deck.deal_one()

print(mycard)
print(len(new_deck.all_cards))



class Player:
    def __init__(self):
        pass
