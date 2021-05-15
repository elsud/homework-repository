"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Tic_tac_toe_checker checks if there are some winners.
If there is "x" winner, function returns "x wins!"
If there is "o" winner, function returns "o wins!"
If there is a draw, function returns "draw!"
If board is unfinished, function returns "unfinished!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """Checking if there're any winner."""

    def check_one_player(player: str) -> bool:
        """Checking if player is a winner."""
        win = [player] * 3
        if any(row == win for row in board):
            return True
        if any(
            column == win
            for column in ([board[0][i], board[1][i], board[2][i]] for i in range(3))
        ):
            return True
        if board[1][1] == player == board[0][0] == board[2][2]:
            return True
        if board[1][1] == player == board[0][2] == board[2][0]:
            return True
        return False

    if check_one_player("x"):
        return "x wins!"
    if check_one_player("o"):
        return "o wins!"
    if any("-" in row for row in board):
        return "unfinished!"
    return "draw!"
