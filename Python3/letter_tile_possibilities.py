# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    There are n tiles, where each tile has one letter tiles[i] printed on it.

    Return the number of possible non-empty sequences of letters that can be
    made using the letters printed on those tiles.
    '''
    # permutations with repetition
    # https://brilliant.org/wiki/permutations-with-repetition/
    # n! / (n1! n2! ... nk!)
    # doing math wrong except for case of using all letters...
    def numTilePossibilities_wrong(self, tiles: str) -> int:
        def rp(n:int,objects:List[int]) -> int:
            return math.factorial(n) // math.prod(math.factorial(o) for o in objects)
        tiles = sorted(tiles)
        objects = [1]
        for i in range(1,len(tiles)):
            if tiles[i] == tiles[i-1]:
                objects[-1] += 1
            else:
                objects.append(1)
        return sum(rp(i,objects) for i in range(1,len(tiles)+1))

    # gave up on using pure math
    # followed hint to use backtracking
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = Counter(tiles)
        def count()->int:
            answer = 0
            for c in tiles:
                if tiles[c] > 0:
                    tiles[c] -= 1
                    answer += 1 + count()
                    tiles[c] += 1
            # s = max(1, sum(tiles[i] for i in tiles if tiles[i] > 0))
            # return answer * s
            return answer
        return count()

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "AAB"
        o = 8
        self.assertEqual(s.numTilePossibilities(i), o)

    def test_two(self):
        s = Solution()
        i = "AAABBC"
        o = 188
        self.assertEqual(s.numTilePossibilities(i), o)

    def test_three(self):
        s = Solution()
        i = "V"
        o = 1
        self.assertEqual(s.numTilePossibilities(i), o)

    def test_four(self):
        s = Solution()
        i = "VVV"
        o = 3
        self.assertEqual(s.numTilePossibilities(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)