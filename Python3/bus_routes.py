# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from math import inf
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
'''
class Solution:
    '''
    based on leetcode discussion post
    '''
    def numBusesToDestination(self, routes, source, target):
        # already at target location
        if source == target:
            return 0
        
        # no path to target location (too few bus stops)
        m = max(max(r) for r in routes)
        if m < target:
            return -1
        
        n = len(routes)
        # minimum number of buses to reach stop
        buses = [inf] * (m + 1)
        buses[source] = 0

        flag = True
        # update routes
        while flag:
            flag = False
            for r in routes:
                i = inf
                for j in r:
                    i = min(i, buses[j])
                i += 1
                for j in r:
                    if buses[j] > i:
                        buses[j] = i
                        flag = True
        
        return buses[target] if buses[target] < inf else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12)
        o = -1
        self.assertEqual(s.numBusesToDestination(*i), o)

    def test_two(self):
        s = Solution()
        i = ([[1,2,7],[3,6,7]], 1, 6)
        o = 2
        self.assertEqual(s.numBusesToDestination(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)