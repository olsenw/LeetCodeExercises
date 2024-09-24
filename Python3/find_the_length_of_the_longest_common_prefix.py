# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Trie:
    def __init__(self):
        self.trie = dict()
    def add(self, s:str):
        curr = self
        for c in s:
            if c not in curr.trie:
                curr.trie[c] = Trie()
            curr = curr.trie[c]
    def partial(self, s:str):
        answer = 0
        curr = self
        for c in s:
            if c in curr.trie:
                answer += 1
                curr = curr.trie[c]
            else:
                return answer
        return answer

class Solution:
    '''
    Given two arrays with positive integers arr1 and arr2.

    A prefix of a positive number is an integer formed by one or more of its
    digits, starting from its leftmost digit. For example, 123 is a prefix of
    the integer 12345, while 234 is not.

    A common prefix of two integers a and b is an integer c, such that c is a
    prefix of both a and b. For example, 5655359 and 56553 have a common prefix
    565 while 1223 and 43456 doe not have a common prefix.

    Find the length of the longest common prefix between all pairs of integers 
    (x, y) such that x belongs to arr1 and y belongs to arr2.

    Return the length of the longest common prefix among all pairs. If no common
    prefix exists among them, return 0.
    '''
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        t = Trie()
        for a in arr1:
            t.add(str(a))
        answer = 0
        for a in arr2:
            answer = max(answer, t.partial(str(a)))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,10,100], [1000]
        o = 3
        self.assertEqual(s.longestCommonPrefix(*i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3], [4,4,4]
        o = 0
        self.assertEqual(s.longestCommonPrefix(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)