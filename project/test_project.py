import pytest
from io import StringIO
from contextlib import redirect_stdout

from test import winner, gameover, display_board

def test_winner():
    global sideA, sideB, board
    # Test Case 1: Side A wins horizontally
    sideA = [0, 1, 2]
    sideB = []
    board = ['X', 'X', 'X', '-', '-', '-', '-', '-', '-']
    assert winner() == 1

    # Test Case 2: Side B wins diagonally
    sideA = []
    sideB = [0, 4, 8]
    board = ['O', '-', '-', '-', 'O', '-', '-', '-', 'O']
    assert winner() == -1

    # Test Case 3: Draw
    sideA = [0, 1, 4, 5, 6]
    sideB = [2, 3, 7, 8]
    board = ['X', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'O']
    assert winner() == 0

    # Test Case 4: Game is ongoing
    sideA = [0, 1]
    sideB = [4, 8]
    board = ['X', 'X', '-', '-', 'O', '-', '-', '-', 'O']
    assert winner() is None

def test_gameover():
    global sideA, sideB, board
    # Test Case 1: Game is over (winner exists)
    sideA = [0, 1, 2]
    sideB = []
    board = ['X', 'X', 'X', '-', '-', '-', '-', '-', '-']
    assert gameover() is True

    # Test Case 2: Game is over (draw)
    sideA = [0, 1, 4, 5, 6]
    sideB = [2, 3, 7, 8]
    board = ['X', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'O']
    assert gameover() is True

    # Test Case 3: Game is ongoing
    sideA = [0, 1]
    sideB = [4, 8]
    board = ['X', 'X', '-', '-', 'O', '-', '-', '-', 'O']
    assert gameover() is False

def test_display_board():
    global board
    # Test Case: Board display
    board = ['X', 'X', 'O', 'O', '-', '-', '-', '-', '-']
    expected_output = """X | X | O
                            --+---+--
                            O | - | -
                            --+---+--
                            - | - | -
                            """
    with StringIO() as buf, redirect_stdout(buf):
        display_board()
        output = buf.getvalue()
    assert output == expected_output
