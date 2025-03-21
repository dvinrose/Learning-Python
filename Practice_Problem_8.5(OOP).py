'''
 Modify the constructor of the class Deck so that the class can also be used for card games
 that do not use the standard deck of 52 cards. For such games, we would need to provide the
 list of cards explicitly in the constructor. Here is a somewhat artificial example:

 deck = Deck(['1', '2', '3', '4'])
 deck.shuffle()
 deck.dealCard()
 '3'
 deck.dealCard()
 '1'
'''

'''
from random import shuffle
# ------------------------------------------------------------------------------
class Card:
    """Represents a playing card."""

    def __init__(self, rank, suit):
        """Initialize rank and suit of the playing card."""
        self.rank = rank
        self.suit = suit

    def getRank(self):
        """Return the rank of the card."""
        return self.rank

    def getSuit(self):
        """Return the suit of the card."""
        return self.suit
# ------------------------------------------------------------------------------
class Deck:
    """Represents a deck of 52 cards"""

    # Ranks and suits are Deck class variables
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    # Suits is a set of 4 Unicode symbols representing the 4 suits
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        """Initialize deck of 52 cards"""
        self.deck = []  # Deck is initially empty

        for suit in Deck.suits:  # Suits and ranks are Deck class variables
            for rank in Deck.ranks:
                # Add Card with given rank and suit to deck
                self.deck.append(Card(rank, suit))
                print(rank, suit)

        #for card in self.deck:

    def deal_card(self):
        """Deal (pop and return) card from the top of the deck"""
        return self.deck.pop()

    def shuffle(self):
        """Shuffle the deck"""
        shuffle(self.deck)

# ------------------------------------------------------------------------------

a = Deck()

'''

#00000000000000000000000000000000000000000000000000000000000000000000

from random import shuffle

class Card:
    """Represents a playing card."""

    def __init__(self, rank, suit=None):
        """Initialize rank and suit of the playing card."""
        self.rank = rank
        self.suit = suit

    def getRank(self):
        """Return the rank of the card."""
        return self.rank

    def getSuit(self):
        """Return the suit of the card."""
        return self.suit

class Deck:
    """Represents a deck of 52 cards, or a custom set of cards."""

    # Ranks and suits are Deck class variables
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self, cardList=None):
        """Initialize the deck."""
        if cardList is not None:  # If a custom list of cards is provided
            self.deck = [Card(rank) for rank in cardList]  # Create cards using the custom ranks
        else:  # Initialize a standard 52-card deck
            self.deck = []  # Deck is initially empty
            for suit in Deck.suits:  # Suits and ranks are Deck class variables
                for rank in Deck.ranks:
                    self.deck.append(Card(rank, suit))

    def deal_card(self):
        """Deal (pop and return) card from the top of the deck."""
        return self.deck.pop()

    def shuffle(self):
        """Shuffle the deck."""
        shuffle(self.deck)

# Example usage:
custom_deck = Deck(['0', '9', '8', '4'])
custom_deck.shuffle()
print(custom_deck.deal_card().getRank())  # E.g., '3'
print(custom_deck.deal_card().getRank())  # E.g., '1'
