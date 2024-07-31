# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array books where books[i] = [thicknessi, heighti] indicates the
    thickness and height of the ith book. Also given is an integer shelfWidth.

    Place these books in order onto bookcase shelves that have a total width
    shelfWidth.

    Choose some of the books to place on this shelf such that the sum of their
    thickness is less than or equal to shelfWidth, then build another level of
    the shelf of the bookcase so that the total height of the bookcase has
    increased by the maximum height of the books just placed. Repeat this
    process until there are no more books to place.

    Note that at each step of the above process, the order of the books is the
    same order as the given sequence of books.

    Return the minimum possible height that the total bookshelf can be after
    placing shelves in this manner.
    '''
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        cache = [[0] * (shelfWidth + 1) for _ in range(n)]
        def dp(index, shelfRemain, bookHeight):
            w,h = books[index]
            newHeight = max(h, bookHeight)
            if index == n - 1:
                if w <= shelfRemain:
                    return newHeight
                return bookHeight + h
            if cache[index][shelfRemain] != 0:
                return cache[index][shelfRemain]
            if w > shelfRemain:
                cache[index][shelfRemain] = bookHeight + dp(index + 1, shelfWidth - w, h)
            else:
                cache[index][shelfRemain] = min(
                    dp(index + 1, shelfRemain - w, newHeight),
                    bookHeight + dp(index + 1, shelfWidth - w, h)
                )
            return cache[index][shelfRemain]
        return dp(0, shelfWidth, 0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
        j = 4
        o = 6
        self.assertEqual(s.minHeightShelves(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,3],[2,4],[3,2]]
        j = 6
        o = 4
        self.assertEqual(s.minHeightShelves(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)