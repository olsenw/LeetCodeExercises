# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import itertools
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two positive integers n and k.

    An integer x is called k-palindromic if:
    * x is a palindrome.
    * x is divisible by k.

    An integer is called good if its digits can be rearranged to form a
    k-palindromic integer. For example, for k = 2, 2020 can be rearranged to
    form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to
    form a k-palindromic integer.

    Return the count of good integers containing n digits.

    Note that any integers must not have leading zeros, neither before or after
    rearrangement. For example, 1010 cannot be rearranged to form 101.
    '''
    # fails
    def countGoodIntegers_fails(self, n: int, k: int) -> int:
        limit = 10 ** (n//2)
        valid = Counter()
        for i in range(1,limit):
            if i % k == 0 and i % 10:
                valid[tuple(sorted(f'{i:05}'))] += 1
            pass
        answer = sum(valid[i] for i in valid)
        if n % 2:
            answer *= 10
        return answer

    # brute force without rearrangement
    def countGoodIntegers_wrong(self, n: int, k: int) -> int:
        if n == 1:
            return 9 // k
        answer = 0
        for i in range(k, 10**(n//2), k):
            if i % 10:
                answer += 1
        return answer

    def countGoodIntegers_wrong2(self, n: int, k: int) -> int:
        if n == 1:
            return 9 // k
        answer = 0
        limit = n // 2
        s = "".join(str(i) * limit for i in range(10))
        for p in itertools.permutations(s, limit):
            i = 0
            for c in p:
                i *= 10
                i += int(c)
            if i % k == 0 and i % 10:
                answer += 1
        if n % 2:
            answer *= 10
        return answer

    # palindrome generation is invalid (not reminder k and not all possible)
    def countGoodIntegers_wrong3(self, n: int, k: int) -> int:
        if n == 1:
            return 9 // k
        valid = set()
        for p in range(k,10**(n//2),k):
            if p % 10:
                p = str(p)
                if n % 2:
                    for c in "0123456789":
                        valid.add(p[::-1] + c + p)
                else:
                    valid.add(p[::-1] + p)
        answer = set()
        for i in valid:
            for j in itertools.permutations(i,n):
                if j[0] != '0':
                    answer.add(j)
        return len(answer)

    # passes... but times out (lot of memory too)
    def countGoodIntegers_tle(self, n: int, k: int) -> int:
        if n == 1:
            return 9 // k
        answer = set()
        palindromes = set()
        upper = 10**n
        upper -= upper % k
        lower = 10**(n-1)
        for i in range(upper, lower, -k):
            s = str(i)
            if s[::-1] == s:
                palindromes.add(s)
                for j in itertools.permutations(s, n):
                    if j[0] != '0':
                        answer.add(''.join(j))
        return len(answer)

    # math for permutations with repeat objects probably good
    # generating incorrect palindromes again
    def countGoodIntegers_wrong4(self, n: int, k: int) -> int:
        def per(t:tuple[int]) -> int:
            answer = 0
            num = math.factorial(n-1)
            for i in range(1,10):
                if t[i] == 0:
                    continue
                dem = 1
                for j in range(10):
                    if i == j:
                        dem *= math.factorial(t[j]-1)
                    else:
                        dem *= math.factorial(t[j])
                answer += num // dem
            return answer
        limit = n//2 + n%2
        palindromes = set()
        a = set()
        m = 0
        for i in range(k, 10 ** limit, k):
            if i % 10 == 0:
                continue
            s = str(i).zfill(limit)
            s = s[::-1][:limit - 1 if n % 2 else limit] + s
            if int(s) % k == 0:
                m+=1
                a.add(s)
                palindromes.add(tuple(s.count(i) for i in '0123456789'))
                pass
        answer = []
        for p in palindromes:
            answer.append(per(p))
        return sum(answer)

    def countGoodIntegers_tle2(self, n: int, k: int) -> int:
        def per(t:tuple[int]) -> int:
            answer = 0
            num = math.factorial(n-1)
            for i in range(1,10):
                if t[i] == 0:
                    continue
                dem = 1
                for j in range(10):
                    if i == j:
                        dem *= math.factorial(t[j]-1)
                    else:
                        dem *= math.factorial(t[j])
                answer += num // dem
            return answer
        palindromes = set()
        upper = 10**n
        upper -= upper % k
        lower = 10**(n-1)
        for i in range(upper, lower, -k):
            s = str(i)
            if s[::-1] == s:
                palindromes.add(tuple(s.count(i) for i in '0123456789'))
                # palindromes.add(s)
        answer = []
        for p in palindromes:
            answer.append(per(p))
        return sum(answer)

    def countGoodIntegers(self, n: int, k: int) -> int:
        def per(t:tuple[int]) -> int:
            answer = 0
            num = math.factorial(n-1)
            for i in range(1,10):
                if t[i] == 0:
                    continue
                dem = 1
                for j in range(10):
                    if i == j:
                        dem *= math.factorial(t[j]-1)
                    else:
                        dem *= math.factorial(t[j])
                answer += num // dem
            return answer
        limit = n//2 + n%2
        palindromes = set()
        a = set()
        m = 0
        for i in range(10 ** limit):
            if i % 10 == 0:
                continue
            s = str(i).zfill(limit)
            s = s[::-1][:limit - 1 if n % 2 else limit] + s
            if int(s) % k == 0:
                m+=1
                a.add(s)
                palindromes.add(tuple(s.count(i) for i in '0123456789'))
                pass
        answer = []
        for p in palindromes:
            answer.append(per(p))
        return sum(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3, 5
        o = 27
        self.assertEqual(s.countGoodIntegers(*i), o)

    def test_two(self):
        s = Solution()
        i = 1, 4
        o = 2
        self.assertEqual(s.countGoodIntegers(*i), o)

    def test_three(self):
        s = Solution()
        i = 5, 6
        o = 2468
        self.assertEqual(s.countGoodIntegers(*i), o)

    def test_four(self):
        s = Solution()
        i = 2, 5
        o = 1
        self.assertEqual(s.countGoodIntegers(*i), o)

    def test_five(self):
        s = Solution()
        i = 10, 1
        o = 41457024
        self.assertEqual(s.countGoodIntegers(*i), o)

    def test_six(self):
        s = Solution()
        i = 4, 6
        o = 58
        self.assertEqual(s.countGoodIntegers(*i), o)

    def test_seven(self):
        s = Solution()
        i = 3, 6
        o = 30
        self.assertEqual(s.countGoodIntegers(*i), o)

    def test_eight(self):
        s = Solution()
        i = 2, 6
        o = 1
        self.assertEqual(s.countGoodIntegers(*i), o)

    def test_nine(self):
        s = Solution()
        i = 3, 1
        o = 243
        self.assertEqual(s.countGoodIntegers(*i), o)

    def test_ten(self):
        s = Solution()
        i = 4, 7
        o = 76
        self.assertEqual(s.countGoodIntegers(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)