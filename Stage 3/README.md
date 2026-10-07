Othello — Technical Breakdown

This project implements the board game Othello/Reversi with:
Stage 1: Game components
Stage 2: Flask-based web GUI version 

#stage 1

Module 1: components.py #store the functions components for the app
-------------------------------------
iniitialise_board(size)
The board is present as a 2D list to show the structure of the list, it also reserved 4 center squares for the starting pieces.

START
↓
Set piece strings (Light, Dark, None)
↓
Create empty 2D board filled with None
↓
Calculate center positions
↓
Place 4 starting pieces in center
↓
Return board
END
--------------------------------------
print_board(board)
Uses a nested loop to print the board with row and column numbers, and also the board values.

START
↓
Get board size
↓
Print column headers
↓
FOR each row
Print row number
FOR each column
Print board value
↓
Print blank line
END
--------------------------------------
legal_move(colour, coor, board)
This function is for checking are there any legal moves on the board. Look for empty squares and scan all 8 possible diretions. The square must be next to a opposing piece. Then continue on the same direction and move 1 square each time, until a non-opponent piece is found. Reflecting the rules for 'Outflanking'. 

START
↓
Is selected square empty?
NO → Return False
YES
↓
Determine opponent colour
↓
FOR each direction
Move one step
↓
Is the move within the board?
NO → Next direction
YES
↓
Opponent piece?
NO → Next direction
YES
↓
Move until there is a non-opponent piece
↓
Ends on own piece?
YES → Return True
NO → Next direction
↓
Return False
END
-----------------------------------
apply_move(colour, coor, board)
Outflanked piece must be collected and then filp to the opposite colour.

START
↓
Determine opponent colour
↓
Place piece on board
↓
FOR each direction
Move one step
↓
Opponent piece?
NO → Next direction
YES
↓
Store opponent positions
↓
Ends on own piece?
YES → Flip stored pieces
NO → Discard list
↓
END
-----------------------------------
legal_move_checker(colour, board)
The board is scanned to detect if there are at least 1 legal move exists. Therefore the game can handle passing turns and end game conditions.

START
↓
FOR each row
FOR each column
Is square empty?
NO → Continue
YES
↓
Is legal_move?
YES → Return True
NO → Continue
↓
Return False
END
------------------------------------  
Module 2: game_engine.py
------------------------------------
Validate if the input is correct or not. Using try/excpet to prevent the program from crashing when there is a invalid input.
cli_coords_input() 

START
↓
WHILE True
↓
Ask user for row input
↓
Ask user for column input
↓
Convert inputs to integers (-1)
↓
Is the move inside the board?
YES → Return (coordinates)
NO
↓
Print 'Invalid'
↓
Loop again
EXCEPTION (ValueError)
↓
Print 'Invalid'
↓
Loop again
----------------------------------------
simple_game_loop()
The game is structured as a loop to handle the flow of the program, i.e. passing turns, end game conditions, and present the results of the game.

START
↓
Print 'Welcome message'
↓
Initialise board
Set move_counter = 60
Set current_player = Dark
↓
WHILE move_counter > 0
↓
Print board
Print current player's turn
↓
Does current player have a legal move?
  │    NO
  │     ↓
  │   Does other player have a legal move?
  │   NO → BREAK (Game Over)
  │   YES → Switch player → CONTINUE loop
  │
  └── YES
      ↓
      Get user coordinates
      ↓
      Is move legal?
      NO → Print "Invalid" → CONTINUE
      YES
      ↓
      Apply move
      ↓
      move_counter -= 1
      ↓
      Switch player
      ↓
      END WHILE
      ↓
      Print "Game Over"
      Print final board
      ↓
      Count Dark pieces
      Count Light pieces
      ↓
Compare scores
Dark > Light → Print "Dark wins"
Light > Dark → Print "Light wins"
Equal → Print "Draw"
END
---------------------------------------


#Stage 2

Module 1: flask_game_engine.py
-------------------------------------
#Functions
-------------------------------------
Isolating the player-switching into a single location, preventing inconsistencies when changing routes.
switch_player(player)


START
↓
Is player == "Dark "?
YES → Return "Light"
NO  → Return "Dark "
END
-------------------------------------
Keep the counting separated form the logic, result will be used to determine the winner of the game.
count_pieces(board)

START
↓
Count "Dark " pieces in board
↓
Count "Light" pieces in board
↓
Return (dark_no, light_no)
END
-------------------------------------
#Routes
-------------------------------------
Used for rendering the page of the game.
index()

START
↓
Render index.html
Pass board to template
↓
Return HTML page
END
-------------------------------------
Handle all the validation and game state at the server side. 
move()

START
↓
Read x, y from request
↓
Convert to 0-based index
↓
Are inputs valid integers?
NO → Return JSON fail
YES
↓
Are coordinates inside board?
NO → Return JSON fail
YES
↓
Does current player have legal moves?
NO
↓
Switch player
↓
Does other player have legal moves?
NO
↓
Count pieces
Determine winner
Return finished JSON
YES
↓
Return JSON (player switched)
YES
Is move legal?
NO → Return JSON fail
YES
↓
Apply move
↓
Decrease move_counter
↓
Switch player
↓
Return JSON success
END
---------------------------------------
The game state is stored in a JSON file.
save()

START
↓
Create data dictionary
↓
Open savegame.json (write mode)
↓
Write JSON data
↓
Return JSON status="saved"
END
---------------------------------------
Restores the entire game state in a single operation.
load()

START
↓
Does save file exist?
NO → Return JSON fail
YES
↓
Open save file
↓
Read JSON data
↓
Restore board, player, counter
↓
Return JSON loaded
END
---------------------------------------