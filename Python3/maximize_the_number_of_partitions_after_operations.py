# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and an integer k.

    It is possible to change at most one index in s to another lowercase English
    letter.

    After changing a letter, do the following partitioning operation until s is
    empty:
    * Choose the longest prefix of s containing at most k distinct characters.
    * Delete the prefix from s and increase the number of partitions by one. The
      remaining characters (if any) in s maintain their initial order.
    
    Return an integer denoting the maximum number of resulting partitions after
    the operations by optimally choosing at most one index to change.
    '''
    # brute force O(26 n^2)
    def maxPartitionsAfterOperations_brute_force(self, s: str, k: int) -> int:
        def partition(s:list[int]) -> int:
            answer = 0
            bitmask = 0
            for c in s:
                i = 1 << (ord(c) - 97)
                bitmask |= i
                if bin(bitmask).count("1") > k:
                    answer += 1
                    bitmask = i
            return answer + (bitmask > 0)
        answer = 0
        n = len(s)
        s = list(s)
        for i in range(n):
            c = s[i]
            for j in "abcdefghijklmnopqrstuvwxyz":
                s[i] = j
                answer = max(answer, partition(s))
            s[i] = c
        return answer

    # attempt at using hints
    # not sure how to calculate the suffix partitions and find answer
    def maxPartitionsAfterOperations_hints(self, s: str, k: int) -> int:
        n = len(s)
        # start position of given partition
        starts = [0]
        # number of partitions for s[0:i]
        prefix = [0] * n
        # number of partitions for s[i:n]
        suffix = [n] * n
        
        # precalculate prefix partitions
        bitmask = 0
        for i,j in enumerate(s):
            c = 1 << (ord(j) - 97)
            bitmask |= c
            if bin(bitmask).count("1") > k:
                starts.append(i)
                bitmask = c
            prefix[i] = len(starts) - 1
        # precalculate suffix partitions
        return

    # leetcode editorial
    # https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/editorial/?envType=daily-question&envId=2025-10-17
    # an implementation of hints
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        # partitions left of character i
        # left[i] = [number of splits prefix, character mask, number distinct characters]
        left = [[0] * 3 for _ in range(n)]
        right = [[0] * 3 for _ in range(n)]

        num,bitmask,count = 0,0,0
        for i in range(n-1):
            binary = 1 << (ord(s[i]) - 97)
            if not (bitmask & binary):
                count += 1
                if count <= k:
                    bitmask |= binary
                else:
                    num += 1
                    bitmask = binary
                    count = 1
            left[i+1][0] = num
            left[i+1][1] = bitmask
            left[i+1][2] = count

        num,bitmask,count = 0,0,0
        for i in range(n-1,0,-1):
            binary = 1 << (ord(s[i]) - 97)
            if not (bitmask & binary):
                count += 1
                if count <= k:
                    bitmask |= binary
                else:
                    num += 1
                    bitmask = binary
                    count = 1
            right[i-1][0] = num
            right[i-1][1] = bitmask
            right[i-1][2] = count
        
        answer = 0
        for i in range(n):
            splits = left[i][0] + right[i][0] + 2
            bitmask = left[i][1] | right[i][1]
            count = bin(bitmask).count('1')
            if left[i][2] == k and right[i][2] == k and count < 26:
                splits += 1
            elif min(count + 1, 26) <= k:
                splits -= 1
            answer = max(answer, splits)
        
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "accca"
        j = 2
        o = 3
        self.assertEqual(s.maxPartitionsAfterOperations(i,j), o)

    def test_two(self):
        s = Solution()
        i = "aabaab"
        j = 3
        o = 1
        self.assertEqual(s.maxPartitionsAfterOperations(i,j), o)

    def test_three(self):
        s = Solution()
        i = "xxyz"
        j = 1
        o = 4
        self.assertEqual(s.maxPartitionsAfterOperations(i,j), o)

    def test_four(self):
        s = Solution()
        i = "c"
        j = 3
        o = 1
        self.assertEqual(s.maxPartitionsAfterOperations(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)