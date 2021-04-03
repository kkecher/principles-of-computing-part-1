#!/usr/bin/env python2

import poc_simpletest
import user48_sr0ObzlL1X_51 as project_2048

def test_init():
    """
    Test self.__init__ method and returns total and failures tests for  stat in test_all() method.
    """
    print 'Testing self.__init__\n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    test_counter = 0
    tests, test_counter = test_init_run_tests(tests, test_counter, height=4, width=6)
    tests, test_counter = test_init_run_tests(tests, test_counter, height=10, width=10)
    tests, test_counter = test_init_run_tests(tests, test_counter, height=1, width=1)
    tests, test_counter = test_init_run_tests(tests, test_counter, height=2, width=1)
    tests, test_counter = test_init_run_tests(tests, test_counter, height=1, width=2)

    #tests.run_test(project_2048.TwentyFortyEight(-1, -4), 'AssertionError: Expected grid_height > 0 and grid_width > 0.\nGot grid_height == -1, grid_width == -4', 'test_init #15: ')
    #tests.run_test(project_2048.TwentyFortyEight(0, 0), 'AssertionError: Expected grid_height > 0 and grid_width > 0.\nGot grid_height == 0, grid_width == 0', 'test_init #16: ')
    #tests.run_test(project_2048.TwentyFortyEight(5, 0), 'AssertionError: Expected grid_height > 0 and grid_width > 0.\nGot grid_height == 5, grid_width == 0', 'test_init #17: ')
    #tests.run_test(project_2048.TwentyFortyEight(0, 1), 'AssertionError: Expected grid_height > 0 and grid_width > 0.\nGot grid_height == 0, grid_width == 1', 'test_init #18: ')
    #tests.run_test(project_2048.TwentyFortyEight(4, -10), 'AssertionError: Expected grid_height > 0 and grid_width > 0.\nGot grid_height == 4, grid_width == -10', 'test_init #19: ')

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_init_run_tests(tests, test_counter, height, width):
    game = project_2048.TwentyFortyEight(height, width)
    tests.run_test(str(game), '[]', 'test_init #' + str(test_counter) + ': ')
    test_counter += 1
    tests.run_test(game.get_grid_height(), height, 'test_init #' + str(test_counter) + ': ')
    test_counter += 1
    tests.run_test(game.get_grid_width(), width, 'test_init #' + str(test_counter) + ': ')
    return tests, test_counter

