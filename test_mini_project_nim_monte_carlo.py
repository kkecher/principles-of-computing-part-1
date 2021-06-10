#!/usr/bin/env python2

"""
Tests for mini-project - Nim (Monte Carlo).
"""

import poc_simpletest
import user48_gqB5mwh50v_7 as ttt

def test_play_random_game():
    """
    Test:
    - choose an initial move items in interval [0, 3]
    - make initial move
    - make random moves while `num_items` > 0
    - check if `num_items_after_finished` <= 0 (check if game was over)
    - check if computer's move was last
    (if yes - computer won, if no - computer lost)
    """
    print 'Testing play_random_game\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0

    for initial_move in range(1, ttt.MAX_REMOVE+1):
        is_computer_won, num_items_after_finished =\
            ttt.play_random_game(initial_move, ttt.NUM_ITEMS)

        test_counter += 1
        tests.run_test(
            is_computer_won in (True, False),
            True,
            'test_play_random_game (is_computer_won) #'
            + str(test_counter) + ': '
            )

        test_counter += 1
        tests.run_test(
            num_items_after_finished <= 0,
            True,
            'test_play_random_game (num_items_after_finished <= 0) #'
            + str(test_counter) + ': '
            )
    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_evaluate_position():
    """
    Test:
    - get initial num_items
    - repeat `play_random_game` ttt.TRIALS
    - count computer's win fraction for each move in interval [0, 3]
    """
    print 'Testing evaluate_position\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0

    computer_win_fractions = ttt.evaluate_position(ttt.NUM_ITEMS)

    test_counter += 1
    tests.run_test(
        type(computer_win_fractions),
        dict,
        'test_evaluate_position (type of `computer_win_fractions` is dict) #'
        + str(test_counter) + ': '
    )

    test_counter += 1
    tests.run_test(
        len(computer_win_fractions),
        ttt.MAX_REMOVE,
        'test_evaluate_position (len of `computer_win_fractions` == ' +\
        str(ttt.MAX_REMOVE) + ' #'
        + str(test_counter) + ': '
    )
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
        list(test_play_random_game())
    )
    total_stat = map(
        lambda x, y: x+y,
        total_stat,
        list(test_evaluate_position())
    )
    print 'Testing summary\n' + 60*'#'
    print 'Ran ' + str(total_stat[0]) + ' tests. ' +\
        str(total_stat[1]) + ' failures.'
    print

test_all()
