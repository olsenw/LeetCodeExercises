# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The bitwise AND of an array nums is the bitwise AND of all integers in nums.

    Given an array of positive integers candidates. Evaluate the bitwise AND of
    every combination of numbers of candidates. Each number in candidates may
    only be used once in each combination.

    Return the size of the largest combination of candidates with a bitwise AND
    greater than 0.
    '''
    def largestCombination_fails(self, candidates: List[int]) -> int:
        h = dict()
        for c in candidates:
            if c not in h:
                h[c] = 0
            for i in list(h.keys()):
                if c & i > 0:
                    h[c & i] = 1 + max(h[c], h[i])
        return max(h[i] for i in h)

    # hint 24 bit numbers
    # can only AND if all the numbers share a bit
    def largestCombination_passes(self, candidates: List[int]) -> int:
        bits = {1 << i:0 for i in range(1,24)}
        for i in candidates:
            for j in bits:
                if i & j:
                    bits[j] += 1
        return max(bits[i] for i in bits)

    def largestCombination_fast(self, candidates: List[int]) -> int:
        answer = 0
        for i in range(24):
            count = 0
            i = 1 << i
            for j in candidates:
                if i & j:
                    count += 1
            answer = max(answer, count)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [16,17,71,62,12,24,14]
        o = 4
        self.assertEqual(s.largestCombination(i), o)

    def test_two(self):
        s = Solution()
        i = [8,8]
        o = 2
        self.assertEqual(s.largestCombination(i), o)

    def test_three(self):
        s = Solution()
        i = [33,93,31,99,74,37,3,4,2,94,77,10,75,54,24,95,65,100,41,82,35,65,38,49,85,72,67,21,20,31]
        o = 18
        self.assertEqual(s.largestCombination(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)