#!/usr/bin/env python2

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

def mc_trial(board, player):
    """
    This function takes a current board in the form TTTBoard class object,
    the next player to move in the form `provided.PLAYERX` or `provided.PLAYERO`
    The function should play a game starting with the given player by making
    random moves, alternating between players. The function should return when
    the game is over. The modified board will contain the state of the game, so
    the function does not return anything. In other words, the function should
    modify the `board` input.4

    `get_winner_code(board)` function returns one of the values:
        2 if PLAYERX won
        3 if PLAYERO won
        4 if DRAW
        None if game is in progress
    """
    while not get_winner_code(board):
        empty_squares = board.get_empty_squares()
        empty_square = random.choice(empty_squares)
        board.move(empty_square[0], empty_square[1], player)
        player = provided.switch_player(player)
    return

def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores in the form list of lists with the same
    dimensions as the Tic-Tac-Toe board, a board from a completed game (TTTBoard
    class object), and which player the machine player is (in the form
    `provided.PLAYERX` or `provided.PLAYERO`). The function should score the
    completed board and update the scores grid. As the function updates the
    scores grid directly, it does not return anything.

    Method `board.square(self, row, col)` returns:
        1 if the cell is EMPTY
        2 if the cell is PLAYERX
        3 if the cell is PLAYERO
    """
    player_code = convert_player_to_player_code(player)
    winner_code = get_winner_code(board)
    looser_code = get_looser_code(board)
    if player_code == winner_code:
        score_current = SCORE_CURRENT
        score_other = -SCORE_OTHER
    elif player_code == looser_code:
        score_current = -SCORE_CURRENT
        score_other = SCORE_OTHER
    else:
        score_current = 0
        score_other = 0
    board_dim = board.get_dim()
    for row in range(board_dim):
        for col in range(board_dim):
            square_code = board.square(row, col)
            if square_code == player_code:
                scores[row][col] += score_current
            elif square_code != 1:
                scores[row][col] += score_other
    return

def get_winner_code(board):
    """
    Takes a completed board and get the winner_code

    `provided.check_win` method returns one of the values:
        2 if PLAYERX won
        3 if PLAYERO won
        4 if DRAW
        None if game is in progress
    """
    return board.check_win()

def get_looser_code(board):
    """
    Takes a completed board and get the looser_code
    """
    match_winner_to_looser_codes = {2: 3, 3: 2, 4: 4}
    winner_code = get_winner_code(board)
    looser_code = match_winner_to_looser_codes[winner_code]
    return looser_code

def convert_player_code_to_player(player_code):
    """
    Get the player from player code according the table:
        provided.PLAYERX if player_code is 2
        provided.PLAYERO if player_code is 3
        'DRAW' if player_code is 4
    """
    player_codes = {2: provided.PLAYERX, 3: provided.PLAYERO, 4: 'DRAW'}
    return player_codes[player_code]

def convert_player_to_player_code(player):
    """
    Get the player from player code according the table:
        2 if player is provided.PLAYERX
        3 if player is provided.PLAYERO
        4 if player is 'DRAW'
    """
    players = {provided.PLAYERX: 2, provided.PLAYERO: 3, 'DRAW': 4}
    return players[player]

def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores.
    The function should find all of the empty squares with the maximum score and
    randomly return one of them as a (row, column) tuple.
    It is an error to call this function with a board that has no empty squares
    (there is no possible next move), so your function may do whatever it wants
    in that case. The case where the board is full will not be tested.

    Method `board.square(self, row, col)` returns:
        1 if the cell is EMPTY
        2 if the cell is PLAYERX
        3 if the cell is PLAYERO
    """
    copy_scores = [list(row) for row in scores]
    while True:
        max_in_rows = dict(enumerate(map(max, copy_scores)))
        max_row_index = max(max_in_rows, key=lambda key: max_in_rows[key])
        max_row = scores[max_row_index]
        max_col_index = max(range(len(max_row)), key=max_row.__getitem__)
        if board.square(max_row_index, max_col_index) == 1:
            return max_row_index, max_col_index
        else:
            copy_scores[max_row_index][max_col_index] = 0

def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, and
    the number of trials to run. The function should use the Monte Carlo
    simulation described above to return a move for the machine player in the
    form of a (row, column) tuple.
    Be sure to use the other functions you have written!
    """
    pass


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
