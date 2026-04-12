# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A B C D E F
    G H I J K L
    M N O P Q R
    S T U V W X
    Y Z

    There is a keyboard, with layout depicted above, in the X-Y place, where
    each English uppercase letter is located at some coordinate.

    Given the string word, return the minimum total distance to type such string
    using only two fingers.

    The distance between coordinates (x1, y1) and (x2, y2) is
    |x1 - x2| + |y1 - y2|.

    Note that the initial positions of the two fingers are considered free and
    do not count towards the total distance, additionally the two fingers do not
    have to start at the first letter or the first two letters.
    '''
    def minimumDistance(self, word: str) -> int:
        coord = dict()
        for i in range(5):
            for j in range(6):
                if i*6 + j >= 26:
                    break
                coord[i*6 + j] = (i,j)
        def dist(a:int,b:int):
            x,y = coord[a]
            i,j = coord[b]
            return abs(x - i) + abs(y - j)
        n = len(word)
        @cache
        def dp(i:int,a:int,b:int):
            if i == n:
                return 0
            answer = float('inf')
            answer = min(answer, dist(a, ord(word[i]) - 65) + dp(i+1, ord(word[i]) - 65, b))
            answer = min(answer, dist(b, ord(word[i]) - 65) + dp(i+1, a, ord(word[i]) - 65))
            return answer
        answer = float('inf')
        for i in range(26):
            for j in range(26):
                answer = min(answer, dp(0,i,j))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "CAKE"
        o = 3
        self.assertEqual(s.minimumDistance(i), o)

    def test_two(self):
        s = Solution()
        i = "HAPPY"
        o = 6
        self.assertEqual(s.minimumDistance(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)