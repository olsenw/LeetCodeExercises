# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums consisting of positive integers.

    A subarray is of nums is called nice if the bitwise AND of every pair of
    elements that are in different positions in the subarray is equal to 0.

    Return the length of the longest nice subarray.

    A subarray is a contiguous part of an array.

    Note that subarrays of length 1 are always considered nice.
    '''
    # passes
    def longestNiceSubarray_passes(self, nums: List[int]) -> int:
        a = [0] * 32
        def add(i:int) -> None:
            for j in range(32):
                a[j] += i & 1
                i >>= 1
        def sub(i:int) -> None:
            for j in range(32):
                if a[j]:
                    a[j] -= i & 1
                i >>= 1
        def test() -> bool:
            # return all(a[i] <= 1 for i in range(32))
            return any(a[i] > 1 for i in range(32))
        answer = 1
        add(nums[0])
        i,j = 0,1
        while j < len(nums):
            add(nums[j])
            while i < j and test():
                sub(nums[i])
                i += 1
            answer = max(answer, j - i + 1)
            j += 1
        return answer

    def longestNiceSubarray(self, nums: List[int]) -> int:
        answer = 1
        a = 0
        i,j = 0,0
        while j < len(nums):
            while a & nums[j]:
                a ^= nums[i]
                i += 1
            a ^= nums[j]
            answer = max(answer, j - i + 1)
            j += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,8,48,10]
        o = 3
        self.assertEqual(s.longestNiceSubarray(i), o)

    def test_two(self):
        s = Solution()
        i = [3,1,5,11,13]
        o = 1
        self.assertEqual(s.longestNiceSubarray(i), o)

    def test_three(self):
        s = Solution()
        i = [744437702,379056602,145555074,392756761,560864007,934981918,113312475,1090,16384,33,217313281,117883195,978927664]
        o = 3
        self.assertEqual(s.longestNiceSubarray(i), o)
        '''
        [
        '00101100010111110011011111000110',
        '00010110100101111111000111011010',
        '00001000101011001111111010000010',
        '00010111011010001111111000011001',
        '00100001011011100001101100000111',
        '00110111101110101011000100011110',
        '00000110110000010000001011011011',
        '00000000000000000000010001000010',
        '00000000000000000100000000000000',
        '00000000000000000000000000100001',
        '00001100111100111111000000000001',
        '00000111000001101100000100111011',
        '00111010010110010100000000110000']
        '''

if __name__ == '__main__':
    unittest.main(verbosity=2)