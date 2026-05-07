# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    From any index i, it is possible to jump to another index j under the
    following rules:
    * Jump to index j where j > i is allowed only if nums[j] < nums[i].
    * Jump to index j where j < i is allowed only if nums[j] > nums[i].

    For each index i, find the maximum value in nums that can be reached by
    following any sequence of valid jumps starting at i.

    Return an array ans where ans[i] is the maximum value reachable starting
    from index i.
    '''
    # generating the graph is O(n^2)
    def maxValue_tle(self, nums: List[int]) -> List[int]:
        n = len(nums)
        graph = {i:[j for j in range(n) if (j < i and nums[j] > nums[i]) or (j > i and nums[j] < nums[i])] for i in range(n)}
        answer = [0] * n
        def bfs(index:int) -> int:
            a = nums[index]
            visited = {index}
            queue = deque(graph[index])
            while queue:
                i = queue.popleft()
                if i in visited:
                    continue
                visited.add(i)
                if answer[i] > 0:
                    a = max(a, answer[i])
                    continue
                else:
                    a = max(a, nums[i])
                for j in graph[i]:
                    if j not in visited:
                        queue.append(j)
            return a
        for i in range(n):
            answer[i] = bfs(i)
        return answer

    # based on hints
    # unable to jump forward/backward in connected component
    def maxValue_fails(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftMaximums = [nums[0]]
        for i in range(1,n):
            leftMaximums.append(max(nums[i], leftMaximums[-1]))
        rightMinimums = [nums[-1]]
        for i in range(n-2,-1,-1):
            rightMinimums.append(min(nums[i], rightMinimums[-1]))
        rightMinimums = rightMinimums[::-1]
        answer = []
        for i in range(n):
            a = nums[i]
            # detect if cut in connected components
            if leftMaximums[i] > rightMinimums[i]:
                a = leftMaximums[i]
            answer.append(a)
        return answer

    # based on LeetCode editorial
    # https://leetcode.com/problems/jump-game-ix/editorial/?envType=daily-question&envId=2026-05-07
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        # [value, index]
        prevMax = [(0,0)] * n
        # precalculate the maximum previous value and index
        value,index = -float('inf'), -1
        for i,j in enumerate(nums):
            if j > value:
                value = j
                index = i
            prevMax[i] = (value,index)
        # subdivide array into smaller partitions
        # [left .. right]
        # left is derived from precalculated maximums array
        # right is passed in along with the information of bigger partition
        def process(rightIndex:int, rightMin:float, rightMax:float) -> None:
            # get the left bound
            leftMax, leftIndex = prevMax[rightIndex]
            # get maximum value in this partition
            currMax = leftMax if leftMax <= rightMin else rightMax
            newRightMin = min(leftMax, rightMin)
            # update answer for this partition
            for i in range(leftIndex,rightIndex+1):
                answer[i] = currMax
                newRightMin = min(newRightMin, nums[i])
            # unable to partition left
            if leftIndex == 0:
                return
            # sub partition to the left
            process(leftIndex-1, newRightMin, currMax)
            return
        process(n-1, float('inf'), 0)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,3]
        o = [2,2,3]
        self.assertEqual(s.maxValue(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3,1]
        o = [3,3,3]
        self.assertEqual(s.maxValue(i), o)

    def test_three(self):
        s = Solution()
        i = [1] * (10**5)
        o = [1] * (10**5)
        # self.assertEqual(s.maxValue(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)