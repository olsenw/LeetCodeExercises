# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There are n gas stations along a circular route, where the amount of
    gas at the ith station is gas[i].

    There exists a car with an unlimited gas tank, starting at one of 
    these gas stations.

    It costs cost[i] units of gas to travel from the ith station to the
    next (i + 1)th station.

    Given two integer arrays gas and cost, return the starting gas 
    station's index if it is possible to travel the whole circuit in 
    clockwise direction, otherwise return -1. If a solution exists it
    is guaranteed to be unique.
    '''
    def canCompleteCircuit_brute(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # base case of single gas staion
        if n == 1:
            # evaluates to a bool and subtracts one (1-1 = 0, 0-1 = -1)
            return (gas[0] >= cost[0]) - 1
        # cycle through all the starting positions
        for s in range(n):
            # check if can complete a cycle
            g = gas[s] - cost[s]
            i = s + 1 if s + 1 < n else 0
            while s != i and g >= 0:
                g += gas[i] - cost[i]
                i = i + 1 if i + 1 < n else 0
            if s == i and g >= 0:
                return s
        return -1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # total sum to check if circuit exists
        s = 0
        # gas for current run
        g = 0
        # starting index of run
        n = 0
        # check all the nodes
        for i in range(len(gas)):
            # difference between gas at staion and cost till next
            d = gas[i] - cost[i]
            # running total
            s += d
            # current run total
            g += d
            # see if current run failed
            if g < 0:
                # chain cannot be any of the pased over, try next
                n = i + 1
                # reset current run
                g = 0
        # answer
        return -1 if s < 0 else n

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        c = [3,4,5,1,2]
        #   -2-4-6-3 0
        #          3 6 4 2 0
        o = 3
        self.assertEqual(s.canCompleteCircuit_brute(i,c), o)
        self.assertEqual(s.canCompleteCircuit(i,c), o)

    def test_two(self):
        s = Solution()
        i = [2,3,4]
        c = [3,4,3]
        o = -1
        self.assertEqual(s.canCompleteCircuit_brute(i,c), o)
        self.assertEqual(s.canCompleteCircuit(i,c), o)

    def test_three(self):
        s = Solution()
        i = [1]
        c = [3]
        o = -1
        self.assertEqual(s.canCompleteCircuit_brute(i,c), o)
        self.assertEqual(s.canCompleteCircuit(i,c), o)

    def test_four(self):
        s = Solution()
        i = [4]
        c = [3]
        o = 0
        self.assertEqual(s.canCompleteCircuit_brute(i,c), o)
        self.assertEqual(s.canCompleteCircuit(i,c), o)

    def test_five(self):
        s = Solution()
        i = [5,8,2,8]
        c = [6,5,6,6]
        #   -1 2-2 0
        #          2 1 4 0
        o = 3
        self.assertEqual(s.canCompleteCircuit_brute(i,c), o)
        self.assertEqual(s.canCompleteCircuit(i,c), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)