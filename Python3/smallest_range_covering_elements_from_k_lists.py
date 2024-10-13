# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given k lists of sorted integers in non-decreasing order. Find the smallest
    range that includes at least one number from each of the k lists.

    Define the range [a,b] as smaller than range [c,d] if b-a < d-c or a<c if
    b-a == d-c.
    '''
    # time limit exceeded passes 86 / 90 testcases
    def smallestRange_tle(self, nums: List[List[int]]) -> List[int]:
        def r(nums: List[int]) -> List[int]:
            x,y = min(n[0] for n in nums), max(n[0] for n in nums)
            return [y-x, x, y]
        h = [[n[0],0,i] for i,n in enumerate(nums)]
        heapq.heapify(h)
        answer = r(h)
        while h[0][1] < len(nums[h[0][2]])-1:
            _,x,y = heapq.heappop(h)
            heapq.heappush(h, [nums[y][x+1], x+1, y])
            a = r(h)
            answer = min(answer, a)
        return answer[1:]

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h = [[n[0],0,i] for i,n in enumerate(nums)]
        hmax = max(i for i,_,_ in h)
        heapq.heapify(h)
        answer = [hmax - h[0][0], h[0][0], hmax]
        while h[0][1] < len(nums[h[0][2]])-1:
            _,x,y = heapq.heappop(h)
            heapq.heappush(h, [nums[y][x+1], x+1, y])
            hmax = max(hmax, nums[y][x+1])
            answer = min(answer, [hmax - h[0][0], h[0][0], hmax])
        return answer[1:]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
        o = [20,24]
        self.assertEqual(s.smallestRange(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3],[1,2,3],[1,2,3]]
        o = [1,1]
        self.assertEqual(s.smallestRange(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)