# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        answer = 0
        n = len(set(nums))
        i = 0
        c = dict()
        for j in range(len(nums)):
            if nums[j] not in c:
                c[nums[j]] = 1
            else:
                c[nums[j]] += 1
            while len(c) == n:
                answer += len(nums) - j
                if c[nums[i]] == 1:
                    del c[nums[i]]
                else:
                    c[nums[i]] -= 1
                i += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,1,2,2]
        o = 4
        self.assertEqual(s.countCompleteSubarrays(i), o)

    def test_two(self):
        s = Solution()
        i = [5,5,5,5]
        o = 10
        self.assertEqual(s.countCompleteSubarrays(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)