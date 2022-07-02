# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a rectangular cake of size h x w and two arrays of integers
    horizontalCuts and verticalCuts where:
    * horizontalCuts[i] is the distance from the top of the rectangular
      cake to the ith horizontal cut.
    * verticalCuts[i] is the distance from the left of the rectangular
      cake to the ith vertical cut.

    Return the maximum area of a piece of cake after all cuts are made.
    Since the answer can be large return it modulo 10^9+7
    '''
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # find sizes of horizontal slices
        horizontalCuts.sort()
        horizontalCuts.append(h)
        for i in range(len(horizontalCuts) - 1, 0, -1):
            horizontalCuts[i] -= horizontalCuts[i - 1]
        # find sizes of vertical slices
        verticalCuts.sort()
        verticalCuts.append(w)
        for i in range(len(verticalCuts) - 1, 0, -1):
            verticalCuts[i] -= verticalCuts[i - 1]
        # modulo largest slice multiplied by largest slice
        modulo = 1000000007
        horizontal = max(horizontalCuts) % modulo
        vertical = max(verticalCuts) % modulo
        return (horizontal * vertical) % modulo

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = 4
        k = [1,2,4]
        l = [1,3]
        o = 4
        self.assertEqual(s.maxArea(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = 4
        k = [3,1]
        l = [1]
        o = 6
        self.assertEqual(s.maxArea(i,j,k,l), o)

    def test_three(self):
        s = Solution()
        i = 5
        j = 4
        k = [3]
        l = [3]
        o = 9
        self.assertEqual(s.maxArea(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)