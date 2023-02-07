# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A farm has a single row of fruit trees arranged from left to right. The
    trees are represented by an integer array fruits where fruits[i] is the type
    of fruit the ith tree produces.

    A person wants to collect the most fruit possible. However the farmer has
    some strict rules that must be followed:
    * There are two baskets, and each basket can only hold a single type of
      fruit. There is no limit on the amount of fruit each basket can hold.
    * Starting from any tree, it is required to pick one fruit from every tree
      (including the start tree) while moving to the right. The picked fruits 
      must fit in one of the two baskets.
    * Once a tree is reached that has fruit which cannot fit into either basket,
      stop picking fruit.

    Given the integer array fruits, return the maximum number of fruits that can
    be picked.
    '''
    # O(n^2)
    def totalFruit_brute(self, fruits: List[int]) -> int:
        answer = 0
        for i in range(len(fruits)):
            a,b = fruits[i], None
            for j in range(i + 1, len(fruits)):
                if fruits[j] == a or fruits[j] == b:
                    continue
                elif b == None:
                    b = fruits[j]
                else:
                    answer = max(answer, j - i + 1)
                    break
            answer = max(answer, j - i + 1)
        return answer

    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 1:
            return 1
        answer = 1
        f = {fruits[0]:1}
        i, j = 0, 1
        while j < len(fruits):
            if fruits[j] in f:
                f[fruits[j]] += 1
            else:
                f[fruits[j]] = 1
            if len(f) > 2:
                if f[fruits[i]] > 1:
                    f[fruits[i]] -= 1
                else:
                    del f[fruits[i]]
                i += 1
            else:
                answer = max(answer, j - i + 1)
            j += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,1]
        o = 3
        self.assertEqual(s.totalFruit(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1,2,2]
        o = 3
        self.assertEqual(s.totalFruit(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,2,2]
        o = 4
        self.assertEqual(s.totalFruit(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)