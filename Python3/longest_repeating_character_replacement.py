# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and an integer k. It is possible to choose any character of
    the string and change it to any other uppercase English character. This
    operation can be performed at most k times.

    Return the length of the longest substring containing the same letter after
    performing the above operation.
    '''
    def characterReplacement_wrong(self, s: str, k: int) -> int:
        n = len(s)
        i,j = 0,1
        seen = Counter()
        seen[s[0]] += 1
        answer = 1
        while j < n:
            # extend the window
            # Window does not squish correctly
            while j < n and seen.total() - seen.most_common(1)[0][1] < k:
                seen[s[j]] += 1
                j += 1
            answer = max(answer, j - i)
            # move the window
            seen[s[i]] -= 1
            i += 1
        return answer

    # inelegant
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 1
        n = len(s)
        i,j = 0,1
        seen = Counter(s[0:1])
        while j < n:
            seen[s[j]] += 1
            j += 1
            # extend the window
            while j < n and seen.total() - seen.most_common(1)[0][1] <= k:
                answer = max(answer, j - i)
                seen[s[j]] += 1
                j += 1
            if j == n and seen.total() - seen.most_common(1)[0][1] <= k:
                answer = max(answer, j - i)
            # move the window
            seen[s[i]] -= 1
            i += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ABAB"
        j = 2
        o = 4
        self.assertEqual(s.characterReplacement(i,j), o)

    def test_two(self):
        s = Solution()
        i = "AABABBA"
        j = 1
        o = 4
        self.assertEqual(s.characterReplacement(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)