# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an array of digit strings nums and a digit string target, return the
    number of pairs of indices (i,j) (where i != j) such that the concatenation
    of nums[i] + nums[j] equals to target.
    '''
    def numOfPairs(self, nums: List[str], target: str) -> int:
        c = Counter(nums)
        answer = 0
        for i in c:
            if not target.startswith(i):
                continue
            end = target[len(i):]
            if end not in c:
                continue
            if i == end:
                answer += c[i] * (c[end] - 1)
            else:
                answer += c[i] * c[end]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["777","7","77","77"]
        j = "7777"
        o = 4
        self.assertEqual(s.numOfPairs(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["123","4","12","34"]
        j = "1234"
        o = 2
        self.assertEqual(s.numOfPairs(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["1","1","1"]
        j = "11"
        o = 6
        self.assertEqual(s.numOfPairs(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)