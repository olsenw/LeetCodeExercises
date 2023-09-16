# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a list of airline tickets where tickets[i] = [fromi, toi] represent
    the departure and the arrival airports of one flight. Reconstruct the
    itinerary in order and return it.

    All of the tickets belong to a man who departs from "JFK", thus, the
    itinerary must begin with "JFK". If there are multiple valid itineraries,
    return the itinerary that has the smallest lexical order when read as a
    single string.

    It is assumed that all the tickets form at least one valid itinerary. Each
    ticket can only be used once.
    '''
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for i,(a,b) in enumerate(tickets):
            graph[a].append((b,i))
        for g in graph:
            graph[g] = sorted(graph[g])
        answer = []
        visited = set()
        def dfs(node):
            answer.append(node)
            if len(answer) == len(tickets)+1:
                return True
            for i,j in graph[node]:
                if j in visited:
                    continue
                visited.add(j)
                if dfs(i):
                    return True
                visited.remove(j)
            answer.pop()
            return False
        dfs("JFK")
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
        o = ["JFK","MUC","LHR","SFO","SJC"]
        self.assertEqual(s.findItinerary(i), o)

    def test_two(self):
        s = Solution()
        i = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        o = ["JFK","ATL","JFK","SFO","ATL","SFO"]
        self.assertEqual(s.findItinerary(i), o)

    def test_three(self):
        s = Solution()
        i = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
        o = ["JFK","NRT","JFK","KUL"]
        self.assertEqual(s.findItinerary(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)