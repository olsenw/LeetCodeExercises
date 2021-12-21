# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer n, return true if it is a power of two; otherwise
    false.

    An integer n is a power of two, if there exists an integer x such 
    that n == 2^x.
    '''
    def isPowerOfTwo_loops(self, n: int) -> bool:
        # no negative number can be found by 2^k (only values > 0) 
        if n <= 0:
            return False
        foundOne = False
        for i in format(n, "b"):
            if i == '1':
                if foundOne:
                    return False
                foundOne = True
        return foundOne

    '''
    Given an integer n, return true if it is a power of two; otherwise
    false.
    
    Do so without using loops or recursion.
    '''
    def isPowerOfTwo_fancy(self, n: int) -> bool:
        # no negative number can be found by 2^k (only values > 0) 
        if n <= 0:
            return False
        '''
        subtracting 1 from a 2^k number forces all following bits to one
        if bitwise & this should result in zero.
        n   = (0100) 4      n   = (0101) 5
        n-1 = (0011) 3      n-1 = (0100) 4
        &   = (0000) 0      &   = (0100) 4 != 0
        '''
        return n & (n-1) == 0

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        self.assertEqual(s.isPowerOfTwo_loops(1), True)
        self.assertEqual(s.isPowerOfTwo_fancy(1), True)

    def test_two(self):
        s = Solution()
        self.assertEqual(s.isPowerOfTwo_loops(16), True)
        self.assertEqual(s.isPowerOfTwo_fancy(16), True)

    def test_three(self):
        s = Solution()
        self.assertEqual(s.isPowerOfTwo_loops(3), False)
        self.assertEqual(s.isPowerOfTwo_fancy(3), False)
    
    def test_four(self):
        s = Solution()
        self.assertEqual(s.isPowerOfTwo_loops(0), False)
        self.assertEqual(s.isPowerOfTwo_fancy(0), False)
        
    
    def test_five(self):
        s = Solution()
        self.assertEqual(s.isPowerOfTwo_loops(-2), False)
        self.assertEqual(s.isPowerOfTwo_fancy(-2), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)