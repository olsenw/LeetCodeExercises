# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    # (48/53) Memory limit exceeded
    def maxNumberOfFamilies_memory(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = {i:0 for i in range(1,n+1)}
        for i,j in reservedSeats:
            seats[i] |= 1 << j
        answer = 0
        left = (1<<2) | (1<<3) | (1<<4) | (1<<5)
        right = (1<<6) | (1<<7) | (1<<8) | (1<<9)
        both = left | right
        mid = (1<<4) | (1<<5) | (1<<6) | (1<<7)
        for i in range(1,n+1):
            if not (seats[i] & both):
                answer += 2
            elif not (seats[i] & left):
                answer += 1
            elif not (seats[i] & right):
                answer += 1
            elif not (seats[i] & mid):
                answer += 1
        return answer

    # not sure why fails
    def maxNumberOfFamilies_fails(self, n: int, reservedSeats: List[List[int]]) -> int:
        answer = 0
        left = (1<<2) | (1<<3) | (1<<4) | (1<<5)
        right = (1<<6) | (1<<7) | (1<<8) | (1<<9)
        both = left | right
        mid = (1<<4) | (1<<5) | (1<<6) | (1<<7)
        reservedSeats.sort()
        row = reservedSeats[0][0]
        seats = 0
        for i,j in reservedSeats:
            if row != i:
                answer += 2 * (i - row - 1)
                if not (seats & both):
                    answer += 2
                elif not (seats & left):
                    answer += 1
                elif not (seats & right):
                    answer += 1
                elif not (seats & mid):
                    answer += 1
                seats = 0
                row = i
            seats |= 1 << j
        # answer += 2 * (i - row - 1)
        if not (seats & both):
            answer += 2
        elif not (seats & left):
            answer += 1
        elif not (seats & right):
            answer += 1
        elif not (seats & mid):
            answer += 1
        if reservedSeats[-1][0] < n:
            answer += 2 * (n - row)
            # answer += 2 * (n - row - 1)
        return answer

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        answer = 0
        left = (1<<2) | (1<<3) | (1<<4) | (1<<5)
        right = (1<<6) | (1<<7) | (1<<8) | (1<<9)
        both = left | right
        mid = (1<<4) | (1<<5) | (1<<6) | (1<<7)
        seats = dict()
        for i,j in reservedSeats:
            if i not in seats:
                seats[i] = 1 << j
            else:
                seats[i] |= 1 << j
        # for i in range(1,n+1):
        #     if i not in seats:
        #         answer += 2
        #         continue
        for i in seats:
            n -= 1
            if not (seats[i] & both):
                answer += 2
            elif not (seats[i] & left):
                answer += 1
            elif not (seats[i] & right):
                answer += 1
            elif not (seats[i] & mid):
                answer += 1
        return answer + 2 * n

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
        o = 4
        self.assertEqual(s.maxNumberOfFamilies(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [[2,1],[1,8],[2,6]]
        o = 2
        self.assertEqual(s.maxNumberOfFamilies(i,j), o)

    def test_three(self):
        s = Solution()
        i = 4
        j = [[4,3],[1,4],[4,6],[1,7]]
        o = 4
        self.assertEqual(s.maxNumberOfFamilies(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)