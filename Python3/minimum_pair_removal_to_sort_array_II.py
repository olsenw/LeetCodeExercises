# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums, perform the following operation any number of times:
    * Select the adjacent pair with the minimum sum in nums. If multiple such
      pairs exist, choose the leftmost one.
    * Replace the pair with their sum.

    Return the minimum number of operations needed to make the array
    non-decreasing.

    An array is said to be non-decreasing if each element is greater than or
    equal to its previous element (if it exists).
    '''
    # based on hints
    def minimumPairRemoval_incomplete(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        m = {i:[i-1 if i > 0 else 0, i+1 if i < n-1 else n-1] for i in range(n)}
        r = set()
        h = [(nums[i] + nums[i+1], i) for i in range(n-1)]
        heapq.heapify(h)
        while any(nums[m[i][0]] > nums[m[i][1]] for i in m):
            answer += 1
            v,i = heapq.heappop(h)
            while i in r:
                v,i = heapq.heappop(h)
            nums[i] = v
            iNext = m[i][1]
            r.add(iNext)
            iNext = m[iNext][1]
            if iNext in r:
                m[i][1] = i
            else:
                m[iNext][0] = i
                heapq.heappush(h, nums)
            pass
        return answer

    # small issue with how the heap is sorted and indices of new nodes
    # make use of new integer values for inserted nodes... which can cause issues with heap if old "right" node has earlier index then new "left" node
    # would also TLE if ran to completion O(n^2)... see the any in the while
    def minimumPairRemoval_incorrect(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        m = {i:[nums[i], None if i == 0 else i-1, None if i + 1 == n else i + 1] for i in range(n)}
        r = set()
        h = [(nums[i] + nums[i+1], i, i+1) for i in range(n-1)]
        heapq.heapify(h)
        while any(m[i][0] > m[m[i][2]][0] for i in m if i not in r and m[i][2] is not None):
            answer += 1
            # get node i
            v,curr,currNext = heapq.heappop(h)
            while curr in r or currNext in r:
                v,curr,currNext = heapq.heappop(h)
            # node i - 1
            prev = m[curr][1]
            # node i + 1
            # currNext = m[curr][2]
            # node i + 2
            final = m[currNext][2] if currNext else None
            # replace node i and i + 1 with new node
            n = len(m)
            m[n] = [v, prev, final]
            # remove curr nodes from consideration
            r.add(curr)
            r.add(currNext)
            # update priority queue and list
            if prev is not None:
                m[prev][2] = n
                heapq.heappush(h, (m[prev][0] + m[n][0], prev, n))
            if final is not None:
                m[final][1] = n
                heapq.heappush(h, (m[final][0] + m[n][0], n, final))
        return answer

    # base on Leetcode editorial
    # https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/editorial/?envType=daily-question&envId=2026-01-23
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # definition of a node in a doubly linked list
        class Node:
            def __init__(self, value:int, left):
                self.value = value
                self.left = left
                self.prev = None
                self.next = None
        # definition of an item in the priority queue
        class PQItem:
            def __init__(self, first, second, cost):
                self.first = first
                self.second = second
                self.cost = cost
            def __lt__(self, other):
                if self.cost == other.cost:
                    return self.first.left < other.first.left
                return self.cost < other.cost
        # priority queue for pairs to remove
        pq = []
        # head of double linked list
        head = Node(nums[0],0)
        # current element in double linked list
        current = head
        # lazy deletion, used to determine if dirty data in priority queue
        merged = [False] * len(nums)
        # number of pairs where nums[i] > nums[i+1]
        decrease_count = 0
        # counter for number of operations needed
        answer = 0
        
        # build the list
        for i in range(1, len(nums)):
            node = Node(nums[i], i)
            current.next = node
            node.prev = current
            heapq.heappush(pq, PQItem(current, node, current.value + node.value))
            if nums[i-1] > nums[i]:
                decrease_count += 1
            current = node

        # apply operation until no decreasing items remain
        while decrease_count:
            item = heapq.heappop(pq)
            first, second, cost = item.first, item.second, item.cost

            # determine if dirty data and should skip
            # ie already processed node
            if merged[first.left] or merged[second.left] or first.value + second.value != cost:
                continue

            answer += 1

            if first.value > second.value:
                decrease_count -= 1

            prev_node = first.prev
            next_node = second.next
            first.next = next_node
            if prev_node:
                if prev_node.value > first.value and prev_node.value <= cost:
                    decrease_count -= 1
                elif prev_node.value <= first.value and prev_node.value > cost:
                    decrease_count += 1
                heapq.heappush(pq, PQItem(prev_node, first, prev_node.value + cost))
            if next_node:
                next_node.prev = first
                if second.value > next_node.value and cost <= next_node.value:
                    decrease_count -= 1
                elif second.value <= next_node.value and cost > next_node.value:
                    decrease_count += 1
                heapq.heappush(pq, PQItem(first, next_node, cost + next_node.value))
            
            first.value = cost
            merged[second.left] = True

        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,2,3,1]
        o = 2
        self.assertEqual(s.minimumPairRemoval(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,2]
        o = 0
        self.assertEqual(s.minimumPairRemoval(i), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = 0
        self.assertEqual(s.minimumPairRemoval(i), o)

    def test_four(self):
        s = Solution()
        i = [2,1]
        o = 1
        self.assertEqual(s.minimumPairRemoval(i), o)

    def test_five(self):
        s = Solution()
        i = [3,-3,-2,2,2,0,3,0,1,0,3,-2]
        o = 11
        self.assertEqual(s.minimumPairRemoval(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)