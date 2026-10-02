# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    Start with an empty array ans. Repeat the following operation until nums is
    empty:
    * Identify all distinct values currently present in nums.
    * Remove one occurrence of every distinct value currently in nums, and
      append those values to ans in ascending order.

    Return the array ans.
    '''
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        answer = []
        c = Counter(nums)
        while c:
            pull = []
            for i in c:
                pull.append(i)
                c[i] -= 1
            for i in pull:
                if c[i] == 0:
                    del c[i]
            answer.extend(sorted(pull))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1,3,2,1,3]
        o = [1,2,3,1,3,3]
        self.assertEqual(s.rearrangeArray(i), o)

    def test_two(self):
        s = Solution()
        i = [7,7,4,4,4]
        o = [4,7,4,7,4]
        self.assertEqual(s.rearrangeArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)