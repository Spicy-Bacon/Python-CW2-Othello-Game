import pytest
from components import (initialise_board, legal_move, apply_move, legal_move_checker)
#test initialise_board()
def test_initialise_board_size():
    board = initialise_board()
    assert len(board) == 8
    assert all(len(row) == 8 for row in board)


def test_initialise_board_starting_pieces():
    board = initialise_board()
    assert board[3][3] == 'Light'
    assert board[4][4] == 'Light'
    assert board[3][4] == 'Dark '
    assert board[4][3] == 'Dark '


#test legal_move()
def test_legal_move_valid():
    board = initialise_board()
    assert legal_move('Dark ', (2, 3), board) is True


def test_legal_move_invalid():
    board = initialise_board()
    assert legal_move('Dark ', (0, 0), board) is False


#test apply_move()
def test_apply_move_flips_piece():
    board = initialise_board()
    apply_move('Dark ', (2, 3), board)

    assert board[3][3] == 'Dark '


#test legal_move_checker()
def test_legal_move_checker_true():
    board = initialise_board()
    assert legal_move_checker('Dark ', board) is True


def test_legal_move_checker_false():
    board = [['Dark ']*8 for _ in range(8)]
    assert legal_move_checker('Light', board) is False

