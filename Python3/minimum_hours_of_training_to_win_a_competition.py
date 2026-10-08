# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A person entering a competition has the following two positive integers,
    initialEnergy and initialExperience denoting their initial energy and
    initial experience respectively.

    Also given two 0-indexed integer arrays energy and experience, both of
    length n.

    The person is facing n opponents in order. The energy and experience of the
    ith opponent is denoted by energy[i] and experience[i] respectively. When
    the person faces an opponent, they to have both strictly greater experience
    and energy to defeat them and move on to the next opponent.

    Defeating the ith opponent increases the person's experience by
    experience[i], but decreases their energy by energy[i].

    Before starting the competition the person can train for some number of
    hours. After each hour of training, the person either chooses to increase
    their experience by one, or increase their energy by one.

    Return the minimum number of training hours required for the person to
    defeat all n opponents.
    '''
    def minNumberOfHours(self, iEng: int, iExp: int, energy: list[int], experience: list[int]) -> int:
        training = 0
        for eng, exp in zip(energy, experience):
            if iExp <= exp:
                training += exp - iExp + 1
                iExp = exp + 1
            iExp += exp
            if iEng <= eng:
                training += eng - iEng + 1
                iEng = eng + 1
            iEng -= eng
        return training

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = 3
        k = [1,4,3,2]
        l = [2,6,3,1]
        o = 8
        self.assertEqual(s.minNumberOfHours(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = 4
        k = [1]
        l = [3]
        o = 0
        self.assertEqual(s.minNumberOfHours(i,j,k,l), o)

    def test_three(self):
        s = Solution()
        i = 5
        j = 3
        k = [1,4]
        l = [2,5]
        o = 2
        self.assertEqual(s.minNumberOfHours(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)