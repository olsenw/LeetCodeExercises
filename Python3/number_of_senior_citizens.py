# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array string details. Each element of details provides
    information about a given passenger compressed into a string of length 15.
    The system is such that:
    * The first ten characters consist of the phone number of passengers.
    * The next character denotes the gender of the person.
    * The following two characters are used to indicate the age of the person.
    * The last two characters determine the seat allotted to that person.

    Return the number of passengers who are strictly more than 60 years old.
    '''
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(d[11:13]) > 60 for d in details)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["7868190130M7522","5303914400F9211","9273338290F4010"]
        o = 2
        self.assertEqual(s.countSeniors(i), o)

    def test_two(self):
        s = Solution()
        i = ["1313579440F2036","2921522980M5644"]
        o = 0
        self.assertEqual(s.countSeniors(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)