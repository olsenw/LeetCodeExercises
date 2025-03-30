# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums of n positive integers and an integer k.

    Initially, start with a score of 1. Maximize the score by applying the
    following operation at most k times:
    * Choose any non-empty subarray nums[l, ..., r] that has not been chosen
      previously.
    * Choose an element x of nums[l, ..., r] with the hightest prime score. If
      multiple such elements exist, choose the one with the smallest index.
    * Multiply the score by x.

    Here, nums[l, ..., r] denotes the subarray of nums starting at index l and
    ending at the index r, both ends inclusive.

    The prime score of an integer x is equal to the number of distinct prime
    factors of x. For example, the prime score of 300 is 3 since
    300 = 2 * 2 * 3 * 5 * 5.

    Return the maximum possible score after applying at most k operations.
    '''
    # is possible to reuse elements by using larger subarray that contains it
    def maximumScore_fails(self, nums: List[int], k: int) -> int:
        # https://www.geeksforgeeks.org/python-program-for-efficient-program-to-print-all-prime-factors-of-a-given-number/
        def primScore(n:int) -> int:
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n))+1, 2):
                while n % i == 0:
                    factors.add(i)
                    n //= i
            if n > 2:
                factors.add(n)
            return len(factors)
        answer = 1
        heap = sorted(((primScore(n),n) for n in nums), reverse=True)
        pass
        for i,j in heap[:min(k, len(heap))]:
            answer *= j
        return answer % (10**5 + 7)

    # spend too much time widening the search at desired possible index
    def maximumScore_tle(self, nums: List[int], k: int) -> int:
        # https://www.geeksforgeeks.org/python-program-for-efficient-program-to-print-all-prime-factors-of-a-given-number/
        def primScore(n:int) -> int:
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n))+1, 2):
                while n % i == 0:
                    factors.add(i)
                    n //= i
            if n > 2:
                factors.add(n)
            return len(factors)
        pScore = [primScore(n) for n in nums]
        order = sorted(range(len(nums)), key=lambda x:(-nums[x],pScore[x],x))
        orderIndex = 0
        i,j = order[orderIndex],order[orderIndex]
        answer = nums[order[orderIndex]]
        for _ in range(1,k):
            pass
            if i > 0 and pScore[i-1] < pScore[order[orderIndex]]:
                i -= 1
            elif j < len(nums) - 1 and pScore[j+1] <= pScore[order[orderIndex]]:
                i = order[orderIndex]
                j += 1
            else:
                orderIndex += 1
                i,j = order[orderIndex],order[orderIndex]
            answer *= nums[order[orderIndex]]
            pass
        return answer % (10**9 + 7)

    # based off of LeetCode solution
    # https://leetcode.com/problems/apply-operations-to-maximize-score/editorial/?envType=daily-question&envId=2025-03-29
    def maximumScore_leet(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        primeScores = [0] * n
        for i in range(n):
            num = nums[i]
            # try all factors in range [2, sqrt(num)]
            for factor in range(2, int(math.sqrt(num))+1):
                if num % factor == 0:
                    primeScores[i] += 1
                    while num % factor == 0:
                        num //= factor
            # num must be prime
            if num >= 2:
                primeScores[i] += 1
        nextDominant = [n] * n
        lastDominant = [-1] * n
        # decreasing monotonic stack
        stack = []
        for i in range(n):
            while stack and primeScores[stack[-1]] < primeScores[i]:
                nextDominant[stack.pop()] = i
            if stack:
                lastDominant[i] = stack[-1]
            stack.append(i)
        subarrays = [(nextDominant[i] - i) * (i - lastDominant[i]) for i in range(n)]
        queue = [(-j,i) for i,j in enumerate(nums)]
        heapq.heapify(queue)
        def modularExponentiation(base, exponent):
            answer = 1
            while exponent > 0:
                if exponent % 2:
                    answer = (answer * base) % mod
                base = (base * base) % mod
                exponent //= 2
            return answer
        answer = 1
        while k > 0:
            num, i = heapq.heappop(queue)
            num *= -1
            operations = min(k, subarrays[i])
            answer = (answer * modularExponentiation(num, operations)) % mod
            k -= operations
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [8,3,9,3,8]
        j = 2
        o = 81
        self.assertEqual(s.maximumScore(i,j), o)

    def test_two(self):
        s = Solution()
        i = [19,12,14,6,10,18]
        j = 3
        o = 4788
        self.assertEqual(s.maximumScore(i,j), o)

    def test_three(self):
        s = Solution()
        i = [19,12,12,12,2,6]
        j = 3
        o = 2736
        self.assertEqual(s.maximumScore(i,j), o)

    def test_four(self):
        s = Solution()
        i = [3289,2832,14858,22011]
        j = 6
        o = 256720975
        self.assertEqual(s.maximumScore(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)