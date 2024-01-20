# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers arr, sort the array by performing a series of
    pancake flips.

    In one pancake flip perform the following steps:
    * Choose an integer k where 1 <= k <= arr.length.
    * Reverse the sub-array arr[0...k-1] (0-indexed).

    For example, if arr = [3,2,1,4] and a pancake flip choosing k = 3, reverse
    the subarray [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

    Return an array of the k values corresponding to a sequence of pancake flips
    that sort arr. Any valid answer that sorts the array within 10 * arr.length
    flips will be accepted.
    '''
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        answer = []
        # find final positions that are incorrect
        for i in range(n-1,0,-1):
            if arr[i] == i + 1:
                continue
            for j in range(i, -1, -1):
                if arr[j] == i + 1:
                    break
            pass
            answer.append(j+1)
            arr = arr[:j+1][::-1] + arr[j+1:]
            if i != j:
                answer.append(i+1)
                arr = arr[:i+1][::-1] + arr[i+1:]
            pass
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,4,1]
        o = [3,4,2,3,1,2]
        self.assertEqual(s.pancakeSort(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3]
        o = []
        self.assertEqual(s.pancakeSort(i), o)

    def test_three(self):
        s = Solution()
        i = [3,1,2]
        o = [1,3,1,2]
        self.assertEqual(s.pancakeSort(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)