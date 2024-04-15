# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return False

class Solution:
    '''
    Suppose there are n versions [1,2,...,n] and the first bad one needs to be
    found.

    Given an API isBadVersion(version) which returns whether version is bad.
    Implement a function to find the first bad version. Minimize the number of
    calls to the API.
    '''
    def firstBadVersion(self, n: int) -> int:
        i,j = 1, n
        while i < j:
            k = (i + j) // 2
            if isBadVersion(k):
                j = k
            else:
                i = k + 1
        return j

class UnitTesting(unittest.TestCase):
    '''
    Tested online
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)