# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a string word and an integer k.

    word is considered to by k-special if abs(freq(word[i]) - word[j]) <= k for
    all indices i and j in the string.

    Here freq(x) denotes the frequency of the character x in word, and abs(y)
    denotes the absolute value of y.

    Return the minimum number of characters that need to be deleted to make word
    k-special.
    '''
    def minimumDeletions_wrong(self, word: str, k: int) -> int:
        answer = len(word)
        c = Counter(word)
        for i in c:
            a = 0
            for j in c:
                if i == j or abs(c[i] - c[j]) <= k:
                    continue
                a += c[j]
                if c[j] > c[i]:
                    a -= c[i] + k
            answer = min(answer, a)
        return answer

    def minimumDeletions_wrong2(self, word: str, k: int) -> int:
        answer = len(word)
        c = Counter(word)
        s = sorted(c, key=lambda x : c[x])
        n = len(s)
        for i in s:
            x,y = 0,0
            while abs(c[i] - c[s[x]]) > k:
                y += c[s[x]]
                x += 1
            x = n - 1
            while abs(c[i] - c[s[x]]) > k:
                y += c[s[x]] - (c[i] + k)
                x -= 1
            answer = min(answer, y)
        return answer

    def minimumDeletions(self, word: str, k: int) -> int:
        answer = len(word)
        c = Counter(word)
        s = sorted(c, key=lambda x: c[x])
        n = len(s)
        for i in s:
            x,y = 0,0
            while c[i] > c[s[x]]:
                y += c[s[x]]
                x += 1
            t = c[i] + k
            x = n - 1
            while t < c[s[x]]:
                y += c[s[x]] - t
                x -= 1
            answer = min(answer, y)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aabcaba"
        j = 0
        o = 3
        self.assertEqual(s.minimumDeletions(i,j), o)

    def test_two(self):
        s = Solution()
        i = "dabdcbdcdcd"
        j = 2
        o = 2
        self.assertEqual(s.minimumDeletions(i,j), o)

    def test_three(self):
        s = Solution()
        i = "aaabaaa"
        j = 2
        o = 1
        self.assertEqual(s.minimumDeletions(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)