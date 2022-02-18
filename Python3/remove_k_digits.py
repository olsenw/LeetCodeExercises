# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given string num representing a non-negative integer num, and an
    integer k, return the smallest possible integer after removing k 
    digits from num.

    Note: remove all leading zeros.
    '''
    # figured out after reading leetcode discusion posts pointing out
    # pattern for removing digit... should have seen for myself when
    # doing removals by hand... very frustrating
    # https://leetcode.com/problems/remove-k-digits/discuss/
    def removeKdigits(self, num: str, k: int) -> str:
        # monotonicity increasing stack
        monotonic = []
        for n in num:
            # still have digits to remove
            # somthing is on monotonic stack
            # the digit to left is larger than digit right num[i-1] > num[i]
            while k and monotonic and monotonic[-1] > n:
                # corrects stack
                monotonic.pop()
                # digit is removed
                k -= 1
            # put charaters on stack (gets remaining when remove done)
            monotonic.append(n)
        # remove digits from right if num is monotonic (digits left to remove)
        while k:
            monotonic.pop()
            k -= 1
        # turn monotonic stack into string
        ans = "".join(monotonic)
        while ans and ans[0] == "0":
            ans = ans[1:]
        # check that there is an answer otherwise return "0"
        return ans if ans else "0"

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1432219"
        j = 3
        # removal 3
        # 432219 132219 142219 143219 143219 143229 143221 (choose 4 ie 132219)
        # 32219 12219 13219 13219 13229 13221 (choose 3 ie 12219)
        # 2219 1219 1219 1229 1221 (choose 2 ie 1219)
        # building (7-3=4)
        # 1 4 3 2 2 1 9 (pick 1 latter one as positionally smaller)
        # 11 41 31 21 21 19 (pick 1)
        # 141 131 121 121 119 (pick 9)
        # 1419 1319 1219 1219 (pick 2 latter one positionally smaller)
        o = "1219"
        self.assertEqual(s.removeKdigits(i,j), o)

    def test_two(self):
        s = Solution()
        i = "10200"
        j = 1
        # removing
        # 0200 1200 1000 1020 1020
        # building
        # 1 0 2 0 0
        # 10 00 20 00
        # 100 000 200
        # 1000 0200
        o = "200"
        self.assertEqual(s.removeKdigits(i,j), o)

    def test_three(self):
        s = Solution()
        i = "10"
        j = 2
        o = "0"
        self.assertEqual(s.removeKdigits(i,j), o)

    def test_four(self):
        s = Solution()
        i = "9"
        j = 1
        o = "0"
        self.assertEqual(s.removeKdigits(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)