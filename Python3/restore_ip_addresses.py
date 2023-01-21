# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import itertools
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A valid IP address consists of exactly four integers separated by single
    dots. Each integer is between 0 and 255 (inclusive) and cannot have leading
    zeros.

    Given a string s containing only digits, return all possible valid IP
    addresses that can be formed by inserting dots into s. It is not possible to
    reorder or remove digits in s. 
    '''
    # brute force all combinations
    # leetcode solution, comment by khalid-salad
    # https://leetcode.com/problems/restore-ip-addresses/solutions/2868540/restore-ip-addresses/?orderBy=most_votes
    # works on the basis that 1 <= len(n) <= 20 leaving only 969 combinations to check
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        # base case impossible
        if n < 4:
            return []
        def lead0(s):
            return s[0] == "0" and s != "0"
        def valid(p):
            return not lead0(p) and int(p) <= 255
        def ip(split):
            return all(valid(p) for p in split)
        answer = []
        for i,j,k in itertools.combinations(range(1, n), 3):
            check = [s[:i], s[i:j], s[j:k], s[k:]]
            if ip(check):
                answer.append('.'.join(check))
            pass
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "25525511135"
        o = ["255.255.11.135","255.255.111.35"]
        self.assertEqual(sorted(s.restoreIpAddresses(i)), o)

    def test_two(self):
        s = Solution()
        i = "0000"
        o = ["0.0.0.0"]
        self.assertEqual(sorted(s.restoreIpAddresses(i)), o)

    def test_three(self):
        s = Solution()
        i = "101023"
        o = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
        self.assertEqual(sorted(s.restoreIpAddresses(i)), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)