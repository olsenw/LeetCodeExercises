# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string paragraph and a string array of the banned words banned,
    return the most frequent word that is not banned. It is guaranteed there is
    at least one word that is not banned, and that the answer is unique.

    The words in paragraph are case-insensitive and the answer should be
    returned in lowercase.

    Note that the words can not contain punctuation symbols.
    '''
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # c = Counter(paragraph.strip("!?',;.").lower().split()).most_common()
        paragraph = paragraph.translate(str.maketrans("!?,;.","     ","'")).lower().split()
        c = Counter(paragraph)
        pass
        for i,_ in c.most_common():
            if i not in banned:
                return i
        return ""

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "Bob hit a ball, the hit BALL flew far after it was hit."
        j = ["hit"]
        o = "ball"
        self.assertEqual(s.mostCommonWord(i,j), o)

    def test_two(self):
        s = Solution()
        i = "a."
        j = []
        o = "a"
        self.assertEqual(s.mostCommonWord(i,j), o)

    def test_three(self):
        s = Solution()
        i = "a, a, a, a, b,b,b,c, c"
        j = ["a"]
        o = "b"
        self.assertEqual(s.mostCommonWord(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)