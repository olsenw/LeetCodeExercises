# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two categories of theme park attractions: land rides and water rides.

    * Land rides
        * landStartTime[i] the earliest time the ith land ride can be boarded.
        * landDuration[i] how long the ith land ride lasts.
    
    * Water rides
        * waterStartTime[j] the earliest time the jth water ride can be boarded.
        * waterDuration[j] how long the jth water ride lasts.
    
    A tourist must experience exactly one ride from each category, in either
    order.

    * A ride may be started at its opening time or any later moment.
    * If a ride is started at time t, it finishes at time t + duration.
    * Immediately after finishing one ride the tourist may board the other (if
      it is already open) or wait until it opens.
    
    Return the earliest possible time at which the tourist can finish both
    rides.
    '''
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        l,w = len(landStartTime), len(waterStartTime)
        # land = sorted(range(l), key=lambda i: (landStartTime[i],landDuration[i]))
        # water = sorted(range(w), key=lambda i: (waterStartTime[i],waterDuration[i]))
        answer = 10**9 + 7
        for i in range(l):
            end = landStartTime[i] + landDuration[i]
            for j in range(w):
                if waterStartTime[j] <= end:
                    answer = min(answer, end + waterDuration[j])
                else:
                    answer = min(answer, waterStartTime[j] + waterDuration[j])
        for i in range(w):
            end = waterStartTime[i] + waterDuration[i]
            for j in range(l):
                if landStartTime[j] <= end:
                    answer = min(answer, end + landDuration[j])
                else:
                    answer = min(answer, landStartTime[j] + landDuration[j])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,8]
        j = [4,1]
        k = [6]
        l = [3]
        o = 9
        self.assertEqual(s.earliestFinishTime(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = [5]
        j = [3]
        k = [1]
        l = [10]
        o = 14
        self.assertEqual(s.earliestFinishTime(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)