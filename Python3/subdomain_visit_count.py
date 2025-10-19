# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A website domain "discuss.leetcode.com" consists of various subdomains. At
    the top level is the "com" domain, at the next level is "leetcode.com" and
    at the lowest level "discuss.leetcode.com". When a domain like
    "discuss.leetcode.com" is visited, so are the parent domains "leetcode.com"
    # and "com" implicitly.

    A count-paired domain is a domain that has one of two formats "rep d1.d2.d3"
    or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 
    is the domain itself.

    Given an array of count-paired domains cpdomains, return an array of the
    count-paired domains of each subdomain in the input. The answer may be
    returned in any order.
    '''
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = Counter()
        for domain in cpdomains:
            count, domain = domain.split(" ")
            count = int(count)
            domain = domain.split(".")
            for i in range(len(domain)):
                c[".".join(domain[i:])] += count
        return [f'{c[i]} {i}' for i in c]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["9001 discuss.leetcode.com"]
        o = sorted(["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"])
        self.assertEqual(sorted(s.subdomainVisits(i)), o)

    def test_two(self):
        s = Solution()
        i = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
        o =  ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
        self.assertEqual(sorted(s.subdomainVisits(i)), sorted(o))

if __name__ == '__main__':
    unittest.main(verbosity=2)