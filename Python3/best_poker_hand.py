# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array ranks and a character array suits. There are 5 cards
    where the ith card has a rank of ranks[i] and a suit of suits[i].

    The following are the types of poker hands that can be made ranked best to
    worst:
    1) "Flush": Five cards of the same suit.
    2) "Three of a Kind": Three cards of the same rank.
    3) "Pair": Two cards of the same rank.
    4) "High Card": Any single card.

    Return a string representing the best type of poker hand that can be made
    with the given cards.

    Note that the return values are case-sensitive.
    '''
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if all(suits[0] == s for s in suits):
            return "Flush"
        c = Counter(ranks)
        if any(c[i] >= 3 for i in c):
            return "Three of a Kind"
        if any(c[i] == 2 for i in c):
            return "Pair"
        return "High Card"

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [13,2,3,1,9], ["a","a","a","a","a"]
        o = "Flush"
        self.assertEqual(s.bestHand(*i), o)

    def test_two(self):
        s = Solution()
        i = [4,4,2,4,4], ["d","a","a","b","c"]
        o = "Three of a Kind"
        self.assertEqual(s.bestHand(*i), o)

    def test_three(self):
        s = Solution()
        i = [10,10,2,12,9], ["a","b","c","a","d"]
        o = "Pair"
        self.assertEqual(s.bestHand(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)