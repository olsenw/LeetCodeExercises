# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n representing the dimensions of an n x n grid, with the
    origin at the bottom-left corner of the grid. Also give a 2D array of
    coordinates rectangles, where rectangles[i] is in the form
    [startx, starty, endx, endy], representing a rectangle on the grid. Each
    rectangle is defined as follows:
    * (startx, starty): The bottom-left corner of the rectangle.
    * (endx, endy): The top-right corner of the rectangle.

    Note that the rectangles do not overlap. Determine if it is possible to make
    either two horizontal or two vertical cuts on the grid such that:
    * Each of the three resulting sections formed by the cuts contains at least
      one rectangle.
    * Every rectangle belongs o exactly one section.

    Return true if such cuts can be made; otherwise, return false.
    '''
    def checkValidCuts_linepass(self, n: int, rectangles: List[List[int]]) -> bool:
        horizontal = []
        vertical = []
        for x,y,a,b in rectangles:
            # heapq.heappush(horizontal, (x,1))
            horizontal.append((x,1))
            # heapq.heappush(horizontal, (a,-1))
            horizontal.append((a,-1))
            # heapq.heappush(vertical, (y,1))
            vertical.append((y,1))
            # heapq.heappush(vertical, (y,-1))
            vertical.append((b,-1))
        horizontal.sort()
        vertical.sort()
        rect = 0
        for i,v in horizontal:
            pass
        return

    def checkValidCuts_passes(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(arr:List[List[int]]) -> bool:
            s,e = arr[0]
            i,j = 0, len(arr) - 1
            while i < len(arr) and arr[i][0] < e:
                e = max(e, arr[i][1])
                i += 1
            i -= 1
            s,e = arr[-1]
            while i <= j and s < arr[j][1]:
                s = min(s, arr[j][0])
                j -= 1
            j += 1
            return j - i > 1
        def prune(arr:List[List[int]]) -> List[List[int]]:
            horizontal = sorted(arr, key=lambda x:(x[0],-x[1]))
            last = horizontal[0]
            arr = []
            for i,j in horizontal:
                if last[1] <= i:
                    arr.append(last)
                    last = [i,j]
                else:
                    last[1] = max(last[1],j)
            arr.append(last)
            return arr
        horizontal = [[x,a] for x,_,a,_ in rectangles]
        if check(prune(horizontal)):
            return True 
        vertical = [[y,b] for _,y,_,b in rectangles]
        return check(prune(vertical))

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def prune(arr:List[List[int]]) -> List[List[int]]:
            horizontal = sorted(arr, key=lambda x:(x[0],-x[1]))
            last = horizontal[0]
            arr = []
            for i,j in horizontal:
                if last[1] <= i:
                    arr.append(last)
                    last = [i,j]
                else:
                    last[1] = max(last[1],j)
            arr.append(last)
            return arr
        horizontal = [[x,a] for x,_,a,_ in rectangles]
        if len(prune(horizontal)) > 2:
            return True 
        vertical = [[y,b] for _,y,_,b in rectangles]
        return len(prune(vertical)) > 2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
        o = True
        self.assertEqual(s.checkValidCuts(i,j), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
        o = True
        self.assertEqual(s.checkValidCuts(i,j), o)

    def test_three(self):
        s = Solution()
        i = 4
        j = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
        o = False
        self.assertEqual(s.checkValidCuts(i,j), o)

    def test_four(self):
        s = Solution()
        i = 3
        j = [[0,0,1,3],[1,0,2,2],[2,0,3,2],[1,2,3,3]]
        o = False
        self.assertEqual(s.checkValidCuts(i,j), o)

    def test_five(self):
        s = Solution()
        i = 4
        j = [[0,0,1,4],[1,0,2,3],[2,0,3,3],[3,0,4,3],[1,3,4,4]]
        o = False
        self.assertEqual(s.checkValidCuts(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)