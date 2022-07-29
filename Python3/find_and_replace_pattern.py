# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a list of strings words and a string pattern, return a list of
    words[i] that match pattern. The answer may be returned in any
    order.

    A word matches the pattern if there exists a permutation of letters
    p so that after replacing every letter x in the pattern with p(x),
    the desired word is obtained.

    Recall that a permutation of letters is a bijection from letters to
    letters: every letter maps to another letter, and no two letters map
    to the same letter.
    '''
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        answer = []
        for w in words:
            mapping = dict()
            used = set()
            for i, j in zip(pattern, w):
                if i not in mapping:
                    if j in used:
                        break
                    mapping[i] = j
                    used.add(j)
                elif mapping[i] != j:
                    break
            else:
                answer.append(w)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["abc","deq","mee","aqq","dkd","ccc"]
        j = "abb"
        o = ["mee","aqq"]
        self.assertEqual(s.findAndReplacePattern(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["a","b","c"]
        j = "a"
        o = ["a","b","c"]
        self.assertEqual(s.findAndReplacePattern(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)