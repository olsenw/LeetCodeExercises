# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of unique integers, arr, where each integer arr[i] is
    strictly greater than 1.

    A binary tree can be made using theses integers, with each integer
    being used any number of times. Each non-leaf node's value should be
    equal to the product of the values of its children.

    Return the number of binary trees that can be made. The answer may
    be large so return the answer modulo 10^9 + 7.
    '''
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # going small to large to not double count
        arr.sort()
        dp = {a:1 for a in arr}
        # go through the whole array
        for i in range(len(arr)):
            # test all values smaller than current
            for j in range(i):
                # check if valid multiplication
                if not arr[i] % arr[j] and arr[i] // arr[j] in dp:
                    # number of ways to do left node * right node
                    dp[arr[i]] += dp[arr[j]] * dp[arr[i] // arr[j]]
        return sum(dp.values()) % (10**9 + 7)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,4]
        o = 3
        self.assertEqual(s.numFactoredBinaryTrees(i), o)

    def test_two(self):
        s = Solution()
        i = [2,4,5,10]
        o = 7
        self.assertEqual(s.numFactoredBinaryTrees(i), o)

    def test_three(self):
        s = Solution()
        i = [18,3,6,2]
        o = 12
        self.assertEqual(s.numFactoredBinaryTrees(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)