# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    Find the minimum length of a subarray that is not identical to any other
    subarray in nums.

    Return an integer denoting the minimum possible length of such a subarray.

    Two subarrays are considered identical if they have the same length and the
    same elements in corresponding positions.
    '''
    # https://www.geeksforgeeks.org/dsa/introduction-to-rolling-hash-data-structures-and-algorithms/
    # rolling hash => (n1*a^(k-1) + n2*a^(k-2) + ... + nk*a^0) % mod
    # a is a prime number
    # k is length of array
    # n1,n2,...,nk are the k values of array
    # mod is a large prime number
    # can shift left or right by subtracting old element, multiplying/dividing by base, adding new element
    # 
    # O(n^2) results in time limit exceeded 700/719 test cases
    def smallestUniqueSubarray_tle(self, nums: List[int]) -> int:
        n = len(nums)
        base = 31
        mod = 10**9 + 7
        # precalculate all the powers needed in a full length hash
        weights = [1] * (n+1)
        for i in range(1,n+1):
            weights[i] = (weights[i-1] * base) % mod
        # preform search with a given window size (ie length of subarrays to compare)
        def rabinKarp(window:int):
            hashes = Counter()
            # calculate initial hash
            h = 0
            for i in range(window):
                h = (h * base + nums[i]) % mod
            hashes[h] += 1
            # move rolling hash forward
            for i in range(1, n-window+1):
                # remove last element in window
                h = (h - weights[window - 1] * nums[i - 1]) % mod
                # add new element in window
                h = (h * base + nums[i + window - 1]) % mod
                # track hash count
                hashes[h] += 1
            # any unique hashes?
            return any(hashes[i] == 1 for i in hashes)
        # find smallest window with unique rolling hash
        for window in range(1,n):
            if rabinKarp(window):
                return window
        # worst case, whole subarray is unique as it is only subarray
        return n

    # base on binary search hints
    # same rolling hash but binary searching for window length
    # 
    # selecting the base is important in a rolling hash
    # should be a prime larger than all possible values and coprime with mod
    # https://cs.stackexchange.com/questions/93002/by-what-criteria-is-the-base-value-selected-in-rabin-karp-algorithm
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # base = 31 <- causes a cache collision
        base = 10007
        mod = 10**9 + 7
        # precalculate all the powers needed in a full length hash
        weights = [1] * (n+1)
        for i in range(1,n+1):
            weights[i] = (weights[i-1] * base) % mod
        # preform search with a given window size (ie length of subarrays to compare)
        def rabinKarp(window:int):
            hashes = Counter()
            # calculate initial hash
            h = 0
            for i in range(window):
                h = (h * base + nums[i]) % mod
            hashes[h] += 1
            # move rolling hash forward
            for i in range(1, n-window+1):
                # remove last element in window
                h = (h - weights[window - 1] * nums[i - 1]) % mod
                # add new element in window
                h = (h * base + nums[i + window - 1]) % mod
                # track hash count
                hashes[h] += 1
            # any unique hashes?
            return any(hashes[i] == 1 for i in hashes)
        # binary search to find smallest window with unique rolling hash
        answer = 0
        i,j = 1,n
        while i <= j:
            k = (i + j) // 2
            if rabinKarp(k):
                answer = k
                j = k - 1
            else:
                i = k + 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,3,3]
        o = 3
        self.assertEqual(s.smallestUniqueSubarray(i), o)

    def test_two(self):
        s = Solution()
        i = [2,1,2,3,3]
        o = 1
        self.assertEqual(s.smallestUniqueSubarray(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,2,2,1]
        o = 2
        self.assertEqual(s.smallestUniqueSubarray(i), o)

    def test_four(self):
        s = Solution()
        i = [2,1,32]
        o = 1
        self.assertEqual(s.smallestUniqueSubarray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)