# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Every valid email consists of a local name and a domain name, separated by
    the '@' sign. Besides lowercase letters, the email may contain one or more
    '.' or '+'.

    If extra periods '.' are added between some characters in the local name
    part of an email address, mail sent there will be forwarded to the same
    address without dots in the local name. Note that this rule does note apply
    to domain names.

    if '+' is added to to the local name, everything after the first plus sign
    will be ignored. This allows certain emails to be filtered. Note that this
    rule does note apply to domain names.

    It is possible to use both of these rules at the same time.

    Given an array of stings emails where an email will be sent to each
    emails[i], return the number of different addresses that actually receive
    mails.
    '''
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for e in emails:
            local, domain = e.split('@')
            local = local.replace('.','')
            plus = local.find('+')
            if plus > -1:
                local = local[:plus]
            unique.add((local,domain))
        return len(unique)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        o = 2
        self.assertEqual(s.numUniqueEmails(i), o)

    def test_two(self):
        s = Solution()
        i = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
        o = 3
        self.assertEqual(s.numUniqueEmails(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)