# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string num which represents a positive integer, and an integer t.

    A number is called zero-free if none of its digits are 0.

    Return a string representing the smallest zero-free number greater than or
    equal to num such that the product of its digits is divisible by t. If no
    such number exists, return "-1".
    '''
    # hints, incomplete
    def smallestNumber_unfinished(self, num: str, t: int) -> str:
        # based on O(sqrt(n)) prime factorization from geeks for geeks
        # https://www.geeksforgeeks.org/dsa/print-all-prime-factors-of-a-given-number/
        def primeFactors(num:int) -> Optional[list[int]]:
            prime = [0] * 10
            # get number of 2's that divide num
            while num % 2 == 0:
                prime[2] += 1
                num //= 2
            # num is now odd (can skip by powers of 2)
            for i in range(3, int(math.sqrt(num) + 1), 2):
                while num % i == 0:
                    if i >= 10:
                        return None
                    prime[i] += 1
                    num //= i
            # possible num is a prime number greater than 2
            if num > 2:
                if num >= 10:
                    return None
                prime[num] += 1
            return prime
        # based on hint 1
        # t must only have prime factors [2,3,5,7]
        # otherwise product of digits of num is impossible
        primes = primeFactors(t)
        if primes is None:
            return "-1"
        # based on hint 2
        # find smallest suffix that needs to change
        def backtrack(s:str,m:int) -> str:
            i = len(s)-1
        return None

    # based on LeetCode editorial
    # https://leetcode.com/problems/smallest-divisible-digit-product-ii/editorial/?envType=daily-question&envId=2026-08-07
    def smallestNumber(self, num: str, t: int) -> str:
        # verify prime factorization consists only of [2,3,5,7]
        temp = t
        for i in range(2,10):
            while temp % i == 0:
                temp //= i
        if temp > 1:
            return "-1"
        # greedy construct answer
        n = len(num)
        # tracks the remainder of t after processing nums digits
        remainder = [0] * (n+1)
        remainder[0] = t
        pos = n - 1
        numl = list(num)
        for i in range(n):
            if numl[i] == "0":
                pos = i
                break
            remainder[i+1] = remainder[i] // math.gcd(remainder[i], int(numl[i]))
        # num is already divisible by t
        if remainder[n] == 1:
            return num
        # convert zeros into valid digits
        for i in range(pos,-1,-1):
            # try replacing 0 with 1->9
            while True:
                numl[i] = chr(ord(numl[i]) + 1)
                # cannot exceed a digit 9
                if numl[i] > '9':
                    break
                temp = remainder[i] // math.gcd(remainder[i], int(numl[i]))
                k = 9
                for j in range(n-1, i, -1):
                    while temp % k != 0:
                        k -= 1
                    temp //= k
                    numl[j] = str(k)
                # able to successfully fill characters
                if temp == 1:
                    return "".join(numl)
        # find next biggest num that is divisible by t
        answer = []
        temp = t
        for i in range(9, 1, -1):
            while temp % i == 0:
                answer.append(str(i))
                temp //= i
        # pad answer with needed 1's and return
        answer = "".join(answer)
        padding = max(n+1 - len(answer), 0)
        answer += "1" * padding
        return answer[::-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1234"
        j = 256
        o = "1488"
        self.assertEqual(s.smallestNumber(i,j), o)

    def test_two(self):
        s = Solution()
        i = "12355"
        j = 50
        o = "12355"
        self.assertEqual(s.smallestNumber(i,j), o)

    def test_three(self):
        s = Solution()
        i = "11111"
        j = 26
        o = "-1"
        self.assertEqual(s.smallestNumber(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)