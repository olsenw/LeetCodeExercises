# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers arr and an integer target.

    Find two non-overlapping sub-arrays of arr each with a sum equal target.
    There can be multiple answers, find the answer where the sum of the lengths
    of the two sub-arrays is minimum.

    Return the minimum sum of the lengths of the two required sub-arrays, or
    return -1 if it is impossible to find two such sub-arrays.
    '''
    def minSumOfLengths_tle(self, arr: List[int], target: int) -> int:
        n = len(arr)
        possible = []
        s = 0
        i = 0
        for j in range(n):
            s += arr[j]
            while i < j and s > target:
                s -= arr[i]
                i += 1
            if s == target:
                possible.append((i,j))
        m = len(possible)
        if m < 2:
            return -1
        answer = n+1
        for i in range(m):
            x,y = possible[i]
            j = bisect.bisect(possible,(y+1,),lo=i+1)
            for k in range(j, m):
                a,b = possible[k]
                answer = min(answer, y-x+1 + b-a+1)
        return answer if answer < n+1 else -1

    # based on hints
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix = [n+1] * n
        s = 0
        i = 0
        for j in range(n):
            s += arr[j]
            while i < j and s > target:
                s -= arr[i]
                i += 1
            if s == target:
                prefix[j] = j-i+1
        for i in range(1,n):
            prefix[i] = min(prefix[i], prefix[i-1])
        suffix = [n+1] * n
        s = 0
        i = n-1
        for j in range(n-1,-1,-1):
            s += arr[j]
            while i > j and s > target:
                s -= arr[i]
                i -= 1
            if s == target:
                suffix[j] = i-j+1
        for i in range(n-2,-1,-1):
            suffix[i] = min(suffix[i],suffix[i+1])
        answer = n+1
        for i in range(n-1):
            answer = min(answer, prefix[i]+suffix[i+1])
        return answer if answer < n+1 else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,2,4,3]
        j = 3
        o = 2
        self.assertEqual(s.minSumOfLengths(i,j), o)

    def test_two(self):
        s = Solution()
        i = [7,3,4,7]
        j = 7
        o = 2
        self.assertEqual(s.minSumOfLengths(i,j), o)

    def test_three(self):
        s = Solution()
        i = [4,3,2,6,2,3,4]
        j = 6
        o = -1
        self.assertEqual(s.minSumOfLengths(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,1,1,1,1]
        j = 3
        o = -1
        self.assertEqual(s.minSumOfLengths(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)