def test_reset():
    """
    Test self.reset method and returns total and failures tests for  stat in test_all() method.
    """
    print 'Testing self.reset \n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    game = project_2048.TwentyFortyEight(4, 6)
    game.reset()
    tests.run_test(str(game), '[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]', 'test_reset #0: ')

    game = project_2048.TwentyFortyEight(10, 10)
    game.reset()
    tests.run_test(str(game), '[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]', 'test_reset #1: ')

    game = project_2048.TwentyFortyEight(1, 1)
    game.reset()
    tests.run_test(str(game), '[[0]]', 'test_reset #2')

    game = project_2048.TwentyFortyEight(2, 1)
    game.reset()
    tests.run_test(str(game), '[[0], [0]]', 'test_reset #3: ')

    game = project_2048.TwentyFortyEight(1, 2)
    game.reset()
    tests.run_test(str(game), '[[0, 0]]', 'test_reset #4: ')

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_str():
    """
    Test self.__str__ method and returns total and failures tests for  stat in test_all() method.
    """
    print 'Testing self.__str__ \n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    game = project_2048.TwentyFortyEight(4, 6)
    game.reset()
    tests.run_test(game.__str__(), '[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]', 'test_str #0: ')

    game = project_2048.TwentyFortyEight(10, 10)
    game.reset()
    tests.run_test(game.__str__(), '[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]', 'test_str #1: ')

    game = project_2048.TwentyFortyEight(1, 1)
    game.reset()
    tests.run_test(game.__str__(), '[[0]]', 'test_str #2: ')

    game = project_2048.TwentyFortyEight(2, 1)
    game.reset()
    tests.run_test(game.__str__(), '[[0], [0]]', 'test_str #3: ')

    game = project_2048.TwentyFortyEight(1, 2)
    game.reset()
    tests.run_test(game.__str__(), '[[0, 0]]', 'test_str #4: ')

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_get_grid_height():
    """
    Test self.get_grid_height method and returns total and failures tests for  stat in test_all() method.
    """
    print 'Testing self.get_grid_height \n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    game = project_2048.TwentyFortyEight(4, 6)
    game.reset()
    tests.run_test(game.get_grid_height(), 4, 'test_get_grid_height #0: ')

    game = project_2048.TwentyFortyEight(10, 10)
    game.reset()
    tests.run_test(game.get_grid_height(), 10, 'test_get_grid_height #1: ')

    game = project_2048.TwentyFortyEight(1, 1)
    game.reset()
    tests.run_test(game.get_grid_height(), 1,  'test_get_grid_height #2: ')

    game = project_2048.TwentyFortyEight(2, 1)
    game.reset()
    tests.run_test(game.get_grid_height(), 2, 'test_get_grid_height #3: ')

    game = project_2048.TwentyFortyEight(1, 2)
    game.reset()
    tests.run_test(game.get_grid_height(), 1, 'test_get_grid_height #4: ')

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_get_grid_width():
    """
    Test self.get_grid_width method and returns total and failures tests for  stat in test_all() method.
    """
    print 'Testing self.get_grid_width \n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    game = project_2048.TwentyFortyEight(4, 6)
    game.reset()
    tests.run_test(game.get_grid_width(), 6, 'test_get_grid_width #0: ')

    game = project_2048.TwentyFortyEight(10, 10)
    game.reset()
    tests.run_test(game.get_grid_width(), 10, 'test_get_grid_width #1: ')

    game = project_2048.TwentyFortyEight(1, 1)
    game.reset()
    tests.run_test(game.get_grid_width(), 1, 'test_get_grid_width #2: ')

    game = project_2048.TwentyFortyEight(2, 1)
    game.reset()
    tests.run_test(game.get_grid_width(), 1, 'test_get_grid_width #3: ')

    game = project_2048.TwentyFortyEight(1, 2)
    game.reset()
    tests.run_test(game.get_grid_width(), 2, 'test_get_grid_width #4: ')

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_new_tile():
    """
    Test self.new_tile method and returns total and failures tests for  stat in test_all() method.
    """
    print 'Testing self.new_tile \n' + 60*'#'
    test_counter = 0
    test_counter_max = 10
    tests = poc_simpletest.TestSuite()

    test_counter, tests = test_new_tile_compare_grids(tests, test_counter,  test_counter_max, height=4, width=6)
    test_counter, tests = test_new_tile_compare_grids(tests, test_counter,  test_counter_max, height=10, width=10)
    test_counter, tests = test_new_tile_compare_grids(tests, test_counter,  test_counter_max, height=1, width=1)
    test_counter, tests = test_new_tile_compare_grids(tests, test_counter,  test_counter_max, height=2, width=1)
    test_counter, tests = test_new_tile_compare_grids(tests, test_counter,  test_counter_max, height=1, width=2)

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_new_tile_compare_grids(tests, test_counter, test_counter_max, height, width):
    game = project_2048.TwentyFortyEight(height, width)
    game.reset()

    #Codeskulptor has time limits so we restrict number of tests.
    #If you have recieved TimeLimitError, hit "Run" once more or reduce test_counter_max
    for dummy_i in range(min(height*width, test_counter_max)):
        initial_grid = [list(row) for row in game.get_grid()]
        game.new_tile()
        new_grid = game.get_grid()
        diff_rows = [[initial_row, new_row] for initial_row, new_row in zip(initial_grid, new_grid) if initial_row != new_row][0]
        diff_cols = [new_col for initial_col, new_col in zip(diff_rows[0], diff_rows[1]) if initial_col != new_col]
        tests.run_test(len(diff_rows)+len(diff_cols), 3, 'test_new_tile # ' + str(test_counter) + ': \nInitial grid: ' + str(initial_grid) + '\nNew_grid:      ' + str(new_grid) + '\n')
        test_counter += 1
    initial_grid = [list(row) for row in str(game)]
    is_game_over = game.new_tile()
    new_grid = game.get_grid()
    if height*width > test_counter_max:
        diff_rows = [[initial_row, new_row] for initial_row, new_row in zip(initial_grid, new_grid) if initial_row != new_row][0]
        diff_cols = [new_col for initial_col, new_col in zip(diff_rows[0], diff_rows[1]) if initial_col != new_col]
        tests.run_test(len(diff_rows)+len(diff_cols), 3, 'test_new_tile # ' + str(test_counter) + ': \nInitial grid: ' + str(initial_grid) + '\nNew_grid:      ' + str(new_grid) + '\n')
        test_counter += 1
        tests.run_test(is_game_over, None, 'test_new_tile # ' + str(test_counter) + ': \nInitial grid: ' + str(initial_grid) + '\nNew_grid:      ' + str(new_grid) + '\n')
    else:
        tests.run_test(is_game_over, 'Game is over', 'test_new_tile # ' + str(test_counter) + ': \nInitial grid: ' + str(initial_grid) + '\nNew_grid: ' + str(new_grid) + '\n')
    test_counter += 1
    return test_counter, tests

