# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a restaurant with a single chef. Given an array customers, where
    customers[i] = [arrivali, timei]:
    * arrivali is the arrival of the ith customer. The arrival times are sorted
      in non-decreasing order.
    * timei is the time needed to prepare the order of the ith customer.

    When a customer arrives, they give the chef their order, and the chef starts
    preparing it once they are idle. The customer waits till the chef finishes
    preparing their order. The chef does not prepare food for more than one
    customer at a time. The chef prepares food for customers in the order they
    were given in the input.

    Return the average waiting time of all customers. Solutions within 10^-5
    from the actual answer are considered accepted.
    '''
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        s = 0
        t = 0
        for a,b in customers:
            t = max(a,t) + b
            s += t - a
        return s / len(customers)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,5],[4,3]]
        o = 5.0
        self.assertEqual(s.averageWaitingTime(i), o)

    def test_two(self):
        s = Solution()
        i = [[5,2],[5,4],[10,3],[20,1]]
        o = 3.25
        self.assertEqual(s.averageWaitingTime(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)