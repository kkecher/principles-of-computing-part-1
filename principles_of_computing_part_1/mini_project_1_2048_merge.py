#!/usr/bin/env python

"""
Merge function for 2048 game.
"""

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
