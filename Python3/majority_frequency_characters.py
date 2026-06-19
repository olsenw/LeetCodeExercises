# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters.

    The frequency group for a value k is the set of characters that appear
    exactly k times in s.

    The majority frequency group is the frequency group that contains the
    largest number of distinct characters.

    Return a string containing all the characters in the majority frequency
    group, in any order. If two of more frequency groups tie for that largest
    size, pick the group whose frequency k is larger.
    '''
    def majorityFrequencyGroup(self, s: str) -> str:
        f = Counter(s)
        c = Counter(f[i] for i in f)
        a = max(sorted((i for i in c), reverse=True), key=lambda x:c[x])
        return "".join(i for i in f if f[i] == a)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aaabbbccdddde"
        o = "ab"
        self.assertEqual("".join(sorted(s.majorityFrequencyGroup(i))), o)

    def test_two(self):
        s = Solution()
        i = "abcd"
        o = "abcd"
        self.assertEqual("".join(sorted(s.majorityFrequencyGroup(i))), o)

    def test_three(self):
        s = Solution()
        i = "pfpfgi"
        o = "fp"
        self.assertEqual("".join(sorted(s.majorityFrequencyGroup(i))), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)