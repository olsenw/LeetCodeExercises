# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from math import acos, degrees, sqrt, pi

class Solution:
    '''
    Given an array trees where trees[i] = [xi, yi] represents the location
    of a tree in the garden.
    
    Fence the entire garden using the minimum length of rope. The garden is
    fenced only if all the trees are enclosed.
    
    Return the coordinates of the trees that are exactly located on the
    fence perimeter.
    '''
    # find far left and wrap clockwise
    def outerTrees_wrong(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort()
        # fence = [min(trees)]
        fence = [trees[0]]
        # check other trees for inclusion into fence
        for t in trees[1:]:
            # initial vector and tree
            a = (t[0] - fence[-1][0], t[1] - fence[-1][1])
            tree = t
            for n in trees:
                if n in fence:
                    continue
                b = (n[0] - fence[-1][0], n[1] - fence[-1][1])
                angle = acos((a[0]*b[0] + a[1]*b[1]) / (sqrt(a[0]*a[0] + a[1]*a[1]) * sqrt(b[0]*b[0] + b[1]*b[1])))
                # if between 0 and 180 reset tree (should be 0 to 90 practically)
                # if -180.0 < angle < 0.0:
                if 0.0 < angle < 3.1415/2:
                    tree = n
                    a = b
            # add tree to fence
            fence.append(tree)
        # return answer
        return fence

    # find far left and wrap clockwise
    # 29 / 88 test cases
    def outerTrees_close(self, trees: List[List[int]]) -> List[List[int]]:
        # create vector from point a to point b
        def vector(ax,ay,bx,by):
            return [bx-ax, by-ay]
        def isRight(ax,ay,bx,by):
            dot = ax * -by + ay * bx
            return dot > 0
        # angle between vector a and b
        def angle(ax,ay,bx,by):
            dot = ax * bx + ay * by
            ma = sqrt(ax * ax + ay * ay)
            mb = sqrt(bx * bx + by * by)
            return acos(dot / (ma * mb))
        # determine if point b is on vector v originating from point a
        def solve(ax,ay,bx,by,vx,vy):
            if vx == 0.0:
                return ax == bx
            if vy == 0.0:
                return ay == by
            return (bx-ax) / vx == (by-ay) / vy
        # trivial case
        if len(trees) < 3:
            return trees
        # impose order on trees (may be able to do away with)
        trees.sort()
        sx,sy = trees[0]
        fence = [t for t in trees if sx == t[0]]
        vx,vy = vector(sx,sy,sx,101)
        while True:
            a = pi
            nx,ny = fence[-1]
            for tx,ty in trees:
                ux,uy = vector(fence[-1][0],fence[-1][1],tx,ty)
                if isRight(vx,vy,ux,uy):
                    b = angle(vx,vy,ux,uy)
                    if b < a:
                        a = b
                        nx,ny = tx,ty
            if len(fence) == len(trees) or nx == sx and ny == sy:
                break
            vx,vy = vector(fence[-1][0],fence[-1][1],nx,ny)
            # fence.append([nx,ny])
            fence.extend([t for t in trees if t not in fence and solve(fence[-1][0],fence[-1][1],t[0],t[1],vx,vy)])
        return fence

    # leetcode solution (Jarvis Algorithm)
    # https://leetcode.com/problems/erect-the-fence/solution/
    # in essence what I was trying to do above... but correct
    # O(m * n) time
    # O(m) space
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # p last point added to the hull
        # q point being considered for addition to hull
        # r any other point in the space
        # cross product of pq and qr is positive if q is more counter clockwise than r
        def orientation(p,q,r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        # is point i colinear in regards to vector created by points p to q
        # more vector calc (I think cross product...)
        def inBetween(p,i,q):
            a = i[0] >= p[0] and i[0] <= q[0] or i[0] <= p[0] and i[0] >= q[0]
            b = i[1] >= p[1] and i[1] <= q[1] or i[1] <= p[1] and i[1] >= q[1]
            return a and b
        # convex hull surrounding the trees
        hull = set()
        # trivial case of 1,2 or 3 trees
        if len(trees) < 4:
            return trees
        # find leftmost point
        left = min(trees)
        # last point added to hull
        p = left
        while True:
            q = trees[(trees.index(p) + 1) % len(trees)]
            for i in trees:
                if orientation(p,i,q) < 0:
                    q = i
            for i in trees:
                if i != p and i != q and orientation(p, i, q) == 0 and inBetween(p,i,q):
                    hull.add(tuple(i))
            hull.add(tuple(q))
            p = q
            if p == left:
                break
        return [list(t) for t in hull]

    '''
    Other valid solutions (also more traditionally accepted)
    Graham Scan O(n log n) time O(n) space
    Monotone Chain O(n log n) time O(n) space
    '''
class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
        o = [[1,1],[2,0],[3,3],[2,4],[4,2]]
        self.assertEqual(sorted(s.outerTrees(i)), sorted(o))

    def test_two(self):
        s = Solution()
        i = [[1,2],[2,2],[4,2]]
        o = [[4,2],[2,2],[1,2]]
        self.assertEqual(sorted(s.outerTrees(i)), sorted(o))

    def test_three(self):
        s = Solution()
        i = [[1,1],[1,10],[10,1]]
        o = [[1,1],[1,10],[10,1]]
        self.assertEqual(sorted(s.outerTrees(i)), sorted(o))

    def test_four(self):
        s = Solution()
        i = [[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]
        o = [[4,5],[2,5],[6,1],[3,5],[2,1],[1,4],[1,2],[7,4],[7,3],[7,2],[3,0],[0,3],[5,0],[5,5],[4,0],[6,5]]
        self.assertEqual(sorted(s.outerTrees(i)), sorted(o))

    def test_five(self):
        s = Solution()
        i = [[0,1],[1,0],[100,100],[99,100],[100,99]]
        o = [[1,0],[99,100],[100,100],[0,1],[100,99]]
        self.assertEqual(sorted(s.outerTrees(i)), sorted(o))

if __name__ == '__main__':
    unittest.main(verbosity=2)