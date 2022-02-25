# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two version numbers, version1 and version2, compare them.

    Version numbers consist of one or more revision joined by a dot '.'
    and may contain leading zeros. Every revision contains at least one
    character. Revisions 0-indexed from left to right, with the leftmost
    revision being revision 0, the next  revision being revision 1, and
    so on.

    To compare version numbers, compare their revisions in left-to-right
    order. Revisions are compared using their integer value ignoring any
    leading zeros. This means that revisions 1 and 001 are considered
    equal. If a version number does not specify a revision at an index
    then treat the revision as 0.

    Return the following:
    * if version1 < version2, return -1
    * if version1 > version2, return 1
    * otherwise return 0
    '''
    # make use of string to integer to make comparison easier
    def compareVersion_integer(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        for i in range(max(len(v1), len(v2))):
            x = v1[i] if i < len(v1) else 0
            y = v2[i] if i < len(v2) else 0
            if x < y:
                return -1
            if x > y:
                return 1
        return 0
    
    # revision of above making use of itertools
    def compareVersion_itertools(self, version1: str, version2: str) -> int:
        from itertools import zip_longest
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        for i, j in zip_longest(v1, v2, fillvalue=0):
            if i < j:
                return -1
            if i > j:
                return 1
        return 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1.01"
        j = "1.001"
        o = 0
        self.assertEqual(s.compareVersion_integer(i, j), o)
        self.assertEqual(s.compareVersion_itertools(i, j), o)

    def test_two(self):
        s = Solution()
        i = "1.0"
        j = "1.0.0"
        o = 0
        self.assertEqual(s.compareVersion_integer(i, j), o)
        self.assertEqual(s.compareVersion_itertools(i, j), o)

    def test_three(self):
        s = Solution()
        i = "0.1"
        j = "1.1"
        o = -1
        self.assertEqual(s.compareVersion_integer(i, j), o)
        self.assertEqual(s.compareVersion_itertools(i, j), o)

    def test_four(self):
        s = Solution()
        i = "01.1.02"
        j = "1.1.1"
        o = 1
        self.assertEqual(s.compareVersion_integer(i, j), o)
        self.assertEqual(s.compareVersion_itertools(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)