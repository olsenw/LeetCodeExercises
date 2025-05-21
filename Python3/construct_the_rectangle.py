# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A web developer needs to know how to design a web page's size. So, given a
    specific rectangular web page's area, design a rectangular web page, whose
    length L and width W satisfy the following requirements:
    * The area of the rectangular web page designed must equal to the given
      target area.
    * The width W should not be larger than the length L, which means L >= W.
    * The difference between length L and width W should be as small as
      possible.
    
    Return an array (L, W) where L and W are the length and width of the web
    page designed in sequence.
    '''
    def constructRectangle(self, area: int) -> List[int]:
        for w in range(math.isqrt(area),0,-1):
            l = area // w
            if area == l * w:
                return [l,w]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        o = [2,2]
        self.assertEqual(s.constructRectangle(i), o)

    def test_two(self):
        s = Solution()
        i = 37
        o = [37,1]
        self.assertEqual(s.constructRectangle(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)