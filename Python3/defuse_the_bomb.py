# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is a bomb to defuse and time is running out! An informer has provided
    a circular array code of length n and a key k.

    To decrypt the code all numbers must be replaced simultaneously.
    * if k > 0, replace the ith number with the sum of the next k numbers.
    * if k < 0, replace the ith number with the sum of the previous k numbers.
    * if k == 0, replace the ith number with 0.

    As code is circular, the next element of code[n-1] is code[0], and the
    previous element of code[0] is code[n-1].

    Given the circular array code and an integer key k, return the decrypted
    code to defuse the bomb!
    '''
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        answer = [0] * n
        if k == 0:
            return answer
        elif k < 0:
            k = abs(k)
            s = sum(code[-k:])
            for i in range(n):
                answer[i] = s
                s += code[i]
                # this works because of pythons list with negative numbers
                s -= code[i - k]
            pass
        else:
            s = sum(code[:k])
            for i in range(n-1,-1,-1):
                answer[i] = s
                s += code[i]
                s -= code[(i + k) % n]
            pass
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,7,1,4]
        j = 3
        o = [12,10,16,13]
        self.assertEqual(s.decrypt(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        j = 0
        o = [0,0,0,0]
        self.assertEqual(s.decrypt(i,j), o)

    def test_three(self):
        s = Solution()
        i = [2,4,9,3]
        j = -2
        o = [12,5,6,13]
        self.assertEqual(s.decrypt(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)