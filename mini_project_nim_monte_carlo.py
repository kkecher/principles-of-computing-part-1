"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random
import codeskulptor
codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 10000
NUM_ITEMS = 21

def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    """
    computer_win_fractions = dict()
    for initial_move in range(1, MAX_REMOVE+1):
        computer_win_counter = 0.0
        for _dummy in range(TRIALS):
            computer_win_counter += play_random_game(initial_move, num_items)[0]
        computer_win_fractions[initial_move] = computer_win_counter / TRIALS
    return computer_win_fractions

def play_random_game(initial_move, num_items):
    """
    First move `initial_move` matches from `num_items`.
    Then makes random moves while `num_items` > 0.
    A player wins if his move was last.
    """
    num_items -= initial_move
    is_computer_won = True
    while True:
        if num_items <= 0:
            # Return num_items for testing purpose
            return is_computer_won, num_items
        else:
            is_computer_won = abs(is_computer_won - 1)
            random_move = random.randrange(MAX_REMOVE) + 1
            num_items -= random_move

def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """

    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_win_fractions = evaluate_position(current_items)
        print
        print 'comp_win_fractions =', comp_win_fractions
        # Get the key with max value
        comp_move = max(
            comp_win_fractions, key=lambda key: comp_win_fractions[key]
        )
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print
            print 60*'#'
            print "Computer wins"
            break
        print
        player_move = int(input("Enter your current move"))
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print
            print 60*'#'
            print "Player wins"
            break

#play_game(21)