def test_set_tile():
    """
    Test self.set_tile method and returns total and failures tests for  stat in test_all() method.
    """
    print 'Testing self.set_tile \n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    game = project_2048.TwentyFortyEight(4, 6)
    game.reset()
    game.set_tile(3, 5, 9)
    tests.run_test(str(game), '[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 9]]', 'test_set_tile #0: ')
    game.set_tile(0, 0, 9)
    tests.run_test(str(game), '[[9, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 9]]', 'test_set_tile #1: ')
    game.set_tile(1, -6, 9)
    tests.run_test(str(game), '[[9, 0, 0, 0, 0, 0], [9, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 9]]', 'test_set_tile #2: ')
    game.set_tile(-4, -4, 9)
    tests.run_test(str(game), '[[9, 0, 9, 0, 0, 0], [9, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 9]]', 'test_set_tile #3: ')
    game.set_tile(-4, -4, -8)
    tests.run_test(str(game), '[[9, 0, -8, 0, 0, 0], [9, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 9]]', 'test_set_tile #4: ')
    #tests.run_test(game.set_tile(4, 2, 9), 'Expected row in range(-self.height, self.height) and col in range(-self.width, self.width).\n Got:\nrow = 4, self.height = 3\ncol = 2, self.width = 6', 'test_set_tile #0: ')

    game = project_2048.TwentyFortyEight(1, 1)
    game.reset()
    game.set_tile(0, 0, 'Hey you, you are awesome!')
    tests.run_test(str(game), "[['Hey you, you are awesome!']]", 'test_set_tile #5')
    game.set_tile(0, 0, 'And I am awesome too!')
    tests.run_test(str(game), "[['And I am awesome too!']]", 'test_set_tile #6')


    tests.report_results()
    print
    return tests.total_tests, tests.failures


