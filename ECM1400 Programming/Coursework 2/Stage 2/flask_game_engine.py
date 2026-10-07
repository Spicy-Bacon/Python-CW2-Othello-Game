from flask import Flask, render_template, request, jsonify
from components import (initialise_board, legal_move, apply_move, legal_move_checker)
import json
import os

app = Flask(__name__)


#Gmae status
board = initialise_board()
move_counter = 60
current_player = 'Dark '
SAVE_FILE = 'savegame.json'


#helper functions
def switch_player(player): #function for switching players
    return 'Light' if player == 'Dark ' else 'Dark '


def count_pieces(board): #function for counting pieces
    dark_no = sum(row.count('Dark ') for row in board) #number of dark pieces
    light_no = sum(row.count('Light') for row in board) #number of white pieces
    return dark_no, light_no


#routes
@app.route("/")
def index():
    return render_template('index.html', game_board=board) #pass the borad into the template


@app.route('/move')
def move():
    global board, move_counter, current_player

    #convert to 1 based indexing
    try:
        x = int(request.args.get('x')) - 1 
        y = int(request.args.get('y')) - 1
    except (TypeError, ValueError):
        return jsonify(status='fail', message='Invalid')

    #check if the move is outside the board
    if not (0 <= x < 8 and 0 <= y < 8):
        return jsonify(status='fail', message='Invalid')

    #check for any legal moves
    if not legal_move_checker(current_player, board):
        other_player = switch_player(current_player) #pass turn if there are no legal moves

        if not legal_move_checker(other_player, board):
            dark_no, light_no = count_pieces(board) #count the number of pieces when game over

            if dark_no > light_no: #message when dark won
                result = 'Dark wins!' 
            elif light_no > dark_no: #message when light won
                result = 'Light wins!'
            else:
                result = 'Draw' #message when the result is a draw

            return jsonify(finished=result, board=board)

        current_player = other_player
        return jsonify(status='success', board=board, player=current_player.strip()) #switch players 

    #check if a move is legal
    if not legal_move(current_player, (y, x), board):
        return jsonify(status='fail', message='Invalid')

    #apply the move
    apply_move(current_player, (y, x), board)
    move_counter -= 1 #counting down the remaining moves

    current_player = switch_player(current_player) #switch player

    return jsonify(status='success', board=board, player=current_player.strip())


#write JSON file
@app.route('/save')
def save():
    data = {'board': board, 'current_player': current_player, 'move_counter': move_counter}

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return jsonify(status="saved")


#read JSON file
@app.route('/load')
def load():
    global board, current_player, move_counter

    if not os.path.exists(SAVE_FILE):
        return jsonify(status='fail', message='No save file')

    with open(SAVE_FILE, 'r') as f:
        data = json.load(f)

    board = data['board']
    current_player = data['current_player']
    move_counter = data['move_counter']

    return jsonify(
        status='loaded',
        board=board,
        player=current_player.strip()
    )

if __name__ == '__main__':
    app.run(debug=True)

