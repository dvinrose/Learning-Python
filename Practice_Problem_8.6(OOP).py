'''
 Implement overloaded operators repr() and == for the Card class. Your new Card class
 should behave as shown:

  Card('3', ' ') == Card('3', ' ')
 True

 Card('3', ' ') == eval(repr(Card('3', ' ')))
 True
'''


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

    def __eq__(self, other):
        """Two cards are equal if they have the same rank and suit."""
        if not isinstance(other, Card):
            return False
        return (self.rank, self.suit) == (other.rank, other.suit)

    def __repr__(self):
        """Canonical string representation that can be eval’d back into a Card."""
        return f"Card({self.rank!r}, {self.suit!r})"

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

Card('3', ' ') == Card('3', ' ')


repr(Card('3', ' '))
"Card('3', ' ')"

eval(repr(Card('3', ' ')))
Card('3', ' ')

Card('3', ' ') == eval(repr(Card('3', ' ')))

'''
No es estrictamente necesario entender sobrecarga de operadores para comprender la
 herencia en programación orientada a objetos, pero conocerlo puede ayudar.

🔹 Herencia: Permite que una clase hija herede atributos y métodos de
 una clase padre, facilitando la reutilización de código.

🔹 Sobrecarga de operadores: Permite redefinir operadores (+, *, ==, etc.) 
para que funcionen con objetos personalizados.

✅ ¿Cómo se conectan? Si una clase padre tiene operadores 
sobrecargados (__add__(), __eq__(), etc.),
 la clase hija hereda esos métodos y puede sobrescribirlos 
 si necesita cambiar su comportamiento.
 '''