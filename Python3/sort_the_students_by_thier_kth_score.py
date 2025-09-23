# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a class with m students and n exams. Given a 0-indexed m x n
    integer matrix score, where each row represents one student and score[i][j]
    denotes the score the ith student got in the jth exam. The matrix score
    contains distinct integers only.

    Also given the integer k. Sort the students (ie the rows of the matrix) by
    their scores in the kth (0-indexed) exam from the highest to the lowest.

    Return the matrix after sorting it.
    '''
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x:x[k], reverse=True)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
        j = 2
        o = [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
        self.assertEqual(s.sortTheStudents(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[3,4],[5,6]]
        j = 0
        o = [[5,6],[3,4]]
        self.assertEqual(s.sortTheStudents(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)