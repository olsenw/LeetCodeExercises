# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A chef has collected data on the satisfaction level of their n dishes. The
    chef is able to cook any dish in 1 unit of time.

    Like-time coefficient of a dish is defined as the time taken to cook that
    dish including previous dished multiplied by its satisfaction level ie
    time[i] * satisfaction[i].

    Return the maximum sum of like-time coefficient that the chef can obtain
    after dishes preparation.

    Dishes can be prepared in any order and the chef can discard some dishes to
    get this maximum value.
    '''
    def maxSatisfaction_passes(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        best = 0
        for i in range(len(satisfaction)):
            best = max(best, sum(j * k for j,k in enumerate(satisfaction[i:], 1)))
        return best

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        best = sum(i * j for i,j in enumerate(satisfaction, 1))
        for i in range(1, len(satisfaction)):
            dismiss = sum(j * k for j,k in enumerate(satisfaction[i:], 1))
            if best > dismiss:
                break
            best = dismiss
        return best if best > 0 else 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-1,-8,0,5,-9]
        o = 14
        self.assertEqual(s.maxSatisfaction(i), o)

    def test_two(self):
        s = Solution()
        i = [4,3,2]
        o = 20
        self.assertEqual(s.maxSatisfaction(i), o)

    def test_three(self):
        s = Solution()
        i = [-1,-4,-5]
        o = 0
        self.assertEqual(s.maxSatisfaction(i), o)

    def test_four(self):
        s = Solution()
        i = [-1] * 500
        o = 0
        self.assertEqual(s.maxSatisfaction(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)