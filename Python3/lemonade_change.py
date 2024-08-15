# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    At a lemonade stand, each lemonade costs $5. Customers are standing in a
    queue to buy from the stand and order one at a time (in the order specified
    by bills). Each customer will only buy one lemonade and py with either a $5,
    $10, or $20 bill. The stand must provide the correct change to each customer
    so that the net transaction is that the customer pays $5.

    Note that the stand does not have any change in hand at the beginning.

    Given an integer array bills where bills[i] is the bill the ith customer
    pays, return true if the stand can provide every customer with the correct
    change, or false otherwise.
    '''
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        for b in bills:
            pass
            if b == 5:
                five += 1
            elif b == 10:
                if five >= 1:
                    ten += 1
                    five -= 1
                else:
                    return False
            else:
                if ten >= 1 and five >= 1:
                    twenty += 1
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    twenty += 1
                    five -= 3
                else:
                    return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,5,5,10,20]
        o = True
        self.assertEqual(s.lemonadeChange(i), o)

    def test_two(self):
        s = Solution()
        i = [5,5,10,10,20]
        o = False
        self.assertEqual(s.lemonadeChange(i), o)

    def test_three(self):
        s = Solution()
        i = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
        o = True
        self.assertEqual(s.lemonadeChange(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)