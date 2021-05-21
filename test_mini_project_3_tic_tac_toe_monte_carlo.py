#!/usr/bin/env python2

"""
Tests for mini-project #4 - Tic-Tac-Toe (Monte Carlo)
"""

import poc_simpletest
import random
import user48_gUfH3o6E9k_35 as ttt
import poc_ttt_provided as provided

def test_mc_trial_if_both_players_played():
    """
    Test if both players played in 'mc_trial'  method.
    """
    print 'Testing mc_trial_if_both_players_played\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    number_of_squares_cases = [2, 3, 8, 10, 13]

    for number_of_squares in number_of_squares_cases:
        for player in [provided.PLAYERX, provided.PLAYERO]:
            board = provided.TTTBoard(number_of_squares)
            ttt.mc_trial(board, player)
            tests.run_test(
                'O' in str(board) and 'X' in str(board),
                True,
                'test_mc_trial_if_both_players_played #'
                + str(test_counter) + ': '
            )
            test_counter += 1

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_mc_trial_if_game_finished():
    """
    Test if game was finished in 'mc_trial'  method.

    'provided.check_win' method returns one of the values:
        2 if PLAYERX won
        3 if PLAYERO won
        4 if DRAW
        None if game is in progress
    """
    print 'Testing mc_trial_if_game_finished\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    valid_check_win_returns = (2, 3, 4)
    number_of_squares_cases = [0, 1, 3, 8, 10, 13]

    for number_of_squares in number_of_squares_cases:
        for player in [provided.PLAYERX, provided.PLAYERO]:
            board = provided.TTTBoard(number_of_squares)
            ttt.mc_trial(board, player)
            tests.run_test(
                board.check_win() in valid_check_win_returns,
                True,
                'test_mc_trial # ' + str(test_counter) + ': '
            )
            test_counter += 1

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_get_winner_code():
    """
    Test if a valid winner_code was got.

    Valid winner codes:
        2 if PLAYERX won
        3 if PLAYERO won
        4 if DRAW
    """
    print 'Testing get_winner_code\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    number_of_squares_cases = [2, 3, 8, 10, 13]
    valid_winner_codes = [2, 3, 4]

    for number_of_squares in number_of_squares_cases:
        for player in [provided.PLAYERX, provided.PLAYERO]:
            board = provided.TTTBoard(number_of_squares)
            ttt.mc_trial(board, player)
            winner_code = ttt.get_winner_code(board)
            tests.run_test(
                winner_code in valid_winner_codes,
                True,
                'test_get_winner_code #' + str(test_counter) + ': '
            )
            test_counter += 1

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_get_looser_code():
    """
    Test if a valid looser_code was got.

    Valid looser codes:
        2 if PLAYERX lost
        3 if PLAYERO lost
        4 if DRAW
    """
    print 'Testing get_looser_code\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    number_of_squares_cases = [2, 3, 8, 10, 13]

    for number_of_squares in number_of_squares_cases:
        for player in [provided.PLAYERX, provided.PLAYERO]:
            board = provided.TTTBoard(number_of_squares)
            ttt.mc_trial(board, player)
            winner_code = ttt.get_winner_code(board)
            if winner_code == 2:
                test_looser_code = 3
            elif winner_code == 3:
                test_looser_code = 2
            elif winner_code == 4:
                test_looser_code = 4

            ttt_looser_code = ttt.get_looser_code(board)
            tests.run_test(
                ttt_looser_code,
                test_looser_code,
                'test_get_looser_code #' + str(test_counter) + ': '
            )
            test_counter += 1

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_convert_player_code_to_player():
    """
    Test if the player_code was converted to winner correctly.

        provided.PLAYERX if player_code is 2
        provided.PLAYERO if player_code is 3
        'DRAW' if player_code is 4
    """
    print 'Testing convert_player_code_to_player\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    valid_data = {2: provided.PLAYERX, 3: provided.PLAYERO, 4: 'DRAW'}

    for player_code in valid_data:
        tests.run_test(
            ttt.convert_player_code_to_player(player_code),
            valid_data[player_code],
            'test_convert_player_code_to_player #' + str(test_counter) + ': '
        )
        test_counter += 1

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_convert_player_to_player_code():
    """
    Test if the player was converted to player_code correctly.

        2 if player is provided.PLAYERX
        3 if player is provided.PLAYERO
        4 if player is 'DRAW'
    """
    print 'Testing convert_player_to_player_code\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    valid_data = {provided.PLAYERX: 2, provided.PLAYERO: 3, 'DRAW': 4}

    for player in valid_data:
        tests.run_test(
            ttt.convert_player_to_player_code(player),
            valid_data[player],
            'test_convert_player_code_to_player #' + str(test_counter) + ': '
        )
        test_counter += 1

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_mc_update_scores():
    """
    Test if 'mc_update_scores' updated squares scores correctly.

    method 'board.square(self, row, col)' returns:
        1 if the cell is EMPTY
        2 if the cell is PLAYERX
        3 if the cell is PLAYERO
    """
    print 'Testing mc_update_scores\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    number_of_squares_cases = [2, 3, 8, 10, 13]
    number_of_checks_squares = 10
    machine_player = provided.PLAYERX

    for number_of_squares in number_of_squares_cases:
        for player in [provided.PLAYERX, provided.PLAYERO]:
            scores = [[0]*number_of_squares for\
                      dummy in range(number_of_squares)]
            board = provided.TTTBoard(number_of_squares)
            ttt.mc_trial(board, player)
            ttt.mc_update_scores(scores, board, machine_player)

            #Check if the 'scores' was updated correctly

            #'ttt.get_winner_code(board)' returns one of the values:
            #    2 if PLAYERX won
            #    3 if PLAYERO won
            #    4 if DRAW
            #    None if game is in progress
            winner_code = ttt.get_winner_code(board)
            looser_code = ttt.get_looser_code(board)
            for dummy in range(
                    min(number_of_squares, number_of_checks_squares)
            ):
                row = random.randrange(number_of_squares)
                col = random.randrange(number_of_squares)
                square_code = board.square(row, col)
                if square_code == winner_code and winner_code != looser_code:
                    tests.run_test(
                        scores[row][col],
                        1,
                        'test_mc_update_scores #' +  str(test_counter) + ': '
                    )
                elif square_code == looser_code and winner_code != looser_code:
                    tests.run_test(
                        scores[row][col],
                        -1,
                        'test_mc_update_scores #' + str(test_counter) + ': '
                    )
                elif square_code == 1 or winner_code == looser_code:
                    tests.run_test(
                        scores[row][col],
                        0,
                        'test_mc_update_scores #' + str(test_counter) + ': '
                    )
                else:
                    raise Exception(
                        'Uncaught condition at test_mc_update_scores function'
                    )

            test_counter += 1

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_get_best_move_if_max_is_not_empty():
    """
    Test if the second best move was chosen if max is not empty.
    """
    print 'Testing get_best_move_if_max_is_not_empty\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    number_of_squares_cases = [2, 7, 8]

    for number_of_squares in number_of_squares_cases:
        board = provided.TTTBoard(number_of_squares)
        scores = [[0]*number_of_squares for dummy in range(number_of_squares)]
        best_row = random.randrange(number_of_squares)
        best_col = random.randrange(number_of_squares)
        scores[best_row][best_col] = 2
        player = random.choice([provided.PLAYERX, provided.PLAYERO])
        board.move(best_row, best_col, player)
        while True:
            second_best_row = random.randrange(number_of_squares)
            second_best_col = random.randrange(number_of_squares)
            if second_best_row != best_row or second_best_col != best_col:
                break
        scores[second_best_row][second_best_col] = 1
        best_move = ttt.get_best_move(board, scores)
        tests.run_test(
            best_move,
            (second_best_row, second_best_col),
            'test_get_best_move_if_max_is_not_empty # ' +
            str(test_counter) + ': '
        )
        test_counter += 1

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_get_best_move_if_max_is_empty():
    """
    Test if the best move was chosen if max is empty.
    """
    print 'Testing get_best_move_if_max_is_empty\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    number_of_squares_cases = [2, 7, 8]

    for number_of_squares in number_of_squares_cases:
        board = provided.TTTBoard(number_of_squares)
        scores = [[0]*number_of_squares for dummy in range(number_of_squares)]
        best_row = random.randrange(number_of_squares)
        best_col = random.randrange(number_of_squares)
        scores[best_row][best_col] = 2
        while True:
            second_best_row = random.randrange(number_of_squares)
            second_best_col = random.randrange(number_of_squares)
            if second_best_row != best_row or second_best_col != best_col:
                break
        scores[second_best_row][second_best_col] = 1
        best_move = ttt.get_best_move(board, scores)
        tests.run_test(
            best_move,
            (best_row, best_col),
            'test_get_best_move_if_max_is_empty # ' +
            str(test_counter) + ': '
        )
        test_counter += 1

    tests.report_results()
    print
    return tests.total_tests, tests.failures


