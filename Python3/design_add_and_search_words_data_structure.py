# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from functools import lru_cache
'''
Design a data structure that supports adding new words and finding if a
string matches any previously added string.

Implement the WordDictionary class:
* WordDictionary()   Initializes the object.
* void addWord(word) Adds word to the data structure, it can be matched
                     later.
* bool search(word)  Returns true if there is any string in the data 
                     structure that matches word or false otherwise. 
                     word may conntain dots '.' where dots can be 
                     matched with any letter.
'''
class WordDictionary:
    # make use of a trie data structure
    # an alternative is to add a character (nod possible in word like 
    # '$') and check if that is in the dictionary at desired level
    def __init__(self):
        # the dictionary of children and if this level is a word
        self.trie = [dict(), False]

    def addWord(self, word: str) -> None:
        t = self.trie
        for s in word:
            d = t[0]
            if s not in d:
                d[s] = [dict(), False]
            t = d[s]
        t[1] = True

    def search(self, word: str) -> bool:
        # allows for recursive search of subtries
        def searchTrie(word:str, start=0, trie=self.trie) -> bool:
            for s in range(start,len(word)):
                d = trie[0]
                if word[s] == '.':
                    for t in d:
                        if searchTrie(word, s+1, d[t]):
                            return True
                    # no matching subtrie found
                    return False
                elif word[s] in d:
                    trie = d[word[s]]
                else:
                    return False
            return trie[1]
        return searchTrie(word)

# really slick alterative solution by taeho911
# probably takes advantage of limited problem constraints/tests
# https://leetcode.com/problems/design-add-and-search-words-data-structure/discuss/1725003/Python-length-first-data-structure
# if has a dictionary of sets, where given set are all the words of a
# given length. only trick is handling search with dots, in which case 
# just iterate over all words in that set and check validity.

class UnitTesting(unittest.TestCase):
    def test_single(self):
        s = WordDictionary()
        s.addWord("cat")
        self.assertEqual(s.search("cat"), True)

    def test_aa(self):
        s = WordDictionary()
        s.addWord("a")
        s.addWord("a")
        self.assertEqual(s.search("."), True)
        self.assertEqual(s.search("a"), True)
        self.assertEqual(s.search("aa"), False)
        self.assertEqual(s.search("a"), True)
        self.assertEqual(s.search(".a"), False)
        self.assertEqual(s.search("a."), False)

    def test_all(self):
        s = WordDictionary()
        # add words
        s.addWord("banana")
        s.addWord("cat")
        s.addWord("mississippi")
        # check if words added
        self.assertEqual(s.search("banana"), True)
        self.assertEqual(s.search("cat"), True)
        self.assertEqual(s.search("mississippi"), True)
        # check that unadded words are not present
        self.assertEqual(s.search("mad"), False)
        self.assertEqual(s.search("word"), False)
        # check dot search works
        self.assertEqual(s.search("ca."), True)
        self.assertEqual(s.search("..."), True)
        # check dot search should fail
        self.assertEqual(s.search("."), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)