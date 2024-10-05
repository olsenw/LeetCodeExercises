# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, return the most frequent even element.

    If there is a tie, return the smallest one. If there is no such element
    return -1.
    '''
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter(n for n in nums if n % 2 == 0)
        if len(c) == 0:
            return -1
        answer = 10**9+7
        count = 0
        for i in c:
            if c[i] == count:
                answer = min(answer, i)
            elif c[i] > count:
                answer = i
                count = c[i]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,2,2,4,4,1]
        o = 2
        self.assertEqual(s.mostFrequentEven(i), o)

    def test_two(self):
        s = Solution()
        i = [4,4,4,9,2,4]
        o = 4
        self.assertEqual(s.mostFrequentEven(i), o)

    def test_three(self):
        s = Solution()
        i = [29,47,21,41,13,37,25,7]
        o = -1
        self.assertEqual(s.mostFrequentEven(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)