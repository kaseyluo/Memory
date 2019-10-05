# Memory - Design Document

## Instructions: 
-	Type “git clone https://github.com/kaseyluo/Memory.git” in your Terminal
-	Type “python3 memory.py”
-	Follow terminal prompts to continue playing! 

## Rules of Memory:
-	52 Cards are laid face down in a 4 X 13 grid
-	Players go around choosing two cards, flip them over, and see if they match:
  -	a match is defined to be two cards with the same value and same color:
    -	Diamonds + Hearts are both red
    -	Clubs + Spades are both black
    -	Ex: Ace of Diamonds would match with Ace of Hearts 
    -	Ex: 10 of Diamonds would not match with 9 of Diamonds
    -	Ex: 5 of Hearts would not match with 5 of Spades
-	If the cards match, the Player takes the cards out of the grid, leaving two blank slots
-	If the cards do not match, the Player re-flips the cards so that they are face down in the same positions
- Next Player’s turn
- After all the remaining cards in the grid are gone or after players decide to quit, the Player with the most amount of pairs is the winner (there can be more than one winner)

## Design Decisions:
-	Created a Card class in order to keep track of the different elements each card had to capture: suit, value, and whether or not it was matched. I kept the information of whether a card is matched or not tied to the Card class and not in the CardGrid class, because it made sense to keep this information as specific as possible to avoid having a grid of Booleans in the CardGrid class.
-	Created a Player class in order to associate each player’s score and matched cards to their player ID
-	Created a CardGrid class to capture information about how many cards were still “visible” and systematize displaying the grid
-	Board Visualization:
  -	Face-down cards are represented with an “X”
  -	Taken cards are represented with an “O” 
-	Users can interact with the game by specifying the appropriate coordinate corresponding to the card they’d like to inspect. 

## Ways to Improve: 
-	Future iterations would be more dynamic to bad user input. My current implementation takes into account bad user input in two ways:
  -	If the user inputs a coordinate that is out of bounds
  -	If the user wishes to inspect a card that is an “O,” meaning that it is no longer in the grid because it was matched
  Other ways to account for bad user input:
  -	Check that user is abiding by the format of inputting: ‘(row, column); (row, column)’ –the current version assumes proper user input
-	Being constrained to a terminal game makes it difficult but another improvement would be making the user interface more visually appealing with buttons
