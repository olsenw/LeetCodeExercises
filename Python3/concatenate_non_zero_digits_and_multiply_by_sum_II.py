# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import sys
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

sys.set_int_max_str_digits(10**5)
class Solution:
    '''
    Given a string s of length m consisting of digits. Also give a 2D integer
    array queries, where queries[i] = [li, ri].

    For each queries[i], extract the substring s[l,r]. Then perform the
    following:
    * Form a new integer x by concatenating all the non-zero digits from the
      substring in their original order. If there are non non-zero digits x = 0.
    * Let sum be the sum of digits in x. The answer is x * sum.

    Return an array of integers answer where answer[i] is the answer to the ith
    query.

    Since the answer may be very large, return them modulo 10^9 + 7.
    '''
    # O(queries.length * s.length) => O(n^2)
    # also fails due to int conversion being limited to 4300 digits
    def sumAndMultiply_tle(self, s: str, queries: List[List[int]]) -> List[int]:
        m = 10**9 + 7
        # digits = [int(i) for i in s if i != '0']
        running = ""
        prefix = [""]
        for i in s:
            if i != '0':
                running += i
            prefix.append(running)
        answer = []
        for left,right in queries:
            a = prefix[left]
            b = prefix[right+1]
            c = b[len(a):]
            c = max(c,'0')
            s = sum(int(i) for i in c)
            answer.append((int(c) * s) % m)
            pass
        return answer

    # memory limit exceeded
    def sumAndMultiply_memory(self, s: str, queries: List[List[int]]) -> List[int]:
        m = 10**9 + 7
        # digits = [int(i) for i in s if i != '0']
        running = ""
        summation = 0
        prefix = [("",0)]
        for i in s:
            if i != '0':
                running += i
                summation += int(i)
            prefix.append((running,summation))
        answer = []
        for left,right in queries:
            a = prefix[left][0]
            b = prefix[right+1][0]
            c = b[len(a):]
            c = max(c,'0')
            s = prefix[right + 1][1] - prefix[left][1]
            answer.append((int(c) * s) % m)
            pass
        return answer

    def sumAndMultiply_tle(self, s: str, queries: List[List[int]]) -> List[int]:
        m = 10**9 + 7
        digits = "".join([i for i in s if i != '0'])
        running = 0
        summation = 0
        prefix = [(0,0)]
        for i in s:
            if i != '0':
                running += 1
                summation += int(i)
            prefix.append((running,summation))
        answer = []
        for left,right in queries:
            a = prefix[left][0]
            b = prefix[right+1][0]
            c = digits[a:b]
            c = max(c,'0')
            s = prefix[right + 1][1] - prefix[left][1]
            answer.append((int(c) * s) % m)
            pass
        return answer

    # not sure why this one exceeds time limit (test case 508/523)
    # It was calculating the base 10 multiplication...
    # editorial (below) precompute every possible base10 power
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        m = 10**9 + 7
        total = 0
        running = 0
        summation = 0
        prefix = [(0,0,0)]
        for i in s:
            if i != '0':
                total = (total * 10 + int(i)) % m
                running += 1
                summation += int(i)
            prefix.append((total,running,summation))
        answer = []
        for left,right in queries:
            a = prefix[left][0]
            b = prefix[right+1][0]
            x = prefix[left][1]
            y = prefix[right+1][1]
            # c = (b - (a * 10**(y-x))) % m
            c = (b - (a * self.pow10[y-x])) % m
            # c = digits[a:b]
            # c = max(c,'0')
            s = prefix[right + 1][2] - prefix[left][2]
            answer.append((c * s) % m)
            pass
        return answer

    # based on LeetCode editorial
    # https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/editorial/?envType=daily-question&envId=2026-07-08
    MOD = 10**9 + 7
    pow10 = [1] * 100001
    for i in range(1, 100001):
        pow10[i] = (pow10[i-1] * 10) % MOD
    def sumAndMultiply_e(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        sum = [0] * (n+1)
        x = [0] * (n+1)
        cnt = [0] * (n+1)
        for i,c in enumerate(s):
            d = int(c)
            sum[i+1] = sum[i] + d
            x[i+1] = (x[i] * 10 + d) % self.MOD if d > 0 else x[i]
            cnt[i+1] = cnt[i] + (d > 0)
        m = len(queries)
        answer = [0] * m
        for i in range(m):
            left = queries[i][0]
            right = queries[i][1] + 1
            length = cnt[right] - cnt[left]
            answer[i] = (x[right] - x[left] * self.pow10[length]) * (sum[right] - sum[left]) % self.MOD
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "10203004"
        j = [[0,7],[1,3],[4,6]]
        o = [12340, 4, 9]
        self.assertEqual(s.sumAndMultiply(i,j), o)

    def test_two(self):
        s = Solution()
        i = "1000"
        j = [[0,3],[1,1]]
        o = [1,0]
        self.assertEqual(s.sumAndMultiply(i,j), o)

    def test_three(self):
        s = Solution()
        i = "9876543210"
        j = [[0,9]]
        o = [444444137]
        self.assertEqual(s.sumAndMultiply(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)