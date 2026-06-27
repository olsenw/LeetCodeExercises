# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an array of positive integers nums.

    Select a subset of nums which satisfies the following condition:
    * Place the selected elements in a 0-indexed array such that it follows the
      pattern [x, x^2, x^4, ..., x^k/2, x^k, x^k/2, ..., x^4, x^2, x] (Note that
      k can be any non-negative power of 2).
    
    Return the maximum number of elements in a subset that satisfies these
    conditions.
    '''
    # based on hints
    def maximumLength(self, nums: List[int]) -> int:
        c = Counter(nums)
        answer = max(0, c[1] if c[1] % 2 == 1 else c[1] - 1)
        c[1] = 0
        for i in c:
            a = 1
            while c[i] > 1 and i * i in c:
                a += 2
                i = i * i
            answer = max(answer, a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,4,1,2,2]
        o = 3
        self.assertEqual(s.maximumLength(i), o)

    def test_two(self):
        s = Solution()
        i = [1,3,2,4]
        o = 1
        self.assertEqual(s.maximumLength(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1,1,1,1]
        o = 5
        self.assertEqual(s.maximumLength(i), o)

    def test_four(self):
        s = Solution()
        i = [1,1,1,1,1,1,1]
        o = 7
        self.assertEqual(s.maximumLength(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)