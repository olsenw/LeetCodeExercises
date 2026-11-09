# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

from sortedcontainers import SortedSet

class Solution:
    '''
    Given k servers numbered from 0 to k-1 that are being used to handle
    multiple requests simultaneously. Each server has infinite computational
    capacity but cannot handle more than one request at a time. The requests are
    assigned to servers according to a specific algorithm.
    * The ith (0-indexed) request arrives.
    * If all servers are busy, the request is dropped (not handled at all).
    * If the (i % k)th server is available, assign the request to that server.
    * Otherwise, assign the request to the next available server (wrapping
      around the list of servers and starting from 0 if necessary).
    
    Given a strictly increasing array arrival of positive integers where
    arrival[i] represents the arrival time of the ith request, and another array
    load, where load[i] represents the load of the ith request (the time it
    takes to complete). Find the busiest server(s). A server is considered
    busiest if it handled the most number of requests successfully among all the
    servers.

    Return a list containing the IDs (0-indexed) of the busiest server(s). The
    IDs may be returned in any order.
    '''
    # did it without hints, just the topic list
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        c = Counter()
        # available servers
        servers = SortedSet(range(2 * k))
        # (time complete, server id)
        processHeap = []
        for i,(a,b) in enumerate(zip(arrival, load)):
            pass
            while processHeap and processHeap[0][0] <= a:
                _, s = heapq.heappop(processHeap)
                servers.add(s)
                servers.add(s+k)
            s = servers.bisect_left(i % k)
            if s < len(servers):
                id = servers[s] % k
                c[id] += 1
                servers.remove(id)
                servers.remove(id+k)
                heapq.heappush(processHeap, (a+b, id))
            pass
        m = c.most_common(1)[0][1]
        return [i for i in c if c[i] == m]

    '''
    faster solutions make use circular array index calculation and min heaps
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [1,2,3,4,5]
        k = [5,2,3,3,3]
        o = [1]
        self.assertEqual(s.busiestServers(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [1,2,3,4]
        k = [1,2,1,2]
        o = [0]
        self.assertEqual(s.busiestServers(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = [1,2,3]
        k = [10,12,11]
        o = [0,1,2]
        self.assertEqual(s.busiestServers(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)