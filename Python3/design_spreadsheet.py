# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional, Tuple

'''
A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given
number of rows. Each cell in the spreadsheet can hold an integer value between 0
and 10**5.

Implement the Spreadsheet class:
'''
class Spreadsheet:
    '''
    Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z') and the
    specified number of rows. All cells are initially set to 0.
    '''
    def __init__(self, rows: int):
        self.rows = dict()

    def _help(cell:str) -> Tuple[int,int]:
        a = ord(cell[0]) - 65
        b = int(cell[1:])
        return (a,b)

    def getCell(self, cell: str) -> int:
        a,b = Spreadsheet._help(cell)
        if b in self.rows:
            return self.rows[b][a]
        return 0

    '''
    Sets the value of the specified cell. The cell reference is provided in the
    format "AX" (e.g. "A1", "B10") where the letter represents the column (from
    'A' to 'Z') and the number represents a 1-indexed row.
    '''
    def setCell(self, cell: str, value: int) -> None:
        a,b = Spreadsheet._help(cell)
        if b not in self.rows:
            self.rows[b] = [0] * 26
        self.rows[b][a] = value

    '''
    Resets the specified cell to 0.
    '''
    def resetCell(self, cell: str) -> None:
        a,b = Spreadsheet._help(cell)
        if b in self.rows:
            self.rows[b][a] = 0

    '''
    Evaluates a formula of the form "=X+Y", where X and Y are either cell
    references or non-negative integers, and returns the computed sum.

    Note if getValue references a cell that has not been explicitly set using
    setCell, its value is considered 0.
    '''
    def getValue(self, formula: str) -> int:
        x,y = formula[1:].split('+')
        if x[0] < 'A':
            x = int(x)
        else:
            x = self.getCell(x)
        if y[0] < 'A':
            y = int(y)
        else:
            y = self.getCell(y)
        return x + y

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Spreadsheet(3)
        self.assertEqual(s.getValue("=5+7"), 12)
        s.setCell("A1", 10)
        self.assertEqual(s.getValue("=A1+6"), 16)
        s.setCell("B2", 15)
        self.assertEqual(s.getValue("=A1+B2"), 25)
        s.resetCell("A1")
        self.assertEqual(s.getValue("=A1+B2"), 15)

if __name__ == '__main__':
    unittest.main(verbosity=2)