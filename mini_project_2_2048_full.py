#!/usr/bin/env python2

"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    if line == []:
        return []
    res_line = [line[0]]
    is_summed = False
    for line_index in range(1, len(line)):
        if line[line_index] != 0:
            if line[line_index] == res_line[-1] and not is_summed:
                res_line[-1] += line[line_index]
                is_summed = True
            else:
                res_line.append(line[line_index])
                is_summed = False
    if res_line[0] == 0:
        res_line.pop(0)
    while len(res_line) != len(line):
        res_line.append(0)
    return res_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        assert grid_height > 0 and grid_width > 0, 'Expected grid_height > 0 and grid_width > 0.\nGot grid_height == %d, grid_width == %d' % (grid_height, grid_width)
        self._height = grid_height
        self._width = grid_width
        self._grid = []
        self.reset() #comment out when run test_mini_project_2_2048_full.py

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [self._width*[0] for dummy_col in range(self._height)]
        self.new_tile() #comment out when run test_mini_project_2_2048_full.py
        self.new_tile() #comment out when run test_mini_project_2_2048_full.py

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
      """
        #We get direction as integer which matches following (row, col) moves:
        directions = {1: (1, 0),
                      2: (-1, 0),
                      3: (0, 1),
                      4: (0, -1)}
        direction = directions[direction]

        assert not(direction[0] == 0 and direction[1] == 0), 'Expected one non-zero element in direction'
        assert not(direction[0] != 0 and direction[1] != 0), 'Expected one zero element in direction'

        #Get copy of self._grid to find out later if any move has been done. We need deepcopy to do it proper way, but Codesculptor doesn't support it.
        copied_grid = [list(row) for row in self._grid]

        #Transpose copied_grid if direction iterates over columns: (1, 0) or (-1, 0) . That keeps iteration  over rows in any case and keeps simple to create merged grid.
        if direction[0] != 0:
            copied_grid = list(map(list, zip(*copied_grid)))
            step = direction[0]
        else:
            step = direction[1]
        merged_grid = []
        for row in copied_grid:
            #Merge function works only in right-to-left way so we reverse every row if the direction is reversed
            if step == -1:
                row.reverse()
            row = merge(row)
            #Reverse merged row if we merge to right.
            if direction[1] == -1:
                row.reverse()
            merged_grid.append(row)

        #Change back reversed grid
        if direction[0] != 0:
            merged_grid = list(map(list, zip(*merged_grid)))
        if direction[0] == -1:
            merged_grid.reverse()
        if self._grid != merged_grid:
            self._grid = merged_grid
            self.new_tile() #comment out when run test_mini_project_2_2048_full.py

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        random_row = random.randrange(self._height)
        initial_random_row = random_row
        while 0 not in self._grid[random_row]:
            random_row += 1
            random_row = random_row % self._height
            if random_row == initial_random_row:
                return 'Game is over'
        random_col =  random.randrange(self._width)
        while self._grid[random_row][random_col] != 0:
            random_col += 1
            random_col = random_col % self._height

        tile = random.random()
        if tile < 0.9:
            tile = 2
        else:
            tile = 4

        self._grid[random_row][random_col] = tile

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        assert row in range(-self._height, self._height) and col in range(-self._width, self._width), 'Expected row in range(-self._height, self._height) and col in range(-self._width, self._width).\n Got:\nrow = %d, self._height = %d\ncol = %d, self._width = %d' % (row, self._height, col, self._width)
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        assert row in range(-self._height, self._height) and col in range(-self._width, self._width), 'Expected row in range(-self._height, self._height) and col in range(-self._width, self._width).\n Got:\nrow = %d, self._height = %d\ncol = %d, self._width = %d' % (row, self._height, col, self._width)
        return self._grid[row][col]

    def get_grid(self):
        """
        Get the board as list.
        """
        return self._grid

#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
