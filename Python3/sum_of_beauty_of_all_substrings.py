# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The beauty of a string is the difference in frequencies between the most
    frequent and least frequent characters.

    Given a string s, return the sum of beauty of all of its substrings.
    '''
    def beautySum_single(self, s: str) -> int:
        c = Counter(s).most_common()
        return c[0][1] - c[-1][1]

    def beautySum(self, s: str) -> int:
        answer = 0
        for i in range(len(s)):
            c = Counter()
            for j in range(i, len(s)):
                c[s[j]] += 1
                answer += max(c[k] for k in c)
                answer -= min(c[k] for k in c)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aabcb"
        o = 5
        self.assertEqual(s.beautySum(i), o)

    def test_two(self):
        s = Solution()
        i = "aabcbaa"
        o = 17
        self.assertEqual(s.beautySum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)