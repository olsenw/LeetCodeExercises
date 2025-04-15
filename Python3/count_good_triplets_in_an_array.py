# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two 0-indexed arrays nums1 and nums2 of length n, both of which are
    permutations of [0, 1, ..., n-1].

    A good triplet is a set of 3 distinct values which are present in increasing
    order by position in both nums1 and nums2. In other words, if pos1v is
    considered as the index of value v in nums1, and nums2 as the index of value
    v in nums 2, then a good triplet will be a set (x, y, z) where
    0 <= x,y,z <= n-1, such that pos1x < pos1y < pos1z and
    pos2x < pos2y < pos2z.

    Return the total number of good triplets.
    '''
    # test case 51 over counts
    def goodTriplets_fails(self, nums1: List[int], nums2: List[int]) -> int:
        answer = 0
        leftA,rightA = set(), set(nums1)
        leftB,rightB = set(), set(nums2)
        unionLeft, unionRight = set(), set(nums1)
        for x,y in zip(nums1,nums2):
            rightA.discard(x)
            rightB.discard(y)
            unionRight.discard(x)
            unionRight.discard(y)
            answer += len(unionLeft) * len(unionRight)
            leftA.add(x)
            leftB.add(y)
            if x in leftB:
                unionLeft.add(x)
            if y in leftA:
                unionLeft.add(y)
        return answer

    # too many repeated calculations on intersections
    def goodTriplets_tle(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        answer = 0
        d = dict()
        left, right = set(), set(nums1)
        for v in nums1:
            right.remove(v)
            d[v] = set(left),set(right)
            left.add(v)
        left,right = set(), set(nums2)
        for v in nums2:
            right.remove(v)
            answer += len(left.intersection(d[v][0])) * len(right.intersection(d[v][1]))
            left.add(v)
        return answer

    def goodTriplets_tle2(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        answer = 0
        indices = {j:i for i,j in enumerate(nums1)}
        left = set()
        right = set(nums2)
        for v in nums2:
            right.remove(v)
            l = sum(nums1[i] in left for i in range(indices[v]))
            r = sum(nums1[i] in right for i in range(indices[v]+1,n))
            answer += l * r
            left.add(v)
        return answer

    # doing union based on index not working
    # or at least need to pick indices better when calling numbers
    def goodTriplets_wrong(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        answer = 0
        dp = {i:None for i in range(n)}
        indices = {j:i for i,j in enumerate(nums2)}
        left1, right1 = set(), set(nums1)
        left2, right2 = set(), set(nums2)
        leftUnion, rightUnion = set(), set(nums1)
        for i in range(n):
            x = nums1[i]
            y = nums2[i]
            right1.remove(x)
            right2.remove(y)
            rightUnion.discard(x)
            rightUnion.discard(y)
            # dp[i] = len(leftUnion), len(rightUnion)
            dp[i] = set(leftUnion), set(rightUnion)
            left1.add(x)
            left2.add(y)
            if x in left2:
                leftUnion.add(x)
            if y in left1:
                leftUnion.add(y)
        for i,v in enumerate(nums1):
            j = min(i, indices[v])
            # j = max(j, 0)
            k = max(i, indices[v])
            # k = min(k, n-1)
            # answer += dp[j][0] * dp[k][1]
            answer += len(dp[j][0]) * len(dp[k][1])
        return answer

    def goodTriplets_tle3(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        answer = 0
        leftDP = {v:None for v in range(n)}
        rightDP = {v:None for v in range(n)}
        left, right = set(), set(range(n))
        for v in nums1:
            right.remove(v)
            leftDP[v] = set(left)
            rightDP[v] = set(right)
            left.add(v)
        left, right = set(), set(range(n))
        for v in nums2:
            right.remove(v)
            # leftDP[v] = set(left)
            # rightDP[v] = set(right)
            answer += len(left.intersection(leftDP[v])) * len(right.intersection(rightDP[v]))
            left.add(v)
        return answer

    # based on leetcode binary indexed tree solution
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # https://en.wikipedia.org/wiki/Fenwick_tree
        class FenwickTree:
            def __init__(self, size):
                self.tree = [0] * (size + 1)
                self.size = size
            def update(self, index, delta):
                index += 1
                while index <= self.size:
                    self.tree[index] += delta
                    index += index & -index
            def query(self, index):
                index += 1
                answer = 0
                while index > 0:
                    answer += self.tree[index]
                    index -= index & -index
                return answer
        n = len(nums1)
        pos2, reversedIndexMapping = [0] * n, [0] * n
        for i, j in enumerate(nums2):
            pos2[j] = i
        for i, j in enumerate(nums1):
            reversedIndexMapping[pos2[j]] = i
        tree = FenwickTree(n)
        answer = 0
        for v in range(n):
            pos = reversedIndexMapping[v]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (n - 1 - pos) - (v - left)
            answer += left * right
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,0,1,3]
        j = [0,1,2,3]
        o = 1
        self.assertEqual(s.goodTriplets(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,0,1,3,2]
        j = [4,1,0,2,3]
        o = 4
        self.assertEqual(s.goodTriplets(i,j), o)

    def test_three(self):
        s = Solution()
        i = [13,14,10,2,12,3,9,11,15,8,4,7,0,6,5,1]
        j = [8,7,9,5,6,14,15,10,2,11,4,13,3,12,1,0]
        o = 77
        self.assertEqual(s.goodTriplets(i,j), o)

    def test_four(self):
        s = Solution()
        i = list(range(10**5))
        j = list(range(10**5))
        o = 166661666700000
        self.assertEqual(s.goodTriplets(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)