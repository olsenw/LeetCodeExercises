# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings word1 and word2, return the minimum number of operations
    required to convert word1 to word2.

    The following three operations are permitted:
    * Insert a character
    * Delete a character
    * Replace a character
    '''
    def minDistance_wrong(self, word1: str, word2: str) -> int:
        # check for trivial cases
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        @cache
        def edit(word:str) -> int:
            # replace characters (how many characters are different)
            # too naive... there are cases where an insert/delete are better
            if len(word) == len(word2):
                replaces = 0
                for i in range(len(word)):
                    if word[i] != word2[i]:
                        replaces += 1
                return replaces
            # delete a character
            elif len(word) > len(word2):
                deletes = 500
                for i in range(len(word)):
                    deletes = min(deletes, 1 + edit(word[:i] + word[i+1:]))
                return deletes
            # insert a character
            else:
                inserts = 500
                return inserts
        return edit(word1)

    # wrong
    # infinite recursion due to how the cache works
    # probably logic issues as well
    def minDistance_wrong(self, word1: str, word2: str) -> int:
        # check for trivial cases
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        # all of the characters present in word2 (no point inserting any others)
        characters = set(word2)

        def delete(word:str) -> int:
            a:int = 500
            # for i in range(len(word)):
            for i in range(len(word)-1,-1,-1):
                a = min(a, 1 + edit(word[:i] + word[i+1:]))
            return a

        def insert(word:str) -> int:
            a:int = 500
            for i in range(len(word) + 1):
                for j in characters:
                    a = min(a, 1 + edit(word[:i] + j + word[i:]))
            return a

        @cache
        def edit(word:str) -> int:
            # replace a character
            if len(word) == len(word2):
                # base case
                if word == word2:
                    return 0
                # check for a delete/insert case
                a = delete(word)
                # replace mismatched
                for i in range(len(word)):
                    if word[i] != word2[i]:
                        a = min(a, 1 + edit(word[:i] + word2[i] + word[i+1:]))
                return a
            # word is too short, insert a character
            elif len(word) < len(word2):
                return insert(word)
            # word is too long, delete a character
            else:
                return delete(word)
            
        return edit(word1)

    # based off of Recursion LeetCode solution
    # https://leetcode.com/problems/edit-distance/editorial/
    # O(3^max(len(w1), len(w2))) time for trying each operation at each character
    # also nails the recursion depth limit
    def minDistance_leetcode_recursion(self, word1: str, word2: str) -> int:
        # i is index in word1, j is index in word2
        def edit(i:int, j:int) -> int:
            # base case
            if i == 0:
                return j
            # base case
            if j == 0:
                return i
            # no change needed
            if word1[i - 1] == word2[j - 1]:
                return edit(i - 1, j - 1)
            # try each of the operations
            else:
                insert = edit(i, j - 1)
                delete = edit(i - 1, j)
                replace = edit(i - 1, j -1)
                return 1 + min(insert, delete, replace)
        return edit(len(word1), len(word2))

    # based off of Top Down DP LeetCode solution
    # https://leetcode.com/problems/edit-distance/editorial/
    # O(len(w1) * len(w2)) time
    # hits recursion limit on my computer, passes online
    def minDistance(self, word1: str, word2: str) -> int:
        # dp = [[None] * len(word2) for _ in range(len(word1))]
        # i is index in word1, j is index in word2
        @cache
        def edit(i:int, j:int) -> int:
            # base case
            if i == 0:
                return j
            # base case
            if j == 0:
                return i
            # no change needed
            if word1[i - 1] == word2[j - 1]:
                return edit(i - 1, j - 1)
            # try each of the operations
            else:
                insert = edit(i, j - 1)
                delete = edit(i - 1, j)
                replace = edit(i - 1, j -1)
                return 1 + min(insert, delete, replace)
        return edit(len(word1), len(word2))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "horse"
        j = "ros"
        o = 3
        self.assertEqual(s.minDistance(i,j), o)

    def test_two(self):
        s = Solution()
        i = "intention"
        #    *****
        j = "execution"
        o = 5
        self.assertEqual(s.minDistance(i,j), o)

    def test_three(self):
        s = Solution()
        i = "ros"
        j = "horse"
        o = 3
        self.assertEqual(s.minDistance(i,j), o)

    def test_four(self):
        s = Solution()
        i = "a" * 500
        j = "b" * 500
        o = 500
        self.assertEqual(s.minDistance(i,j), o)

    def test_five(self):
        s = Solution()
        i = "patterns"
        j = "pasttern"
        o = 2
        self.assertEqual(s.minDistance(i,j), o)

    def test_six(self):
        s = Solution()
        i = "patternsaaa"
        j = "pasttern"
        o = 5
        self.assertEqual(s.minDistance(i,j), o)

    def test_seven(self):
        s = Solution()
        i = "aa"
        j = "bc"
        o = 2
        self.assertEqual(s.minDistance(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)