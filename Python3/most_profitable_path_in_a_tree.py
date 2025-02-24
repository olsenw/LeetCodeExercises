# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at
    node 0. Given a 2D integer array edges of length n-1 where
    edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi
    in the three.

    At every node i, there is a gate. Also given is an array of even integers
    amount, where amount[i] represents:
    * the price needed to open the gate at node i, if amount[i] is negative, of,
    * the cash reward obtained on opening the gate at node i, otherwise.

    The game goes on as follows:
    * Initially, Alice is at node 0 and Bob is at node bob.
    * At every second, Alice and Bob each move to an adjacent node. Alice moves
      towards some leaf node, while Bob moves towards node 0.
    * For every node along their path, Alice and Bob either spend money to open
      the gate at that node, or accept the reward. Note that:
      * If the gate is already open, no price will be required, nor will there
        there be any cash reward.
      * If Alice and Bob reach the node simultaneously, they share the
        price/reward for opening the gate there in other words, if the price to
        open the gate is c, then both Alice and Bob pay c / 2 each. Similarly,
        if the reward at the gate is c, both of them receive c / 2 each.
    * If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches
      node 0, he stops moving. Note that these events are independent of each
      other.
    
    Return the maximum net income Alice can have if she travels towards the
    optimal leaf node.
    '''
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        tree = {i:[[],-1,0] for i in range(len(edges) + 1)}
        tree[-1] = [[],-1,0]
        for a,b in edges:
            tree[a][0].append(b)
            tree[b][0].append(a)
        def bobdfs(node:int, source:int) -> bool:
            tree[node][1] = tree[source][1] + 1
            if node == 0:
                return True
            for n in tree[node][0]:
                if n != source and bobdfs(n, node):
                    return True
            tree[node][1] = -1
            return False
        bobdfs(bob, -1)
        def alice(node:int,source:int,depth:int)->int:
            tree[node][2] = tree[source][2]
            if tree[node][1] == -1 or depth < tree[node][1]:
                tree[node][2] += amount[node]
            elif depth == tree[node][1]:
                tree[node][2] += amount[node] // 2
            if source != -1 and len(tree[node][0]) == 1:
                return tree[node][2]
            answer = -float('inf')
            for n in tree[node][0]:
                if n != source:
                    answer = max(answer, alice(n, node, depth + 1))
            return answer
        return alice(0,-1,0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1],[1,2],[1,3],[3,4]]
        j = 3
        k = [-2,4,2,-4,6]
        o = 6
        self.assertEqual(s.mostProfitablePath(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [[0,1]]
        j = 1
        k = [-7280,2350]
        o = -7280
        self.assertEqual(s.mostProfitablePath(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [[0,1],[1,2],[2,3]]
        j = 3
        k = [-5644,-6018,1188,-8502]
        o = -11662
        self.assertEqual(s.mostProfitablePath(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)