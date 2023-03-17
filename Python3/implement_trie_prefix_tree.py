# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Trie:
    '''
    A trie (pronounced as "try") or prefix tree is a tree data structure used to
    efficiently store and retrieve keys in a dataset of strings. There are
    various applications of this data structure, such as autocomplete and
    spellchecker.

    Implement the Trie class:
    '''
    def __init__(self):
        self.root:Dict[str, list[bool, Dict]] = [False,dict()]
        
    # inserts the string word into the trie
    def insert(self, word: str) -> None:
        c = self.root
        for w in word:
            if w not in c[1]:
                c[1][w] = [False, dict()]
            c = c[1][w]
        c[0] = True
        
    # returns true if the string word is in the trie, and false otherwise.
    def search(self, word: str) -> bool:
        c = self.root
        for w in word:
            if w not in c[1]:
                return False
            c = c[1][w]
        return c[0]
        
    # returns true if there is a previously inserted string word that has the
    # prefix prefix, and false otherwise.
    def startsWith(self, prefix: str) -> bool:
        c = self.root
        for w in prefix:
            if w not in c[1]:
                return False
            c = c[1][w]
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        t = Trie()
        t.insert("apple")
        self.assertTrue(t.search("apple"))
        self.assertFalse(t.search("app"))
        self.assertTrue(t.startsWith("app"))
        t.insert("app")
        self.assertTrue(t.search("app"))

if __name__ == '__main__':
    unittest.main(verbosity=2)