def test_get_tile():
    """
    Test self.get_tile method and returns total and failures tests for  stat in test_all() method.
    """
    print 'Testing self.get_tile \n' + 60*'#'

    tests = poc_simpletest.TestSuite()
    game = project_2048.TwentyFortyEight(4, 6)
    game.reset()
    game.set_tile(0, 0, 'I')
    tests.run_test(game.get_tile(0, 0), 'I', 'test_get_tile #0: ')

    game = project_2048.TwentyFortyEight(10, 10)
    game.reset()
    game.set_tile(5, 3, 'want')
    tests.run_test(game.get_tile(5, 3), 'want', 'test_get_tile #1: ')

    game = project_2048.TwentyFortyEight(1, 1)
    game.reset()
    game.set_tile(-1, 0, 'to')
    tests.run_test(game.get_tile(-1, 0), 'to',  'test_get_tile #2: ')

    game = project_2048.TwentyFortyEight(2, 1)
    game.reset()
    game.set_tile(1, 0, 'break')
    tests.run_test(game.get_tile(1, 0), 'break', 'test_get_tile #3: ')

    game = project_2048.TwentyFortyEight(1, 2)
    game.reset()
    game.set_tile(-1, 1, 'free')
    tests.run_test(game.get_tile(-1, 1), 'free', 'test_get_tile #4: ')

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def test_move():
    """
    Test self.move method and returns total and failures tests for  stat in test_all() method.
    """
    print 'Testing self.move \n' + 60*'#'

    tests = poc_simpletest.TestSuite()

    game = project_2048.TwentyFortyEight(4, 6)
    game.reset()

    create_test_grid(game, [[0, 3, 0, 0, 2, 0], [3, 0, 3, 0, 0, 0], [0, 4, 3, 2, 0, 0], [2, 1, 2, 3, 2, 0]])
    direction = 1
    game.move(direction)
    tests.run_test(str(game), '[[3, 3, 6, 2, 4, 0], [2, 4, 2, 3, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]', 'test_move #0: ')

    create_test_grid(game, [[0, 3, 0, 0, 2, 0], [3, 0, 3, 0, 0, 0], [0, 4, 3, 2, 0, 0], [2, 1, 2, 3, 2, 0]])
    direction = 2
    game.move(direction)
    tests.run_test(str(game), '[[0, 0, 0, 0, 0, 0], [0, 3, 0, 0, 0, 0], [3, 4, 6, 2, 0, 0], [2, 1, 2, 3, 4, 0]]', 'test_move #1: ')

    create_test_grid(game, [[0, 3, 0, 0, 2, 0], [3, 0, 3, 0, 0, 0], [0, 4, 3, 2, 0, 0], [2, 1, 2, 3, 2, 0]])
    direction = 3
    game.move(direction)
    tests.run_test(str(game), '[[3, 2, 0, 0, 0, 0], [6, 0, 0, 0, 0, 0], [4, 3, 2, 0, 0, 0], [2, 1, 2, 3, 2, 0]]', 'test_move #2: ')

    create_test_grid(game, [[0, 3, 0, 0, 2, 0], [3, 0, 3, 0, 0, 0], [0, 4, 3, 2, 0, 0], [2, 1, 2, 3, 2, 0]])
    direction = 4
    game.move(direction)
    tests.run_test(str(game), '[[0, 0, 0, 0, 3, 2], [0, 0, 0, 0, 0, 6], [0, 0, 0, 4, 3, 2], [0, 2, 1, 2, 3, 2]]', 'test_move #3: ')

    game = project_2048.TwentyFortyEight(1, 1)
    game.reset()
    create_test_grid(game, [[4]])
    direction = 1
    game.move(direction)
    tests.run_test(str(game), '[[4]]', 'test_move #4: ')

    create_test_grid(game, [[4]])
    direction = 2
    game.move(direction)
    tests.run_test(str(game), '[[4]]', 'test_move #5: ')

    create_test_grid(game, [[4]])
    direction = 3
    game.move(direction)
    tests.run_test(str(game), '[[4]]', 'test_move #6: ')

    create_test_grid(game, [[4]])
    direction = 4
    game.move(direction)
    tests.run_test(str(game), '[[4]]', 'test_move #7: ')

    game = project_2048.TwentyFortyEight(2, 1)
    game.reset()
    create_test_grid(game, [[2], [4]])
    direction = 1
    game.move(direction)
    tests.run_test(str(game), '[[2], [4]]', 'test_move #8: ')

    create_test_grid(game, [[2], [4]])
    direction = 2
    game.move(direction)
    tests.run_test(str(game), '[[2], [4]]', 'test_move #9: ')

    create_test_grid(game, [[2], [4]])
    direction = 3
    game.move(direction)
    tests.run_test(str(game), '[[2], [4]]', 'test_move #10: ')

    create_test_grid(game, [[2], [4]])
    direction = 4
    game.move(direction)
    tests.run_test(str(game), '[[2], [4]]', 'test_move #11: ')

    game = project_2048.TwentyFortyEight(1, 2)
    game.reset()
    create_test_grid(game, [[2, 2]])
    direction = 1
    game.move(direction)
    tests.run_test(str(game), '[[2, 2]]', 'test_move #12: ')

    create_test_grid(game, [[2, 2]])
    direction = 2
    game.move(direction)
    tests.run_test(str(game), '[[2, 2]]', 'test_move #13: ')

    create_test_grid(game, [[2, 2]])
    direction = 3
    game.move(direction)
    tests.run_test(str(game), '[[4, 0]]', 'test_move #14: ')

    create_test_grid(game, [[2, 2]])
    direction = 4
    game.move(direction)
    tests.run_test(str(game), '[[0, 4]]', 'test_move #15: ')

    tests.report_results()
    print
    return tests.total_tests, tests.failures

def create_test_grid(game, test_values):
    for row_index in range(len(test_values)):
        for col_index in range(len(test_values[row_index])):
            game.set_tile(row_index, col_index, test_values[row_index][col_index])

def test_all():
    """
    Run all tests.
    """
    #total_stat = [total_tests, total_failures]
    total_stat = [0, 0]
    total_stat = map(lambda x, y: x+y, total_stat, list(test_init()))
    total_stat = map(lambda x, y: x+y, total_stat, list(test_reset()))
    total_stat = map(lambda x, y: x+y, total_stat, list(test_str()))
    total_stat = map(lambda x, y: x+y, total_stat, list(test_get_grid_height()))
    total_stat = map(lambda x, y: x+y, total_stat, list(test_get_grid_width()))
    total_stat = map(lambda x, y: x+y, total_stat, list(test_new_tile()))
    total_stat = map(lambda x, y: x+y, total_stat, list(test_set_tile()))
    total_stat = map(lambda x, y: x+y, total_stat, list(test_get_tile()))
    total_stat = map(lambda x, y: x+y, total_stat, list(test_move()))

    print 'Testing summary\n' + 60*'#'
    print 'Ran ' + str(total_stat[0]) + ' tests. ' + str(total_stat[1]) + ' failures.'
    print

test_all()
