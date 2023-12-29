# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array items, where each items[i] = [typei, colori, namei] describes
    the type, color, and name of the ith item. Also given a rule represented by
    two strings, ruleKey and ruleValue.

    The ith item is said to match the rule if one of the following is true:
    * ruleKey == "type" and ruleValue == typei
    * ruleKey == "color" and ruleValue == colori
    * ruleKey == "name" and ruleValue == namei

    Return the number of items that match the given rule.
    '''
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rules = {"type":0, "color":1, "name":2}
        index = rules[ruleKey]
        return sum(ruleValue == i[index] for i in items)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
        j = "color"
        k = "silver"
        o = 1
        self.assertEqual(s.countMatches(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
        j = "type"
        k = "phone"
        o = 2
        self.assertEqual(s.countMatches(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)