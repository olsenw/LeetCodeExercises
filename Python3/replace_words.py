# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    In English, there is a concept call root, which can be followed by some
    other word to form another longer word called a successor. For example, when
    the root "help" is followed by the successor word "ful", forming the word
    "helpful".

    Given a dictionary consisting of many roots and a sentence consisting of
    words separated by spaces, replace all the successors in the sentence with
    the root forming it. If a successor can be replaced by more than one root,
    replace the root that has the shortest length.

    Return the sentence after the replacement.
    '''
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = [False,dict()]
        for d in set(dictionary):
            curr = trie
            for c in d:
                if c not in curr[1]:
                    curr[1][c] = [False, dict()]
                curr = curr[1][c]
            curr[0] = True
        def rep(w:str) -> str:
            curr = trie
            for i,c in enumerate(w):
                if curr[0] == True:
                    return w[:i]
                if c not in curr[1]:
                    break
                curr = curr[1][c]
            return w
        return " ".join(rep(i) for i in sentence.split())

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["cat","bat","rat"]
        j = "the cattle was rattled by the battery"
        o = "the cat was rat by the bat"
        self.assertEqual(s.replaceWords(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["a","b","c"]
        j = "aadsfasf absbs bbab cadsfafs"
        o = "a a b c"
        self.assertEqual(s.replaceWords(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)