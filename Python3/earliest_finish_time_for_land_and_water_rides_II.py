# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
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
    # based on hints for binary search
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        answer = 10**9+7
        # length of arrays
        l,w = len(landStartTime),len(waterStartTime)
        # sort land index based on start time
        land = sorted((i for i in range(l)), key = lambda i: landStartTime[i])
        # minimum prefix of duration sorted by start time
        landPrefix = [0] * l
        landPrefix[0] = landDuration[land[0]]
        for i in range(1,l):
            landPrefix[i] = min(landPrefix[i-1], landDuration[land[i]])
        # minimum suffix of start+duration sorted by start time
        landSuffix = [0] * l
        landSuffix[-1] = landStartTime[land[-1]] + landDuration[land[-1]]
        for i in range(l-2,-1,-1):
            landSuffix[i] = min(landSuffix[i+1], landStartTime[land[i]] + landDuration[land[i]])
        # sort water index based on start time
        water = sorted((i for i in range(w)), key = lambda i: waterStartTime[i])
        # minimum prefix of duration sorted by start time
        waterPrefix = [0] * w
        waterPrefix[0] = waterDuration[water[0]]
        for i in range(1,w):
            waterPrefix[i] = min(waterPrefix[i-1], waterDuration[water[i]])
        # minimum suffix of start+duration sorted by start time
        waterSuffix = [0] * w
        waterSuffix[-1] = waterStartTime[water[-1]] + waterDuration[water[-1]]
        for i in range(w-2,-1,-1):
            waterSuffix[i] = min(waterSuffix[i+1], waterStartTime[water[i]] + waterDuration[water[i]])
        # find answer based on land ride then water ride
        for i in range(l):
            finish = landStartTime[land[i]] + landDuration[land[i]]
            # split water into rides ready to go before finish and rides need to wait
            j = bisect.bisect_right(water, finish, key=lambda x:waterStartTime[x])
            # get lowest duration water ride ready to go
            p = waterPrefix[j-1] if waterStartTime[water[j-1]] <= finish else 10**9+7
            # get soonest complete water ride that need to wait for
            s = waterSuffix[j] if j < w else 10**9+7
            answer = min(answer, finish + p)
            answer = min(answer, s)
        # find answer based on water ride then land ride
        for i in range(w):
            finish = waterStartTime[water[i]] + waterDuration[water[i]]
            j = bisect.bisect_right(land, finish, key=lambda x:landStartTime[x])
            p = landPrefix[j-1] if landStartTime[land[j-1]] <= finish else 10**9+7
            s = landSuffix[j] if j < l else 10**9+7
            answer = min(answer, finish + p)
            answer = min(answer, s)
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

    def test_three(self):
        s = Solution()
        i = [80,71]
        j = [27,47]
        k = [45,3,64,7,25,45,6]
        l = [40,39,66,64,24,74,49]
        o = 107
        self.assertEqual(s.earliestFinishTime(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)