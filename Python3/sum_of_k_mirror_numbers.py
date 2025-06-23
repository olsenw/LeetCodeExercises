# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A k-mirror number is a positive integer without leading zeros that reads the
    same both forward and backward in base-10 as well ass in base-k.

    Given the base k and the number n, return the sum of the n smallest k-mirror
    numbers.
    '''
    def kMirror(self, k: int, n: int) -> int:
        def intToBase(n:int, base:int) -> str:
            if n == 0:
                return "0"
            answer = ""
            while n:
                answer += str(n % base)
                n //= base
            return answer[::-1]
        def palindromGenerator():
            old = ["0"]
            for i in range(1, 10):
                old.append(str(i))
                yield old[-1]
            new = ["00"]
            for i in range(1,10):
                new.append(f'{i}{i}')
                yield new[-1]
            curr = ["000"]
            while True:
                for i in range(10):
                    for j in old:
                        curr.append(f'{i}{j}{i}')
                        yield curr[-1]
                old = new
                new = curr
                curr = ["0"*(len(new[-1]) + 1)]
        answer = 0
        pg = palindromGenerator()
        while n:
            p = next(pg)
            if p[0] == '0':
                continue
            p = int(p)
            s = intToBase(p, k)
            if s == s[::-1]:
                n -= 1
                answer += p
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3,7
        o = 499
        self.assertEqual(s.kMirror(*i), o)

    def test_two(self):
        s = Solution()
        i = 2,5
        o = 25
        self.assertEqual(s.kMirror(*i), o)

    def test_three(self):
        s = Solution()
        i = 7,17
        o = 20379000
        self.assertEqual(s.kMirror(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)