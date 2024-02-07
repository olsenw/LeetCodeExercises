# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Implement the class SubrectangleQueries which receives a rows x cols rectangle
as a matrix of integers in the constructor and supports two methods:
'''
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.r = rectangle

    '''
    Updates all values with newValue in the sub rectangle whose upper left
    coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
    '''
    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.r[i][j] = newValue

    '''
    Returns the current value of the coordinate (row,col) from the rectangle.
    '''
    def getValue(self, row: int, col: int) -> int:
        return self.r[row][col]

class UnitTesting(unittest.TestCase):
    # tested online
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)