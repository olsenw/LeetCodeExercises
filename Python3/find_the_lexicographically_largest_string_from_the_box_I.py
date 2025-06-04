# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string word and an integer numFriends.

    Alice is organizing a game for her numFriends friends. There are multiple
    rounds in the game, where in each round:
    * word is split into numFriends non-empty strings, such that no previous
      round has had the exact same split.
    * All the split words are put into a box.

    Find the lexicographically largest string from the box after all the rounds
    are finished.
    '''
    # wrong note that length does not equal lexicographically largest
    def answerString_wrong(self, word: str, numFriends: int) -> str:
        n = len(word)
        l = n - (numFriends - 1)
        # answer = ""
        # for i in range(n-l):
        #     answer = max(answer, word[i:i+l])
        # return answer
        return max(word[i:i+l] for i in range(n - l))

    # need to evaluate all largest letter starts
    def answerString_fails(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1:
            return word
        l = n - numFriends + 1
        c = max(word)
        i = word.find(c)
        return word[i:i+l]

    # time limit exceeded 776 /  785
    def answerString_tle(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        l = n - numFriends + 1
        answer = ""
        for i in range(n):
            for j in range(i+1,i+l+1):
                answer = max(answer, word[i:j])
        return answer

    # passes (barely) O(n^2)
    def answerString_slow(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        l = n - numFriends + 1
        c = max(word)
        answer = c
        for i in range(n):
            if word[i] != c:
                continue
            for j in range(i+1,i+l+1):
                answer = max(answer, word[i:j])
        return answer

    # based on LeetCode Two Pointers editorial
    # https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/editorial/?envType=daily-question&envId=2025-06-04
    # O(n)
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        i,j,n = 0,1,len(word)
        while j < n:
            k = 0
            while j + k < n and word[i + k] == word[j + k]:
                k += 1
            if j + k < n and word[i + k] < word[j + k]:
                i,j = j, max(j + 1, i + k +1)
            else:
                j = j + k + 1
        last = word[i:]
        m = len(last)
        return last[: min(m, n - numFriends + 1)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "dbca"
        j = 2
        o = "dbc"
        self.assertEqual(s.answerString(i,j), o)

    def test_two(self):
        s = Solution()
        i = "gggg"
        j = 4
        o = "g"
        self.assertEqual(s.answerString(i,j), o)

    def test_three(self):
        s = Solution()
        i = "aann"
        j = 2
        o = "nn"
        self.assertEqual(s.answerString(i,j), o)

    def test_four(self):
        s = Solution()
        i = "gh"
        j = 1
        o = "gh"
        self.assertEqual(s.answerString(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)