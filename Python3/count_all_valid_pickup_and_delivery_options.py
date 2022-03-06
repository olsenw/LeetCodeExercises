# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given n orders, each order consists of pickup and delivery services.

    Count all valid pickup/delivery sequences given that delivery(i) is
    always after pickup(i).

    Return answer modulo 10^9+7.
    '''
    # power of permutations
    # when pick Pi there are 2*i-1 places Di can go into previous permutations
    def countOrders(self, n: int) -> int:
        # modulo = 10**9+7
        modulo = 1_000_000_007
        dp = 1
        for i in range(2,n+1):
            # n * dp[n - 1] * (2 * (n - 1) + 1)
            dp = (dp * i * (2 * i - 1)) % modulo
        return dp

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.countOrders(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = 6
        self.assertEqual(s.countOrders(i), o)

    def test_three(self):
        s = Solution()
        i = 3
        o = 90
        self.assertEqual(s.countOrders(i), o)

    def test_four(self):
        s = Solution()
        i = 4
        o = 2520
        self.assertEqual(s.countOrders(i), o)

    def test_five(self):
        s = Solution()
        i = 5
        o = 113400
        self.assertEqual(s.countOrders(i), o)

    def test_eight(self):
        s = Solution()
        i = 8
        o = 729647433
        self.assertEqual(s.countOrders(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)