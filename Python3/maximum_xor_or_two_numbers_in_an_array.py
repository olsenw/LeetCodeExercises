# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums, return the maximum result of nums[i]
    XOR nums[j], where 0 <= i <= j < nums.length.

    Constraints:
    * 1 <= nums.length <= 2 * 10^5
    * 0 <= nums[i] <= 2^31 - 1 (aka 32 bit integers)
    '''
    # too slow to be accepted, correct however
    def findMaximumXOR_brute(self, nums: List[int]) -> int:
        a = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                a = max(a, nums[i] ^ nums[j])
                # print(f"{nums[i]} XOR {nums[j]} -> {nums[i] ^ nums[j]} (best: {a})")
        return a

    # busted... not sure where it is going wrong...
    # probably overthinking it when comes to searching for best xor...
    # kept for sake of a first attempt using trie
    def findMaximumXOR_trie_broken(self, nums: List[int]) -> int:
        # for an introduction to trie data structure
        # https://leetcode.com/tag/trie/discuss/1066206/Introduction-to-Trie
        trie = dict()
        # insert values into trie
        for i in nums:
            # a one in the 30th column
            mask = 1073741824
            t = trie
            # cut off one early to allow debug insert after for loop
            for s in range(30):
                m = i & mask == mask
                mask >>= 1
                if m not in t:
                    t[m] = dict()
                t = t[m]
            # put value at end for readability/debug
            t[i & mask == mask] = i
        # find best two to XOR
        # highest set bit and next highest set bit
        bit = 0
        while len(trie) == 1 and bit < 30:
            trie = trie[False] if False in trie else trie[True]
            bit += 1
        high = trie[True]
        low = trie[False] if False in trie else trie[True]
        def recurse(high,low,bit,diff):
            if bit >= 30:
                return diff, high, low
            # only one option force to take
            if len(high) == 1 and len(low) == 1:
                high = high[True] if True in high else high[False]
                low = low[True] if True in low else low[False]
                return recurse(high, low, bit + 1, diff)
            # if only one high option
            elif len(high) == 1:
                w = True in high
                high = high[w]
                low = low[not w]
                return recurse(high, low, bit + 1, diff+1)
            # if only one low option
            elif len(low) == 1:
                w = True in low
                high = high[not w]
                low = low[w]
                return recurse(high, low, bit +1, diff+1)
            # check all options for which have most differnet bits
            else:
                d, h, l = recurse(high[False], low[False], bit+1, diff)
                dp, hp, lp = recurse(high[True], low[True], bit+1, diff)
                if dp > d: d, h, l = dp, hp, lp
                dp, hp, lp = recurse(high[True], low[False], bit+1, diff+1)
                if dp > d: d, h, l = dp, hp, lp
                dp, hp, lp = recurse(high[False], low[True], bit+1, diff+1)
                if dp > d: d, h, l = dp, hp, lp
                return d,h,l
        _, high, low = recurse(high, low, bit, 1)
        return high ^ low

    # based on solution from leetcode discusion port (author darrenli2)
    # first part here is that trie works
    # second there is a best XOR for a given value, and trie finds closest to it
    # https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/1473811/python-using-trie-solution-time-O(N)-space-O(N)
    def findMaximumXOR_trie_slow(self, nums: List[int]) -> int:
        trie = dict()
        # build trie
        for n in nums:
            t = trie
            # shift through all bits in the int
            for i in range(31,-1,-1):
                b = (n >> i) & 1
                if not b in t:
                    t[b] = dict()
                t = t[b]
        # keep track of best found
        best = 0
        for n in nums:
            xor = 0
            t = trie
            for i in range(31,-1,-1):
                # hope for there to be an opposite bit at this position
                b = not (n >> i) & 1
                xor <<= 1
                if b in t:
                    xor += 1
                    t = t[b]
                else:
                    t = t[not b]
            best = max(best, xor)
        return best

    # based on solution from leetcode discusion post (author Crisss)
    # bassically builds best xor and checks if it is possible
    # https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/1170619/Python-or-bit-manipulation-or-set()
    def findMaximumXOR_wtf(self, nums: List[int]) -> int:
        xor = 0
        # iterate through all the bit positions
        for i in range(31,-1,-1):
            # generate all unique prefixes for bit position i
            # ie for 25 = 0b11001 and position 2 (ie bit 2^2) -> 0b110
            prefix = {n >> i for n in nums}
            # left shift xor 
            xor <<= 1
            # the test case of if xor have filled final position
            test = xor + 1
            for p in prefix:
                # check if this xor is in one of the prefixes found
                if test ^ p in prefix:
                    # if it is that means worse case it must be test
                    xor = test
                    # don't have to check other prefixes
                    break
        return xor

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [14,70,53,83,49,91,36,80,92,51,66,70]
        o = 127
        self.assertEqual(s.findMaximumXOR_brute(i), o)
        self.assertEqual(s.findMaximumXOR_trie_slow(i), o)
        self.assertEqual(s.findMaximumXOR_wtf(i), o)

    def test_two(self):
        s = Solution()
        i = [3,10,5,25,2,8]
        o = 28
        self.assertEqual(s.findMaximumXOR_brute(i), o)
        self.assertEqual(s.findMaximumXOR_trie_slow(i), o)
        self.assertEqual(s.findMaximumXOR_wtf(i), o)

    def test_three(self):
        s = Solution()
        i = [i for i in range(2 * 10**5)]
        o = 262143
        # self.assertEqual(s.findMaximumXOR_trie_slow(i), o)
        self.assertEqual(s.findMaximumXOR_wtf(i), o)

    def test_four(self):
        s = Solution()
        i = [1,1]
        o = 0
        self.assertEqual(s.findMaximumXOR_brute(i), o)
        self.assertEqual(s.findMaximumXOR_trie_slow(i), o)
        self.assertEqual(s.findMaximumXOR_wtf(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)