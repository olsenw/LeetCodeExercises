# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums of n integers and two integers k and x.

    The x-sum of an array is calculated by the following procedure:
    * Count the occurrences of all elements in the array.
    * Keep only the occurrences of the top x most frequent elements. If two
      elements. If two elements have the same number of occurrences, the element
      with the bigger value is considered more frequent.
    * Calculate the sum of th resulting array.

    Note that if an array has less than x distinct elements, its x-sum is the
    sum of the array.

    Return an integer array answer of length n - k + 1 where answer[i] is the
    x-sum of the subarray nums[i.. i + k - 1].
    '''
    def findXSum_fails(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []
        for i in range(n - k + 1):
            c = Counter(nums[i:i+k-1])
            answer.append(sum(j for _,j in c.most_common(x)))
        return answer

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []
        for i in range(n - k + 1):
            c = Counter(nums[i:i+k])
            s = sorted(((c[j],j) for j in c), reverse=True)[:x]
            pass
            answer.append(sum(a*b for a,b in s))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,2,2,3,4,2,3]
        j = 6
        k = 2
        o = [6,10,12]
        self.assertEqual(s.findXSum(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [3,8,7,8,7,5]
        j = 2
        k = 2
        o = [11,15,15,15,12]
        self.assertEqual(s.findXSum(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)