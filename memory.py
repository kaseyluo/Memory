from memoryComponents import Player, generateDeck, CardGrid
from ast import literal_eval

def createPlayers(numPlayers): #takes in # of players and returns a list of Player objects
	players = []
	for i in range(numPlayers):
		players.append(Player(i + 1))
	return players

def printGameUpdate(grid, playerIndex, players):
	print("There are ", grid.cardsLeft, " cards left in the game.")
	print("Player ", playerIndex + 1, "has ", players[playerIndex].numPairs, "pairs.")
	players[playerIndex].printPairs()

def determineWinners(players):
	# first, figure out the max number of pairs that a player collected
	maxNumPairs = players[0].numPairs
	winner = players[0]
	for player in players:
		if player.numPairs > maxNumPairs:
			maxNumPairs = player.numPairs
			winner = player
	# make sure to account for if there's a tie
	winners = [winner]
	for player in players:
		if player.numPairs == maxNumPairs and player is not winner:
			winners.append(player)
	return winners

def printAboutWinners(winners):
	if len(winners) == 1:
		print("The winner is Player ", winners[0].playerID, " with ", winners[0].numPairs, " matches!")
	else:
		print("There was a tie! Winners are: ")
		for w in winners:
			print("Player ", w.playerID, " with ", w.numPairs, " matches!") 

def playMemory():
	print("Welcome to the game of Memory!")
	numPlayers = int(input("How many players? Enter here: "))
	players = createPlayers(numPlayers) #list of player objects
	print("Cool! Setting up the game for ", numPlayers, "players....")
	print("Here is your randomly generated board. 'X' means there is a card, and 'O' means the spot is empty")
	deck = generateDeck()
	grid = CardGrid(deck)
	grid.createBoard()
	grid.displayTrueGrid() #TODO: remove later
	grid.displayGrid()

	while not grid.isGameOver():
		for playerIndex in range(numPlayers):
			# ---------------------- GET USER INPUT AND MAKE SURE IT'S VALID INPUT ------------------------------
			if grid.isGameOver(): break # need this line in case the game is over in the middle of this for loop
			c1, c2  = input("Player " + str(playerIndex + 1) + ", which two cards would you like to inspect? [Format: '(row, column); (row, column)']. Enter here or type 'q;' to quit: ").split(";")
			if c1 == "q":
				grid.cardsLeft = 0
				break
			coord1 = literal_eval(c1)
			coord2 = literal_eval(c2)

			#check that coord1 and coord2 are in range
			while (coord1[0] > 3 or coord2[0] > 3 or coord1[0] < 0 or coord2[0] < 0 or coord1[1] > 12 or coord2[1] > 12 or coord1[1] < 0 or coord2[1] < 0):
				print("One or more of the cards you selected is out of bounds.")
				c1, c2  = input("Player " + str(playerIndex + 1) + ", which two cards would you like to inspect? [Format: '(row, column); (row, column)']. Enter here or type 'q;' to quit: ").split(";")
				if c1 == "q":
					grid.cardsLeft = 0
					break
				coord1 = literal_eval(c1)
				coord2 = literal_eval(c2)
			
			if grid.isGameOver(): break
			card1 = grid.grid[int(coord1[0])][int(coord1[1])]
			card2 = grid.grid[int(coord2[0])][int(coord2[1])]

			#check to make sure these cards were not already selected
			while (card1.isMatched) or (card2.isMatched):
				print("One or more of the cards you selected was already matched. ")
				c1, c2  = input("Player " + str(playerIndex + 1) + ", which two cards would you like to inspect? [Format: '(row, column); (row, column)']. Enter here or type 'q;' to quit: ").split(";")
				if c1 == "q":
					grid.cardsLeft = 0
					break
				coord1 = literal_eval(c1)
				coord2 = literal_eval(c2)

				#check that coord1 and coord2 are in range
				while(coord1[0] > 3 or coord2[0] > 3 or coord1[0] < 0 or coord2[0] < 0 or coord1[1] > 12 or coord2[1] > 12 or coord1[1] < 0 or coord2[1] < 0):
					print("One or more of the cards you selected is out of bounds.")
					c1, c2  = input("Player " + str(playerIndex + 1) + ", which two cards would you like to inspect? [Format: '(row, column); (row, column)']. Enter here or type 'q;' to quit: ").split(";")
					if c1 == "q":
						grid.cardsLeft = 0
						break
					coord1 = literal_eval(c1)
					coord2 = literal_eval(c2)
	
				
				if grid.isGameOver(): break
				card1 = grid.grid[int(coord1[0])][int(coord1[1])]
				card2 = grid.grid[int(coord2[0])][int(coord2[1])]
			# ------------------------------------------------------------------------------------------------------------------------------------------------------------

			if grid.isGameOver(): break
			#show the grid with the revealed cards
			grid.displayGrid(True, coord1, coord2)

			#state whether it's a match or not
			if card1.isAMatch(card2):
				print("It's a match!")

				#decrement cards left, change isMatched to be true, update corresponding player's information
				grid.cardsLeft -= 2
				card1.isMatched = True
				card2.isMatched = True
				players[playerIndex].numPairs += 1
				players[playerIndex].matches.append((card1, card2))
			else:
				print("No match!")
			printGameUpdate(grid, playerIndex, players)
			grid.displayGrid()
			grid.displayTrueGrid() #TODO: remove this later

	#determine which player is the winner
	winners = determineWinners(players)
	printAboutWinners(winners)

playMemory()
	