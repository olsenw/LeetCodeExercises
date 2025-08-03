# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Fruits are available at some positions on an infinite x-axis. Given a 2D 
    integer array fruits where fruits[i] = [positioni, amounti] depicts amount,
    fruits at the position positioni. fruits is already sorted by positioni in
    ascending order, and each positioni is unique.

    Also given integer startPos and an integer k. Initially, a person starts at
    the position startPos. From any position the person can walk to the left or
    right. It takes one step to move one unit on the x-axis, and it is only
    possible to walk at most k steps in total. For every position the person
    reaches, they harvest all the fruits at that position, and the fruits will
    disappear from that position.

    Return the maximum total number of fruits that can be harvested.
    '''
    def maxTotalFruits_fails(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        answer = 0
        values = [0]
        for i in range(len(fruits)):
            values.append(values[-1] + fruits[i][1])
        startIndex = bisect.bisect(fruits, [startPos, 10**5])
        fruitIndex = bisect.bisect(fruits, [startPos - k, 0])
        for i in range(fruitIndex, startIndex):
            distance = fruits[i][0] + (k - (startPos - fruits[i][0]))
            distance = max(distance, startPos)
            j = bisect.bisect(fruits, [distance, 10**5], i)
            # j = min(j, len(values) - 1)
            answer = max(answer, values[j] - values[i])
        j = bisect.bisect(fruits, [startPos + k, 10**5], startIndex)
        # j = min(j, len(values) - 1)
        answer = max(answer, values[j] - values[startIndex])
        return answer

    # based on hint to do two patterns
    def maxTotalFruits_fails2(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        answer = 0
        values = [0]
        for i in range(len(fruits)):
            values.append(values[-1] + fruits[i][1])
        # go left then go right
        startIndex = bisect.bisect(fruits, [startPos, 10**5])
        fruitIndex = bisect.bisect(fruits, [startPos - k, 0])
        for i in range(fruitIndex, startIndex):
            distance = fruits[i][0] + (k - (startPos - fruits[i][0]))
            distance = max(distance, startPos)
            j = bisect.bisect(fruits, [distance, 10**5], i)
            # j = min(j, len(values) - 1)
            answer = max(answer, values[j] - values[i])
        # go right then go left
        fruitIndex = bisect.bisect(fruits, [startPos + k, 10**5])
        for i in range(startIndex, fruitIndex):
            distance = fruits[i][0] - (k - (fruits[i][0] - startPos))
            distance = min(distance, startPos)
            j = bisect.bisect(fruits, [distance,0], 0, i)
            answer = max(answer, values[i] - values[j])
        return answer

    # based on Leetcode editorial
    # https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/editorial/?envType=daily-question&envId=2025-08-03
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        answer = 0
        n = len(fruits)
        s = [0]
        pos = []
        for i in range(n):
            s.append(s[-1] + fruits[i][1])
            pos.append(fruits[i][0])
        # move up to half k steps one direction
        for i in range(k // 2 + 1):
            # move left then right
            j = k - 2 * i
            left = startPos - i
            right = startPos + j
            start = bisect.bisect_left(pos, left)
            end = bisect.bisect(pos, right)
            answer = max(answer, s[end] - s[start])
            # move right then left
            j = k - 2 * i
            left = startPos - j
            right = startPos + i
            start = bisect.bisect_left(pos, left)
            end = bisect.bisect(pos, right)
            answer = max(answer, s[end] - s[start])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2,8],[6,3],[8,6]]
        j = 5
        k = 4
        o = 9
        self.assertEqual(s.maxTotalFruits(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
        j = 5
        k = 4
        o = 14
        self.assertEqual(s.maxTotalFruits(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [[0,3],[6,4],[8,5]]
        j = 3
        k = 2
        o = 0
        self.assertEqual(s.maxTotalFruits(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = [[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]]
        #                                                                   ^^^
        j = 21
        k = 30
        o = 71
        self.assertEqual(s.maxTotalFruits(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)