# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a wordList, implement a spellchecker that converts a query word into a
    correct word.

    For a given query word, the spell checker handles two categories of spelling
    mistakes:
    * Capitalization: If the query matches a word in the word list
      (case-insensitive), then the query word is returned with the same case as
      the case in the word list.
    * Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of
      the query word with any vowel individually, it matches a word in the word
      list (case-insensitive), then the query word is returned with the same
      as the match in the word list.
    
    In addition, the spell checker operates under the following precedence
    rules:
    * When the query exactly matches a word in the word list (case-sensitive),
      return the same word back.
    * When the query matches a word up to capitalization, return the first such
      match in the word list.
    * When the query matches a word up to vowel errors, return the first such
      match in the word list.
    * If the query has no matches in the word list return the empty string.

    Given some queries, return a list of words answer, where answer[i] is the
    correct word for query = queries[i].
    '''
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def replace(word: str):
            for c in 'aeiou':
                word = word.replace(c, '*')
            return word
        exact = set()
        capitalization = dict()
        vowel = dict()
        for w in wordlist:
            exact.add(w)
            l = w.lower()
            if l not in capitalization:
                capitalization[l] = w
            l = replace(l)
            if l not in vowel:
                vowel[l] = w
        def test(word:str):
            if word in exact:
                return word
            w = word.lower()
            if w in capitalization:
                return capitalization[w]
            w = replace(w)
            if w in vowel:
                return vowel[w]
            return ""
        return [test(w) for w in queries]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["KiTe","kite","hare","Hare"]
        j = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
        o = ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
        self.assertEqual(s.spellchecker(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["yellow"]
        j = ["YellOw"]
        o = ["yellow"]
        self.assertEqual(s.spellchecker(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)