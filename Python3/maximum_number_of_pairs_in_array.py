# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums. In one operation, the following may be
    done:
    * Choose two integers in nums that are equal.
    * Remove both integers from nums, forming a pair.

    The operation is done on nums as many times as possible.

    Return a 0-indexed integer array answer of size 2 where answer[0] is the
    number of pairs that are formed and answer[i] is the number of leftover
    integers in nums after doing the operation as many times as possible.
    '''
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        answer = 0
        s = set()
        for n in nums:
            if n in s:
                answer += 1
                s.remove(n)
            else:
                s.add(n)
        return [answer, len(s)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2,1,3,2,2]
        o = [3,1]
        self.assertEqual(s.numberOfPairs(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1]
        o = [1,0]
        self.assertEqual(s.numberOfPairs(i), o)

    def test_three(self):
        s = Solution()
        i = [0]
        o = [0,1]
        self.assertEqual(s.numberOfPairs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)