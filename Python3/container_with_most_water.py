# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array height of length n. There are n vertical
    lines drawn such that the two endpoints of the ith line are (i, 0)
    and (i, height[i]).

    Find two lines that together with the x-axis form a container, such
    that the container contains the most water.

    Return the maximum amount of water a container can store.

    Note that container is not slanted.

    Example: [3,1,1,2] => 6
    4 
    3 *                 * is vertical line
    2 * O   O   O *     O is water of max container
    1 * O * O * O *
    '''
    def maxArea_brute(self, height: List[int]) -> int:
        m = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                w = j - i
                h = min(height[i], height[j])
                m = max(m, w * h)
        return m

    def maxArea(self, height: List[int]) -> int:
        m = 0
        i = 0
        j = len(height) - 1
        while i < j:
            a, b = height[i], height[j]
            m = max(m, (j - i) * min(a, b))
            if a <= b:
                i += 1
            else:
                j -= 1
        return m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,8,6,2,5,4,8,3,7]
        o = 49
        self.assertEqual(s.maxArea_brute(i), o)
        self.assertEqual(s.maxArea(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1]
        o = 1
        self.assertEqual(s.maxArea_brute(i), o)
        self.assertEqual(s.maxArea(i), o)

    def test_three(self):
        s = Solution()
        i = [3,2,1,1]
        o = 3
        self.assertEqual(s.maxArea_brute(i), o)
        self.assertEqual(s.maxArea(i), o)

    def test_four(self):
        s = Solution()
        i = [3,1,1,2]
        o = 6
        self.assertEqual(s.maxArea_brute(i), o)
        self.assertEqual(s.maxArea(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)