def test_get_best_move_if_two_equal_maxes_and_both_are_empty():
    """
    Test if the best move was chosen if two equal maxes and one is empty.
    """
    print 'Testing get_best_move_if_two_equal_maxes_and_one_is_empty\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    number_of_squares_cases = [2, 7, 8]

    for number_of_squares in number_of_squares_cases:
        board = provided.TTTBoard(number_of_squares)
        scores = [[0]*number_of_squares for dummy in range(number_of_squares)]
        best_row = random.randrange(number_of_squares)
        best_col = random.randrange(number_of_squares)
        scores[best_row][best_col] = 2
        while True:
            other_best_row = random.randrange(number_of_squares)
            other_best_col = random.randrange(number_of_squares)
            if other_best_row != best_row or other_best_col != best_col:
                break
        scores[other_best_row][other_best_col] = 2
        while True:
            second_best_row = random.randrange(number_of_squares)
            second_best_col = random.randrange(number_of_squares)
            if (
                    second_best_row != best_row or
                    second_best_col != best_col
            ) and (
                second_best_row != other_best_row or
                second_best_col != other_best_col
            ):
                break
        scores[second_best_row][second_best_col] = 1
        best_move = ttt.get_best_move(board, scores)
        tests.run_test(
            best_move == (best_row, best_col) or
            best_move == (other_best_row, other_best_col),
            True,
            'test_get_best_move_if_two_equal_maxes_and_both_are_empty# ' +
            str(test_counter) + ': '
        )
        test_counter += 1

    tests.report_results()
    print
    return tests.total_tests, tests.failures


