# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import permutations
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a survey that consists of n questions where each question's answer
    is either 0 (no) or 1 (yes).

    The survey was given to m students numbered from 0 to m - 1 and m mentors
    numbered from 0 to m - 1. The answer of the students are represented by a 2D
    integer array students where students[i] is an integer array that contains
    the answer of the ith student (0-indexed). The answers of the mentors are
    represented by a 2D integer array mentors where mentors[i] is an integer
    array that contains the answers of the jth mentor (0-indexed).

    Each student will be assigned to one mentor, and each mentor will have one
    student assigned to them. The compatibility score of a student-mentor pair
    is the number of answers that are the same for both the student and the
    mentor.

    Find the optimal student-mentor pairings to maximize the sum of the
    compatibility scores.

    Given students and mentors, return the maximum compatibility score sum that
    can be achieved.
    '''
    def maxCompatibilitySum(self, students: list[list[int]], mentors: list[list[int]]) -> int:
        m = len(mentors)
        n = len(mentors[0])
        compatibility = dict()
        # mentors
        for i in range(m):
            # students
            for j in range(m):
                # compatibility[(j,i)] = sum((mentors[i][k] == 1 and students[j][k] == 1) for k in range(n))
                compatibility[(j,i)] = sum((mentors[i][k] == students[j][k]) for k in range(n))
        answer = 0
        # all the permutations of students matched to mentors
        for p in permutations(range(m)):
            a = 0
            for i in range(m):
                c = compatibility[(i,p[i])]
                a += c
            answer = max(answer, a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1,0],[1,0,1],[0,0,1]]
        j = [[1,0,0],[0,0,1],[1,1,0]]
        o = 8
        self.assertEqual(s.maxCompatibilitySum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[0,0],[0,0],[0,0]]
        j = [[1,1],[1,1],[1,1]]
        o = 0
        self.assertEqual(s.maxCompatibilitySum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)