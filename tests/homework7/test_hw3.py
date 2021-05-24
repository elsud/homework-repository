"""Test homework7.hw3"""

from homework7.hw3 import tic_tac_toe_checker


def test_example_1():
    """test from example"""
    unfinished_board = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]

    assert tic_tac_toe_checker(unfinished_board) == "unfinished!"


def test_example_2():
    """test from example"""
    board = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_x_wins():
    """Test when "x" wins. Horizontal win"""
    board = [["x", "o", "x"], ["-", "o", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_o_wins():
    """Test when "o" win. Vertical win"""
    board = [["o", "x", "o"], ["o", "x", "x"], ["o", "-", "x"]]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_win_diagonal_1():
    """Test win on top left to bottom right diagonal"""
    board = [["x", "o", "o"], ["-", "x", "o"], ["x", "-", "x"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_wins_diagonal_2():
    """Test win on bottom left to top right diagonal"""
    board = [["x", "x", "o"], ["-", "o", "o"], ["o", "-", "x"]]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_unfinished():
    """Test when game unfinished"""
    board = [["x", "x", "o"], ["-", "o", "x"], ["x", "x", "o"]]
    assert tic_tac_toe_checker(board) == "unfinished!"


def test_draw():
    """Test draw"""
    board = [["x", "x", "o"], ["o", "o", "x"], ["x", "x", "o"]]
    assert tic_tac_toe_checker(board) == "draw!"
