"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """Check a tic tac toe's board and define a result of a game"""
    # check horizontal
    for line in board:
        if len(set(line)) == 1:
            if line[0] in "ox":
                return line[0] + " wins!"
    # check vertical
    for i in range(3):
        if len(set(line[i] for line in board)) == 1:
            if board[0][i] in "ox":
                return board[0][i] + " wins!"
    # check horizontal top left to bottom right
    if len(set(board[i][i] for i in range(3))) == 1:
        if board[0][0] in "ox":
            return board[0][0] + " wins!"
    # check horizontal bottom right to top left
    if len(set(board[i][2 - i] for i in range(3))) == 1:
        if board[0][-1] in "ox":
            return board[0][-1] + " wins!"

    if str(board).count("-"):
        return "unfinished!"
    return "draw!"


# if __name__ == '__main__':
#     test = [["x", "x", "o"],
#             ["-", "o", "x"],
#             ["x", "x", "o"]]
#
#     print(tic_tac_toe_checker(test)