def test_get_best_move_if_two_equal_maxes_and_one_is_empty():
    """
    Test if the best move was chosen if two equal maxes and one is empty.
    """
    print 'Testing get_best_move_if_two_equal_maxes_and_one_is_empty\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    number_of_squares_cases = [2, 7, 8]

    for number_of_squares in number_of_squares_cases:
        board = provided.TTTBoard(number_of_squares)
        scores = [[0]*number_of_squares for dummy in range(number_of_squares)]
        best_row = random.randrange(number_of_squares)
        best_col = random.randrange(number_of_squares)
        scores[best_row][best_col] = 2
        player = random.choice([provided.PLAYERX, provided.PLAYERO])
        board.move(best_row, best_col, player)
        while True:
            other_best_row = random.randrange(number_of_squares)
            other_best_col = random.randrange(number_of_squares)
            if other_best_row != best_row or other_best_col != best_col:
                break
        scores[other_best_row][other_best_col] = 2
        while True:
            second_best_row = random.randrange(number_of_squares)
            second_best_col = random.randrange(number_of_squares)
            if (
                    second_best_row != best_row or
                    second_best_col != best_col
            ) and (
                second_best_row != other_best_row or
                second_best_col != other_best_col
            ):
                break
        scores[second_best_row][second_best_col] = 1
        best_move = ttt.get_best_move(board, scores)
        tests.run_test(
            best_move,
            (other_best_row, other_best_col),
            'test_get_best_move_if_two_equal_maxes_and_one_is_empty # ' +
            str(test_counter) + ': '
        )
        test_counter += 1

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_get_best_move_if_two_equal_maxes_and_none_is_empty():
    """
    Test if second best move was chosen if two equal maxes and none is empty.
    """
    print 'Testing get_best_move_if_two_equal_maxes_and_none_is_empty\n'+60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    number_of_squares_cases = [2, 7, 8]

    for number_of_squares in number_of_squares_cases:
        board = provided.TTTBoard(number_of_squares)
        scores = [[0]*number_of_squares for dummy in range(number_of_squares)]
        best_row = random.randrange(number_of_squares)
        best_col = random.randrange(number_of_squares)
        scores[best_row][best_col] = 2
        player = random.choice([provided.PLAYERX, provided.PLAYERO])
        board.move(best_row, best_col, player)
        while True:
            other_best_row = random.randrange(number_of_squares)
            other_best_col = random.randrange(number_of_squares)
            if other_best_row != best_row or other_best_col != best_col:
                break
        scores[other_best_row][other_best_col] = 2
        player = random.choice([provided.PLAYERX, provided.PLAYERO])
        board.move(other_best_row, other_best_col, player)
        while True:
            second_best_row = random.randrange(number_of_squares)
            second_best_col = random.randrange(number_of_squares)
            if (second_best_row != best_row or second_best_col != best_col) and\
            (second_best_row != other_best_row or\
             second_best_col != other_best_col):
                break
        scores[other_best_row][other_best_col] = 1
        best_move = ttt.get_best_move(board, scores)
        tests.run_test(
            best_move,
            (second_best_row, second_best_col),
            'test_get_best_move_if_two_equal_maxes_and_none_is_empty # ' +
            str(test_counter) + ': '
        )
        test_counter += 1

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_mc_move(board, player, trials):
    """
    This function takes a current board, which player the machin player is,
    and the number of trials to run.
    The function should use the Monte Carlo simulation described above
    to return a move for the machine player in the form of a (row, col) tuple.
    Be sure to use the other functions you have written!

    Test if game was finished in 'mc_trial'  method.
    'provided.check_win' method returns one of the values:
        2 if PLAYERX won
        3 if PLAYERO won
        4 if DRAW
        None if game is in progress
    """
    print 'Testing mc_trial_if_game_finished\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    valid_check_win_returns = (2, 3, 4)
    number_of_squares_cases = [0, 1, 3, 8, 10, 13]

    for number_of_squares in number_of_squares_cases:
        for player in [provided.PLAYERX, provided.PLAYERO]:
            board = provided.TTTBoard(number_of_squares)
            ttt.mc_trial(board, player)
            tests.run_test(
                board.check_win() in valid_check_win_returns,
                True,
                'test_mc_trial # ' + str(test_counter) + ': '
            )
            test_counter += 1

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_all():
    """
    Run all tests.
    """
    #total_stat = [total_tests, total_failures]
    total_stat = [0, 0]
    total_stat = map(
        lambda x, y: x+y,
        total_stat,
        list(test_mc_trial_if_both_players_played())
    )
    total_stat = map(
        lambda x, y: x+y,
        total_stat,
        list(test_mc_trial_if_game_finished())
    )
    total_stat = map(
        lambda x, y: x+y,
        total_stat,
        list(test_get_winner_code())
    )
    total_stat = map(
        lambda x, y: x+y,
        total_stat,
        list(test_get_looser_code())
    )
    total_stat = map(
        lambda x, y: x+y,
        total_stat,
        list(test_convert_player_code_to_player())
    )
    total_stat = map(
        lambda x, y: x+y,
        total_stat,
        list(test_convert_player_to_player_code())
    )
    total_stat = map(
        lambda x, y: x+y,
        total_stat,
        list(test_mc_update_scores())
    )
    total_stat = map(
        lambda x, y: x+y,
        total_stat,
        list(test_get_best_move_if_max_is_not_empty())
    )
    total_stat = map(
        lambda x, y: x+y,
        total_stat,
        list(test_get_best_move_if_max_is_empty())
    )
    total_stat = map(
        lambda x, y: x+y,
        total_stat,
        list(test_get_best_move_if_two_equal_maxes_and_both_are_empty())
    )
    total_stat = map(
        lambda x, y: x+y,
        total_stat,
        list(test_get_best_move_if_two_equal_maxes_and_one_is_empty())
    )
    total_stat = map(
        lambda x, y: x+y,
        total_stat,
        list(test_get_best_move_if_two_equal_maxes_and_none_is_empty())
    )
    print 'Testing summary\n' + 60*'#'
    print 'Ran ' + str(total_stat[0]) + ' tests. ' +\
        str(total_stat[1]) + ' failures.'
    print

test_all()
