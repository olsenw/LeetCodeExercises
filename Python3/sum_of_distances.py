# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict, deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums. There exists an array arr of length
    nums.length, where arr[i] is the sum of |i - j| over all j such that
    nums[j] == nums[i] and j != i. If there is no such j set arr[i] to be 0.

    Return the array arr.
    '''
    # brute force O(n^2)
    def distance_tle(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i,j in enumerate(nums):
            d[j].append(i)
        answer = []
        for x,y in enumerate(nums):
            a = 0
            for i in d[y]:
                a += abs(i - x)
            answer.append(a)
        return answer

    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i,j in enumerate(nums):
            d[j].append(i)
        # p = {i:deque(d[i][:1]) for i in d if len(d[i]) > 1}
        p = {i:deque([0]) for i in d if len(d[i]) > 1}
        for i in p:
            # for j in d[i][1:]:
            for j in d[i]:
                p[i].append(p[i][-1] + j)
        answer = []
        for i,j in enumerate(nums):
            if j not in p:
                answer.append(0)
                continue
            n = len(d[j])
            l = p[j].popleft()
            l = (i * (n - len(p[j]))) - l
            n = len(p[j]) - 1
            r = (p[j][-1] - p[j][0]) - (i * n)
            answer.append(abs(l) + abs(r))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,1,1,2]
        o = [5,0,3,4,0]
        self.assertEqual(s.distance(i), o)

    def test_two(self):
        s = Solution()
        i = [0,5,3]
        o = [0,0,0]
        self.assertEqual(s.distance(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1,1,1,1,1,1,1,1]
        o = [45,37,31,27,25,25,27,31,37,45]
        self.assertEqual(s.distance(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)