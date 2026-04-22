# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two string arrays, queries and dictionary. All words in each array
    comprise of lowercase English letters and are the same length.

    In one edit, it is possible to take a word from queries, and change any
    letter in the word to any other letter. Find all words from queries that,
    after a maximum of two edits, equal some word from dictionary.

    Return a list of all words from queries, that match with some word from
    dictionary after a maximum of two edits. Return the words in the same order
    as they appear in queries.
    '''
    # brute force (the dp tracking may be an over optimization for small constraints)
    # early break out in checking helps a lot
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def check_slow(q,w):
            return sum(i != j for i,j in zip(q,w))
        def check(q,w):
            d = 0
            for i in range(len(q)):
                if q[i] != w[i]:
                    d += 1
                if d > 2:
                    break
            return d
        answer = []
        dp = dict()
        for q in queries:
            if q in dp:
                if dp[q] == True:
                    answer.append(q)
                continue
            for w in set(dictionary):
                if check(q,w) <= 2:
                    answer.append(q)
                    dp[q] = True
                    break
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["word","note","ants","wood"]
        j = ["wood","joke","moat"]
        o = ["word","note","wood"]
        self.assertEqual(s.twoEditWords(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["yes"]
        j = ["not"]
        o = []
        self.assertEqual(s.twoEditWords(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)