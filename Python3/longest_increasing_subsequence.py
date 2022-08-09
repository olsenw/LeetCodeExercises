# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from sortedcontainers import SortedDict

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        #brute
        answer = 0
        for a in range(len(nums)):
            x = nums[a]
            c = 1
            for b in range(a + 1, len(nums)):
                y = nums[b]
                if x < y:
                    x = y
                    c += 1
            answer = max(answer, c)
        return answer
        '''
        # maybe smarter
        so = SortedDict()
        for a in reversed(range(len(nums))):
            b = so.bisect(nums[a])
            if b < len(so):
                so[nums[a]] = max(so.values()[b:]) + 1
            else:
                so[nums[a]] = 1
        return max(so.values())

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,9,2,5,3,7,101,18]
        o = 4
        self.assertEqual(s.lengthOfLIS(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1,0,3,2,3]
        o = 4
        self.assertEqual(s.lengthOfLIS(i), o)

    def test_three(self):
        s = Solution()
        i = [7,7,7,7,7,7,7]
        o = 1
        self.assertEqual(s.lengthOfLIS(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)