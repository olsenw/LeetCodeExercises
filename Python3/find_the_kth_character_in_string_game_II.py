# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob are playing a game. Initially, Alice has a string word = 'a'.

    Given a positive integer k. Also given is an integer array operations, where
    operations[i] represents the type of the ith operation.

    Now Bob will ask Alice to perform all operations in sequence:
    * If operations[i] == 0, append a copy of word to itself.
    * If operations[i] == 1, generate a new string by changing each character in
      word to its next character in the English alphabet, and append it to the
      original word.
    
    Return the value of the kth character in word after performing all the
    operations.
    '''
    # brute force, will fail because of memory issues
    def kthCharacter_simulation(self, k: int, operations: List[int]) -> str:
        m = {i:chr((ord(i) - 96) % 26 + 97) for i in "abcdefghijklmnopqrstuvwxyz"}
        word = 'a'
        for o in operations:
            if o == 0:
                word = word + word
            else:
                word = word + "".join(m[w] for w in word)
        return word[k-1]

    # based on hints
    def kthCharacter_fails(self, k: int, operations: List[int]) -> str:
        m = len(operations)
        n = 2 ** m
        j = 0
        for i in range(m-1,0,-1):
            if k > n // 2:
                k //= 2
                if operations[i]:
                    j += 1
            n //= 2
        return chr((j % 26) + 97)
    
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        m = len(operations)
        n = 2 ** m
        j = 0
        for i in range(m-1,-1,-1):
            n //= 2
            if k > n:
                k -= n
                if operations[i]:
                    j += 1
        return chr((j % 26) + 97)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = [0,0,0]
        o = "a"
        self.assertEqual(s.kthCharacter(i,j), o)

    def test_two(self):
        s = Solution()
        i = 10
        j = [0,1,0,1]
        o = "b"
        self.assertEqual(s.kthCharacter(i,j), o)

    def test_three(self):
        s = Solution()
        i = 50000
        j = [1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1]
        o = "i"
        self.assertEqual(s.kthCharacter(i,j), o)

    def test_four(self):
        s = Solution()
        i = 50000
        j = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        o = "b"
        self.assertEqual(s.kthCharacter(i,j), o)

    def test_five(self):
        s = Solution()
        i = 16
        j = [1,1,1,1]
        o = "e"
        self.assertEqual(s.kthCharacter(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)