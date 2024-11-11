# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums of length n.

    The following operation can be performed many time times as needed:
    * Pick an index i that has not been picked before, and pick a prime p
      strictly less than nums[i], then subtract p from nums[i].

    Return true if it is possible to make nums a strictly increasing array using
    the above operation and false otherwise.

    A strictly increasing array is an array whose each element is strictly
    greater than its preceding element.
    '''
    # important 1 <= nums[i] <= 1000
    primes = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    def primeSubOperation(self, nums: List[int]) -> bool:
        last = 0
        for n in nums:
            if n <= last:
                return False
            i = bisect.bisect_left(self.primes, n - last)
            last = n
            if i:
                last = n - self.primes[i-1]
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,9,6,10]
        o = True
        self.assertEqual(s.primeSubOperation(i), o)

    def test_two(self):
        s = Solution()
        i = [6,8,11,12]
        o = True
        self.assertEqual(s.primeSubOperation(i), o)

    def test_three(self):
        s = Solution()
        i = [5,8,3]
        o = False
        self.assertEqual(s.primeSubOperation(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)