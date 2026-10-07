def initialise_board(size=8):
    #state of the empty square
    light = 'Light'
    dark = 'Dark '
    none = 'None '

    board = [[none for _ in range(size)] for _ in range(size)] #setup a empty board with none
    center_1 = size // 2 - 1 #find the center for the starting piece
    center_2 = size // 2
    board[center_1][center_1] = light #starting piece colors
    board[center_2][center_2] = light
    board[center_1][center_2] = dark
    board[center_2][center_1] = dark

    return board

def print_board(board):
    size = len(board)

    print(" ", end="") #set space before the column numbers
    for column in range(size): #print the column numbers
        print(f"{column+1:>6}", end="")
    print()

    for row in range(size): #print the row numbers
        print(f"{row+1:>3} ", end="") 
        for column in range(size):#print the board
            print(f"{board[row][column]:>6}", end="")
        print()

    print()

def legal_move(colour, coor, board):
    size = len(board)
    row, column = coor

    if board[row][column] != 'None ': #check if the square is empty
        return False
    
    if colour == 'Light': #check the colour of the opposing piece
        opponent = "Dark "
    else:
        opponent = "Light"
    
    directions = [(-1, -1), (-1, 0), (-1, 1), ( 0, -1), ( 0, 1), ( 1, -1), ( 1, 0), ( 1, 1)] #all possible directions

    for x, y in directions:
        hm = row + x #horizontal movement
        vm = column + y #vertical movement
        opp_piece = False 

        if not (0 <= hm < size and 0 <= vm < size): #check if the move is inside the board
            continue
        if board[hm][vm] != opponent: #check the next square on that direction a opposing piece or not
            continue

        while 0 <= hm < size and 0 <= vm < size: #keep moving to that direction until meets a non-opposing piece
            if board[hm][vm] == opponent:
                opp_piece = True
                hm += x
                vm += y
            else:
                break

        if opp_piece and 0 <= hm < size and 0 <= vm < size: #check if the piece is our own colour
            if board[hm][vm] == colour:
                return True
            
    return False

def apply_move(colour, coor, board): #function for applying a move and flipping the pieces
    size = len(board)
    row, column = coor

    if colour == "Light":
        opponent = "Dark "
    else:
        opponent = "Light"

    directions = [(-1, -1), (-1, 0), (-1, 1), ( 0, -1), (0, 1),( 1, -1), ( 1, 0), ( 1, 1)]

    board[row][column] = colour  #Place a piece

    for x, y in directions:
        hm = row + x
        vm = column + y
        flip_pieces = [] #empty list to store the piece needed to flip

        if not (0 <= hm < size and 0 <= vm < size):
            continue
        if board[hm][vm] != opponent:
            continue

        while 0 <= hm < size and 0 <= vm < size: #store pieces needed to flip
            if board[hm][vm] == opponent:
                flip_pieces.append((hm, vm))
                hm += x
                vm += y
            else:
                break

        if 0 <= hm < size and 0 <= vm < size and board[hm][vm] == colour: #flip the outflanked pieces
            for flip_x, flip_y in flip_pieces:
                board[flip_x][flip_y] = colour

def legal_move_checker(colour, board): #function for checking is there a legal move and retuni
    size = len(board)
    for hm in range(size):
        for vm in range(size):
            if board[hm][vm] == "None " and legal_move(colour, (hm, vm), board):
                return True
    return False


    




    

