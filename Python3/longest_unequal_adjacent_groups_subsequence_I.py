# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string array words and a binary array groups both of length n, where
    words[i] is associated with groups[i].

    Select the longest alternating subsequence from words. A subsequence of
    words is alternating if for any two consecutive strings in the sequence,
    their corresponding elements in the binary array groups differ. Essentially,
    choose strings such that adjacent elements have non-matching corresponding
    bits in the groups array.

    Formally, find the longest subsequence of an array of indices
    [0, 1, ..., n-1] denoted as [i0, i1, ... in-1], such that
    groups[ij] != groups[ij-1] for each 0 <= j < k - 1 and find the words
    corresponding to these indices.

    Return the selected subsequence. If there are multiple answers, return any
    of them.

    Note: The elements in words are distinct.
    '''
    # greedy solution because the first element is always taken
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        answer = []
        last = -1
        for i,j in enumerate(groups):
            if j != last:
                answer.append(words[i])
                last = j
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["e","a","b"]
        j = [0,0,1]
        o = ["e","b"]
        self.assertEqual(s.getLongestSubsequence(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["a","b","c","d"]
        j = [1,0,1,1]
        o = ["a","b","c"]
        self.assertEqual(s.getLongestSubsequence(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)