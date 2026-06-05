# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers num1 and num2 representing an inclusive range
    [num1, num2].

    The waviness of a number is defined as the total count of its peaks and
    valleys:
    * A digit is a peak if it is strictly greater than both of its immediate
      neighbors.
    * a digit is a valley if it is strictly less than both of its immediate
      neighbors.
    * The first and last digits of a number cannot be peaks or valleys.
    * Any number with fewer than 3 digits has a waviness of 0.

    Return the total sum of waviness for all numbers in the range [num1, num2].
    '''
    # search range is too large 1 <= num1 <= num2 <= 10^15
    def totalWaviness_brute(self, num1: int, num2: int) -> int:
        def waviness(num:int) -> int:
            if num < 100:
                return 0
            answer = 0
            num = str(num)
            for i in range(1,len(num)-1):
                if num[i-1] < num[i] > num[i+1]:
                    answer += 1
                if num[i-1] > num[i] < num[i+1]:
                    answer += 1
            return answer
        answer = 0
        for i in range(num1,num2+1):
            answer += waviness(i)
        return answer

    # based on bottom up DFS DP solution by LeetCode
    # https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/editorial/?envType=daily-question&envId=2026-06-05
    # complicated...
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(num:int) -> int:
            # early bailout when num is less than 100 (no waviness)
            if num < 100:
                return 0
            s = str(num)
            n = len(s)
            # digit 10 represents invalid state when leading zero is present
            # (prev, curr, tight, lead, count, sum)
            currStates = [(10,10,1,1,1,0)]
            # iterate positions left to right
            for pos in range(n):
                limit = int(s[pos])
                cnt = [[[[0] * 11 for _ in range(11)] for _ in range(2)] for _ in range(2)]
                sumArr = [[[[0] * 11 for _ in range(11)] for _ in range(2)] for _ in range(2)]
                for prev, curr, tight, lead, c, sVal in currStates:
                    maxDigit = limit if tight else 9
                    for digit in range(maxDigit + 1):
                        newLead = 1 if (lead and digit == 0) else 0
                        newPrev = curr
                        newCurr = 10 if newLead else digit
                        newTight = 1 if (tight and digit == maxDigit) else 0
                        add = 0
                        # calculate fluctuation when there are three significate digits
                        # (ie both prev and curr are valid and not leading zeros)
                        if not newLead and prev != 10 and curr != 10:
                            if (prev < curr and curr > digit) or (prev > curr and curr < digit):
                                add = c
                        cnt[newTight][newLead][newPrev][newCurr] += c
                        sumArr[newTight][newLead][newPrev][newCurr] += sVal + add
                # collect legal states
                newStates = []
                for tight in range(2):
                    for lead in range(2):
                        for prev in range(11):
                            for cur in range(11):
                                c = cnt[tight][lead][prev][cur]
                                if c != 0:
                                    newStates.append((prev,cur,tight,lead,c,sumArr[tight][lead][prev][cur]))
                currStates = newStates
            # sum of fluctuation values of all states
            answer = 0
            for _, _, _, _, _, sVal in currStates:
                answer += sVal
            return answer
        return solve(num2) - solve(num1-1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 120
        j = 130
        o = 3
        self.assertEqual(s.totalWaviness(i,j), o)

    def test_two(self):
        s = Solution()
        i = 198
        j = 202
        o = 3
        self.assertEqual(s.totalWaviness(i,j), o)

    def test_three(self):
        s = Solution()
        i = 4848
        j = 4848
        o = 2
        self.assertEqual(s.totalWaviness(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)