# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import re
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given three arrays of length n that describe the properties of n coupons:
    code, businessLine, and isActive. The ith coupon has:
    * code[i]: a string representing the coupon identifier.
    * businessLine[i]: a string denoting the business category of the coupon.
    * isActive[i]: a boolean indicating whether the coupon is currently active.

    A coupon is considered valid if all of the following conditions hold:
    1. code[i] is non-empty and consists only of alphanumeric characters
       (a-z, A-Z, 0-9) and underscores (_).
    2. businessLine[i] is one of the following four categories: "electronics",
       "grocery", "pharmacy", "restaurant".
    3. isActive[i] is true.

    Return an array of the codes of all valid coupons, sorted first by their
    businessLine in the order: "electronics", "grocery", "pharmacy",
    "restaurant", and then by code in lexicographical (ascending) order within
    each category.
    '''
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        indices = [i for i in range(len(code)) if isActive[i] and businessLine[i] in order and re.fullmatch("[a-zA-Z0-9_]+", code[i])]
        indices.sort(key=lambda i:(order[businessLine[i]], code[i]))
        return [code[i] for i in indices]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["SAVE20","","PHARMA5","SAVE@20"]
        j = ["restaurant","grocery","pharmacy","restaurant"]
        k = [True,True,True,True]
        o = ["PHARMA5","SAVE20"]
        self.assertEqual(s.validateCoupons(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"]
        j = ["grocery","electronics","invalid"]
        k = [False,True,True]
        o = ["ELECTRONICS_50"]
        self.assertEqual(s.validateCoupons(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)