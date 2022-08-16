# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import Counter

class Solution:
    '''
    Given a string s and an array of strings words of the same length.
    Return all starting indices of substrings(s) in s that is a
    concatenation of each word in words exactly once, in any order, and
    without any intervening characters.

    Answer may be returned in any order.
    '''
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        answer = []
        wlen = len(words[0])
        window = wlen * len(words)
        possible = Counter()
        target = Counter()
        for w in words:
            for c in w:
                possible[c] += 1
            target[w] += 1
        actual = Counter(s[0:window])
        if possible == actual:
            check = Counter()
            for j in range(len(words)):
                # check[s[i + j * wlen:i + j * wlen + wlen]] += 1
                # print(j * wlen, s[j * wlen:j * wlen + wlen])
                check[s[j * wlen:j * wlen + wlen]] += 1
            # print("check", check)
            if target == check:
                answer.append(0)
        #print(possible, target, actual)
        for i in range(window, len(s)):
            # print(i-window, s[i-window], i, s[i])
            actual[s[i - window]] -= 1
            actual[s[i]] += 1
            #print(actual)
            if possible == actual:
                check = Counter()
                f = i - window + 1
                for j in range(len(words)):
                    # check[s[i + j * wlen:i + j * wlen + wlen]] += 1
                    # print(f + j * wlen, s[f + j * wlen:f + j * wlen + wlen])
                    check[s[f + j * wlen:f + j * wlen + wlen]] += 1
                # print("check", check)
                if target == check:
                    answer.append(f)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "barfoothefoobarman"
        j = ["foo","bar"]
        o = [0,9]
        self.assertEqual(s.findSubstring(i,j), o)

    def test_two(self):
        s = Solution()
        i = "wordgoodgoodgoodbestword"
        j = ["word","good","best","word"]
        o = []
        self.assertEqual(s.findSubstring(i,j), o)

    def test_three(self):
        s = Solution()
        i = "barfoofoobarthefoobarman"
        j = ["bar","foo","the"]
        o = [6,9,12]
        self.assertEqual(s.findSubstring(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)