# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given three integers n, m and k. Consider the following algorithm to find
    the maximum element of an array of positive integers.

    maximum_value = -1
    maximum_index = -1
    search_cost = 0
    n = arr.length
    for (i = 0; i < n; i++) {
        if (maximum_value < arr[i]) {
            maximum_value = arr[i]
            maximum_index = i
            search_cost = search_cost + 1
        }
    }
    return maximum_index

    Build an array arr which has the following properties:
    * arr has exactly n integers.
    * 1 <= arr[i] <= m where (0 <= i < n).
    * After applying the mentioned algorithm to arr, the value search_cost is
      equal to k.

    Return the number of ways to build the array arr under the mentioned
    conditions. As the answer may grow large, the answer must be computed modulo
    10^9 + 7.
    '''
    # based on LeetCode editorial
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        modulo = 10**9 + 7
        # a starting index b maximum integer c search cost
        @cache
        def dp(a,b,c):
            # unable to add any more elements to array
            if a == n:
                # 1 possible solution if the correct number of max values are added
                return 1 if c == 0 else 0
            # too many maximum values (bail)
            if c < 0:
                return 0
            # all the possible numbers that can be appended without being a new max
            answer = (b * dp(a + 1, b, c)) % modulo
            # all the possible numbers that can be appended and are a new max
            for i in range(b + 1, m + 1):
                # modulo addition
                answer = (answer +  dp(a + 1, i, c - 1)) % modulo
            return answer
        return dp(0, 0, k)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = (2,3,1)
        o = 6
        self.assertEqual(s.numOfArrays(*i), o)

    def test_two(self):
        s = Solution()
        i = (5,2,3)
        o = 0
        self.assertEqual(s.numOfArrays(*i), o)

    def test_three(self):
        s = Solution()
        i = (9,1,1)
        o = 1
        self.assertEqual(s.numOfArrays(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)