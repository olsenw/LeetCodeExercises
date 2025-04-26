# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string word containing distinct lowercase English letters.

    Telephone keypads have keys mapped with distinct collections of lowercase
    English letters, which can be used to form words by pushing them. For
    example, the key 2 is mapped with ["a,"b","c"] and can be pushed one time to
    type 'a', two times to type 'b', and three times to type 'c'.

    It is allowed to remap the keys numberered 2 to 9 to distinct collections of
    letters. The keys can remapped to any amount of letters, but each letter
    must be mapped to exactly one key. Find the minimum number of times the keys
    will be pushed to type the string word.

    Return the minimum number of pushes needed to type word after remapping the
    keys.
    '''
    def minimumPushes(self, word: str) -> int:
        answer = 0
        c = Counter(word)
        digit = 8
        for _,j in c.most_common():
            answer += j * (digit // 8)
            digit += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcde"
        o = 5
        self.assertEqual(s.minimumPushes(i), o)

    def test_two(self):
        s = Solution()
        i = "xycdefghij"
        o = 12
        self.assertEqual(s.minimumPushes(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)