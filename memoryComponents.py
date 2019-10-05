from cardGame import Number, Suit, Card
import random

class Player:
	def __init__(self, playerID):
		self.playerID = playerID
		self.numPairs = 0
		self.matches = [] #array of tuples, where each tuple represents a matching pair of cards

	def printPairs(self): #used to determine number of matched pairs player has
		for i in range(len(self.matches)): 
			match = self.matches[i]
			print("Pair ", i + 1, ": (", match[0].describeSelf(), ", ", match[1].describeSelf(), ")")
 
class CardGrid:
	def __init__(self, deck, grid = [[' ' for i in range(13)] for j in range(4)], cardsLeft = 52):
		self.deck = deck
		self.grid = grid
		self.cardsLeft = cardsLeft

	def createBoard(self):
		for i in range(4):
			for j in range(13):
				self.grid[i][j] = self.deck.pop(0)

	def isGameOver(self):
		return self.cardsLeft == 0

	def displayGrid(self, showSelected = False, card1 = None, card2 = None):
		introRow = "    "
		for i in range(13): 
			if len(str(i)) == 1: introRow += str(i) + "    "
			else: introRow += str(i) + "   "
		print(introRow)
		print("-----------------------------------------------------------------")


		for r in range(len(self.grid)):
			rowString = str(r) + " | "
			for c in range(len(self.grid[r])):
				card = self.grid[r][c]
				if showSelected and ((r == card1[0] and c == card1[1]) or (r == card2[0] and c == card2[1])):
					rowString += card.describeSelf() + " "
				elif card.isMatched: #'0' means that the card at this spot was already matched and removed
					rowString += "O    "
				else: #'X' means that the card is flipped over and unidentifiable
					rowString += "X    "
			print(rowString)


	def displayTrueGrid(self): #debugging function that shows where all the cards are 
		introRow = "    "
		for i in range(13): 
			if len(str(i)) == 1: introRow += str(i) + "    "
			else: introRow += str(i) + "   "
		print(introRow)
		print("-----------------------------------------------------------------")

		for i in range(len(self.grid)):
			row = self.grid[i]
			rowString = str(i) + " | "
			for card in row:
				rowString += card.describeSelf() + "  "
			print(rowString)

def generateDeck(): #creates an array of all the cards
	deck = []
	for s in Suit:
		for n in Number:
			deck.append(Card(s, n))
	shuffledDeck = random.sample(deck, len(deck)) #shuffles cards in the deck
	return shuffledDeck
