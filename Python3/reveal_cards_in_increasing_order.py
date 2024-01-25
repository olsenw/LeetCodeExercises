# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array deck. There is a deck of cards where every card has a
    unique integer. The integer on the ith card is deck[i].

    The deck can be ordered in any order desired. Initially, all cards start
    face down (unrevealed) in one deck.

    Perform the following steps until all cards are revealed:
    1) Take the top card of the deck, reveal it, and take it out of the deck.
    2) If there are still cards in the deck then put the next top card of the
       deck at the bottom of the deck.
    3) If there are still unrevealed cards, go back to step 1. Otherwise stop.

    Return an ordering of the deck that would reveal the cards in increasing
    order.

    Note that the first entry in the answer is considered to be the top of the
    deck.
    '''
    def deckRevealedIncreasing_wrong(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        answer = []
        for i in range(n // 2):
            answer.append(deck[i])
            j = i + n // 2
            if j < n:
                answer.append(deck[j])
        return answer

    def deckRevealedIncreasing_wrong2(self, deck: List[int]) -> List[int]:
        m = len(deck)
        n = m // 2 + m % 2
        if m == 1:
            return deck
        deck.sort()
        r = self.deckRevealedIncreasing(deck[n:])
        answer = []
        for i in range(n):
            answer.append(deck[i])
            if i < len(r):
                answer.append(r[i])
        return answer

    def deckRevealedIncreasing_wrong3(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        answer = [deck[0]]
        for d in deck[1:]:
            answer[0],answer[-1] = answer[-1],answer[0]
            answer = [d] + answer
        return answer

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        s = deque(range(n))
        answer = []
        while len(s) > 1:
            answer.append(s.popleft())
            s.append(s.popleft())
        answer.append(s.popleft())
        deck.sort()
        m = {i:j for i,j in zip(answer,deck)}
        return [m[i] for i in range(n)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [17,13,11,2,3,5,7]
        o = [2,13,3,11,5,17,7]
        self.assertEqual(s.deckRevealedIncreasing(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1000]
        o = [1,1000]
        self.assertEqual(s.deckRevealedIncreasing(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)