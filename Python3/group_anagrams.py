# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List

class Solution:
    '''
    Given an array of strings strs, group the anagrams together. The answer may
    be returned in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters exactly
    once.
    '''
    # O(k * n log n) time [k is number strings][n is length of string]
    def groupAnagrams_counter_sort(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for s in strs:
            ht[tuple(sorted(Counter(s).items()))].append(s)
        return list(ht.values())

    # O(k * n log n) time
    def groupAnagrams_sort(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for s in strs:
            ht[tuple(sorted(s))].append(s)
        return list(ht.values())

    # O(k * n) time
    def groupAnagrams_custom_counter(self, strs: List[str]) -> List[List[str]]:
        def counts(s):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            return tuple(count)
        ht = defaultdict(list)
        for s in strs:
            ht[counts(s)].append(s)
        return list(ht.values())

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["eat","tea","tan","ate","nat","bat"]
        o = [["bat"],["nat","tan"],["ate","eat","tea"]]
        self.assertEqual(s.groupAnagrams(i), o)

    def test_two(self):
        s = Solution()
        i = [""]
        o = [[""]]
        self.assertEqual(s.groupAnagrams(i), o)

    def test_three(self):
        s = Solution()
        i = ["a"]
        o = [["a"]]
        self.assertEqual(s.groupAnagrams(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)