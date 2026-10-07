from components import initialise_board, print_board, legal_move, apply_move, legal_move_checker
def cli_coords_input():
    while True:
        try:
            row = int(input("Enter row 1-8: ")) - 1 #input the coordinates
            
            column = int(input("Enter column 1-8: ")) - 1

            if 0 <= row < 8 and 0 <= column < 8: #for if the input is valid
                return (row, column)
            else:
                print('You must enter number between 1 to 8.') #error message when number is not 1-8
        
        except ValueError:
            print('You must enter numbers') #error message when input is anything other then a number

def simple_game_loop():
    print('Welcome to Othello!')

    board = initialise_board()
    move_counter = 60 #there are 60 moves maximum in a game, since the grid is 64 squares, and there are 4 starting pieces
    current_player = "Dark "

    while move_counter > 0: #game loop
        print_board(board)
        print(f"{current_player.strip()}'s turn.") #display which player's turn

        if not legal_move_checker(current_player, board): #check for legal move
            print('You have no legal moves, passing turn.')
            other_player = 'Light' if current_player == 'Dark ' else 'Dark ' #pass turn if there are no legal move
            
            if not legal_move_checker(other_player, board): #end the game when there is no legal move for both players
                print('Game Over')
                break

            current_player = other_player #switching players if there is a legal move
            continue

        coor = cli_coords_input() #enter the coordinates

        if not legal_move(current_player, coor, board): #check if the move is legal
            print('Invalid move')
            continue

        apply_move(current_player, coor, board) #apply the move if its legal
        move_counter -= 1 #counting down the remaining moves
        current_player = 'Light' if current_player == 'Dark ' else 'Dark ' #switch players

    print('Game Over!') #end the game when there are no more moves
    print_board(board)

    #show the piece count for both sides
    dark_no = sum(row.count('Dark ') for row in board) 
    light_no = sum(row.count('Light') for row in board)

    print(f'Dark: {dark_no}')
    print(f'Light: {light_no}')

    if dark_no > light_no: #check which colour has more pieces
        print('Dark wins!')
    elif light_no> dark_no:
        print('Light wins!')
    else:
        print('Draw')

if __name__ == '__main__':
    simple_game_loop()