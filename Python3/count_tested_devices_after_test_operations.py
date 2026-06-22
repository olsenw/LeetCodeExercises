# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array batteryPercentages having length n, denoting
    the battery percentage of n 0-indexed devices.

    Test each device i in order from 0 to n-1 by performing the following test
    operations:
    * If batteryPercentages[i] is greater than 0:
        * Increment the count of tested devices.
        * Decrease the battery percentage of all devices with indices j in the
          range [i+1, n-1] by 1 ensuring their battery percentage never goes
          below 0, ie batteryPercentages[i] = max(0, batteryPercentages[j] - 1).
        * Move to the next device.
    * Otherwise, move to the next device without performing any test.

    Return an integer denoting the number of devices that will be tested after
    performing the test operations in order.
    '''
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n = len(batteryPercentages)
        b = 0
        answer = 0
        for i in range(n):
            if batteryPercentages[i] - b > 0:
                answer += 1
                b += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,2,1,3]
        o = 3
        self.assertEqual(s.countTestedDevices(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1,2]
        o = 2
        self.assertEqual(s.countTestedDevices(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)