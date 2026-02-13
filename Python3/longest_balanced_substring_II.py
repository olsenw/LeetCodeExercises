# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting only of the characters 'a', 'b', and 'c'.

    A substring of s is called balanced if all distinct characters in the
    substring appear the same number of times.

    Return the length of the longest balanced substring of s.
    '''
    # based on hints
    def longestBalanced(self, s: str) -> int:
        answer = 0
        # hint 2) longest continuous string single character
        def single(letter: str) -> int:
            answer = 0
            count = 0
            for i in range(len(s)):
                if s[i] == letter:
                    count += 1
                else:
                    answer = max(answer, count)
                    count = 0
            return max(answer, count)
        answer = max(answer, single('a'))
        answer = max(answer, single('b'))
        answer = max(answer, single('c'))
        # Hint 3) longest equal double pair
        def double(x:str, y:str, bad:str) -> int:
            answer = 0
            h = {0:-1}
            count = 0
            for i in range(len(s)):
                count += s[i] == x
                count -= s[i] == y
                if s[i] == bad:
                    h = {0:i}
                    count = 0
                elif count in h:
                    answer = max(answer, i - h[count])
                else:
                    h[count] = i
            return answer
        answer = max(answer, double('a','b','c'))
        answer = max(answer, double('a','c','b'))
        answer = max(answer, double('b','c','a'))
        # Hint 4) hash prefix count pairs
        def triple() -> int:
            answer = 0
            # hash pair (count_b - count_a, count_c - count_a) -> earliest index
            # if find again that is a valid range
            h = {(0,0):-1}
            a,b,c = 0,0,0
            for i in range(len(s)):
                a += 'a' == s[i]
                b += 'b' == s[i]
                c += 'c' == s[i]
                pair = (b-a, c-a)
                if pair in h:
                    answer = max(answer, i - h[pair])
                else:
                    h[pair] = i
            return answer
        answer = max(answer, triple())
        return answer

class UnitTesting(unittest.TestCase):
    # def test_one(self):
    #     s = Solution()
    #     i = "abbac"
    #     o = 4
    #     self.assertEqual(s.longestBalanced(i), o)

    # def test_two(self):
    #     s = Solution()
    #     i = "aabcc"
    #     o = 3
    #     self.assertEqual(s.longestBalanced(i), o)

    # def test_three(self):
    #     s = Solution()
    #     i = "aba"
    #     o = 2
    #     self.assertEqual(s.longestBalanced(i), o)

    # def test_four(self):
    #     s = Solution()
    #     i = "aabbcc"
    #     o = 6
    #     self.assertEqual(s.longestBalanced(i), o)

    def test_five(self):
        s = Solution()
        i = "bacbbc"
        o = 4
        self.assertEqual(s.longestBalanced(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)