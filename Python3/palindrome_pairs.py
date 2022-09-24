# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a 0-indexed array of unique strings words.
    
    A palindrome pair is a pair of integers (i,j) such that:
    * 0 <= i,j < word.length
    * i != j
    * words[i] + words[j] (the concatenation of the two strings) is a palindrome
      string.
    
    Return an array of all the palindrome pairs of words.
    '''
    # based on discussion post by ryangrayson
    # https://leetcode.com/problems/palindrome-pairs/discuss/2585442/Intuitive-Python3-or-HashMap-or-95-Time-and-Space-or-O(N*W2)
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # mapping reversed(string) -> index(string)
        backward = {}
        for i, word in enumerate(words):
            backward[word[::-1]] = i
        # list of all the pairs
        res = []

        # for each word check is palindrome is possible
        for i, word in enumerate(words):
            # treat word[i] as suffix is there a prefix in  backwards
            if word in backward and backward[word] != i:
                res.append([i, backward[word]])
            # special case where there is empty string allowing a palindrome
            # to generate pair
            if word != "" and "" in backward and word == word[::-1]:
                res.append([i, backward[""]])
                res.append([backward[""], i])
            # test all substrings to see if they exist in backwards
            for j in range(len(word)):
                if word[j:] in backward and word[:j] == word[j-1::-1]:
                    res.append([backward[word[j:]], i])
                if word[:j] in backward and word[j:] == word[:j-1:-1]:
                    res.append([i, backward[word[:j]]])
                    
        return res

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["abcd","dcba","lls","s","sssll"]
        o = [[0,1],[1,0],[3,2],[2,4]]
        self.assertEqual(s.problem_name(i), o)

    def test_two(self):
        s = Solution()
        i = ["bat","tab","cat"]
        o = [[0,1],[1,0]]
        self.assertEqual(s.problem_name(i), o)

    def test_three(self):
        s = Solution()
        i = ["a",""]
        o = [[0,1],[1,0]]
        self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)