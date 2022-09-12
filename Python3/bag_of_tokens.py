# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import deque

'''
You have an initial power of power, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.
'''
class Solution:
    # based off of leetcode solution
    # https://leetcode.com/problems/bag-of-tokens/solution/
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # sort smallest to largest
        tokens.sort()
        # make double ended queue to deal with pointers
        queue = deque(tokens)
        # best answer and running score
        answer = score = 0
        # if there are tokens left and have power or score to play
        while queue and (power >= queue[0] or score):
            # keep scoring until power runs out
            while queue and power >= queue[0]:
                # score with smallest tokens
                power -= queue.popleft()
                score += 1
            # update best answer
            answer = max(answer, score)
            # increase power if possible
            if queue and score:
                power += queue.pop()
                score -= 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [100]
        j = 50
        o = 0
        self.assertEqual(s.bagOfTokensScore(i,j), o)

    def test_two(self):
        s = Solution()
        i = [100,200]
        j = 150
        o = 1
        self.assertEqual(s.bagOfTokensScore(i,j), o)

    def test_three(self):
        s = Solution()
        i = [100,200,300,400]
        j = 200
        o = 2
        self.assertEqual(s.bagOfTokensScore(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)