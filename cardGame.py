import enum

class Number(enum.Enum):
	TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN = range(2, 11)
	JACK, QUEEN, KING, ACE = 'J', 'Q', 'K', 'A'

class Suit(enum.Enum):
	# Red Suits: Hearts and Diamonds
	# Black Suits: Clubs and Spades
	CLUBS, HEARTS, DIAMONDS, SPADES = 'C', 'H', 'D', 'S' 

class Card:
	def __init__(self, suit, number, isMatched = False):
		self.suit = suit
		self.number = number
		self.isMatched = isMatched

	def describeSelf(self):
		# format is "[value]-[suit]""
		description = str(self.number.value) + "-"  + self.suit.value
		if len(description) < 4: description += " " #add an extra space for formatting purposes
		return description

	def isAMatch(self, card):
		#if the cards are the same color and the same value, that means it's a match
		return (((self.suit.value == 'H' or self.suit.value == 'D') and (card.suit.value == 'H' or card.suit.value == 'D')) or ((self.suit.value == 'C' or self.suit.value == 'S') and (card.suit.value == 'C' or card.suit.value == 'S')))  and (self.number.value == card.number.value)