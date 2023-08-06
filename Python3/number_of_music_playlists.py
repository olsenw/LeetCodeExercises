# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A music player contains n different songs. The goal is listen to goal (not
    necessarily different) during a trip. To avoid boredom, playlists are
    created such that:
    * Every song is played at least once.
    * A song can only be played again only if k other songs have been played.

    Given n, goal, and k, return the number of possible playlists that can be
    created. Since the answer may be large return it modulo 10**9 + 7.
    '''
    # based on LeetCode editorial bottom up
    # https://leetcode.com/problems/number-of-music-playlists/editorial/
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        m = 10**9 + 7
        def mul(a,b):
            return ((a % m) * (b % m)) % m
        def add(a,b):
            return ((a % m) + (b % m)) % m
        # base case i < j ie impossible to have more unique songs than length
        dp = [[0] * (n+1) for _ in range(goal+1)]
        # base case number of ways to form empty playlist
        dp[0][0] = 1
        # playlist length
        for i in range(1, goal+1):
            # unique songs in playlist
            for j in range(1, min(i,n) + 1):
                # add the number of playlist by adding new unique song
                dp[i][j] = add(dp[i][j], mul(dp[i-1][j-1], n - j + 1))
                # can repeat a song
                if j > k:
                    # add the number of playlist by repeating a song
                    dp[i][j] = add(dp[i][j], mul(dp[i-1][j], j - k))
        return dp[goal][n]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = (3,3,1)
        o = 6
        self.assertEqual(s.numMusicPlaylists(*i), o)

    def test_two(self):
        s = Solution()
        i = (2,3,0)
        o = 6
        self.assertEqual(s.numMusicPlaylists(*i), o)

    def test_three(self):
        s = Solution()
        i = (2,3,1)
        o = 2
        self.assertEqual(s.numMusicPlaylists(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)