from homework7.board import tic_tac_toe_checker


def test_is_x_winner_when_there_are_3_x_in_a_row():
    board = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_is_o_winner_when_there_are_3_o_in_a_column():
    board = [["x", "-", "o"], ["-", "o", "o"], ["x", "x", "o"]]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_is_x_winner_when_there_a_diagonal_of_x():
    board = [["x", "o", "-"], ["o", "x", "-"], ["-", "o", "x"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_is_o_winner_when_there_a_diagonal_of_o():
    board = [["-", "x", "o"], ["x", "o", "-"], ["o", "o", "x"]]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_is_unfinished_when_there_are_no_winners_and_the_game_can_be_continued():
    board = [["x", "o", "-"], ["o", "x", "-"], ["-", "o", "-"]]
    assert tic_tac_toe_checker(board) == "unfinished!"


def test_is_draw_when_there_are_no_winner_and_the_board_is_filled():
    board = [["x", "o", "x"], ["x", "x", "o"], ["o", "x", "o"]]
    assert tic_tac_toe_checker(board) == "draw!"
