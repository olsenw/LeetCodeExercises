# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from collections import defaultdict, deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n indicating there are n people numbered from 0 to n - 1.
    Also given a 0-indexed 2D integer array meetings where
    meetings[i] = xi, yi, timei] indicates that person xi and person yi have a
    meeting at timei. A person may attend multiple meetings at the same time.
    Finally, given an integer firstPerson.

    Person 0 has a secret and initially shares the secret with a person
    firstPerson at time 0. This secret is then shared every time a meeting takes
    place with a person that has the secret. More formally, for every meeting,
    if a person xi has the secret at timei, then they share the secret with
    person yi, and vice versa.

    The secrets are shared instantaneously. That is a person may receive the
    secret and share it with people in other meetings within the same time
    frame.

    Return a list of all the people that have the secret after all the meetings
    have taken place. The answer may be returned in any order.
    '''
    def findAllPeople_memory_exceeded(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: (x[2],x[0],x[1]))
        people = {i:[] for i in range(n)}
        for x,(i,j,k) in enumerate(meetings):
        # for i,j,k in meetings:
            people[i].append(x)
            # people[i].append([k,j])
            people[j].append(x)
            # people[j].append([k,i])
        visited = set()
        def bfs(p: int) -> Set[int]:
            answer = set([p])
            q = deque(people[p])
            while q:
                i = q.popleft()
                if i in visited:
                    continue
                visited.add(i)
                i = meetings[i]
                answer.add(i[0])
                answer.add(i[1])
                j = bisect.bisect_left(people[i[0]], i[2], key=lambda x:meetings[x][2])
                k = bisect.bisect_left(people[i[1]], i[2], key=lambda x:meetings[x][2])
                q.extend(people[i[0]][j:])
                q.extend(people[i[1]][k:])
            return answer
        return bfs(0).union(bfs(firstPerson))

    def findAllPeople_time_exceeded(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: (x[2],x[0],x[1]))
        people = {i:[] for i in range(n)}
        for x,(i,j,k) in enumerate(meetings):
        # for i,j,k in meetings:
            people[i].append(x)
            # people[i].append([k,j])
            people[j].append(x)
            # people[j].append([k,i])
        visited = set()
        def bfs(p: int) -> Set[int]:
            answer = set([p])
            q = set(people[p])
            while q:
                i = q.pop()
                if i in visited:
                    continue
                visited.add(i)
                i = meetings[i]
                answer.add(i[0])
                answer.add(i[1])
                j = bisect.bisect_left(people[i[0]], i[2], key=lambda x:meetings[x][2])
                for x in people[i[0]][j:]:
                    if x not in visited or x not in q:
                        q.add(x)
                k = bisect.bisect_left(people[i[1]], i[2], key=lambda x:meetings[x][2])
                for x in people[i[1]][k:]:
                    if x not in visited or x not in q:
                        q.add(x)
            return answer
        return bfs(0).union(bfs(firstPerson))

    # dumb, does not handle telling at the same time
    def findAllPeople_fails(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: (x[2],x[0],x[1]))
        secret = {0:0, firstPerson:0}
        for i,j,k in meetings:
            pass
            if i in secret or j in secret:
                secret[i] = k
                secret[j] = k
        return list(secret.keys())

    # based on hints
    # fails because at a given time there can be disjoint sets of meetings
    # people know/learning the secret and those who don't/won't 
    def findAllPeople_fails(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(set)
        # graph[0].add(0)
        # graph[0].add(firstPerson)
        for i,j,k in meetings:
            graph[k].add(i)
            graph[k].add(j)
        answer = {0, firstPerson}
        for t in sorted(graph.keys()):
            if any(i in answer for i in graph[t]):
                answer.update(graph[t])
        return list(answer)

    # bfs
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # when is this person last seen
        people = {i:-1 for i in range(n)}
        people[0] = 0
        people[firstPerson] = 0 
        # (person, time) -> [(person, time),...]
        graph = defaultdict(set)
        graph[(0,0)].add((firstPerson,0))
        # graph[(firstPerson,0)].append((0,0))
        for i,j,k in sorted(meetings, key=lambda x:x[2]):
            # i,j = min(i,j), max(i,j)
            if i in people and k > people[i]:
                graph[(i,people[i])].add((i,k))
            people[i] = max(k,people[i])
            if j in people and k > people[j]:
                graph[(j,people[j])].add((j,k))
            people[j] = max(k,people[j])
            graph[(i,k)].add((j,k))            
            graph[(j,k)].add((i,k))  
        visited = set()
        answer = set()
        q = set([(0,0)])
        while q:
            i = q.pop()
            if i in visited:
                continue
            visited.add(i)
            answer.add(i[0])
            q.update(graph[i])
        return list(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 6
        j = [[1,2,5],[2,3,8],[1,5,10]]
        k = 1
        o = [0,1,2,3,5]
        self.assertEqual(sorted(s.findAllPeople(i,j,k)), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [[3,1,3],[1,2,2],[0,3,3]]
        k = 3
        o = [0,1,3]
        self.assertEqual(sorted(s.findAllPeople(i,j,k)), o)

    def test_three(self):
        s = Solution()
        i = 5
        j = [[3,4,2],[1,2,1],[2,3,1]]
        k = 1
        o = [0,1,2,3,4]
        self.assertEqual(sorted(s.findAllPeople(i,j,k)), o)

    def test_four(self):
        s = Solution()
        i = 5
        j = [[1,2,2],[2,3,2],[3,4,2]]
        k = 4
        o = [0,1,2,3,4]
        self.assertEqual(sorted(s.findAllPeople(i,j,k)), o)

    def test_five(self):
        s = Solution()
        i = 5
        j = [[1,2,2],[3,4,2]]
        k = 4
        o = [0,3,4]
        self.assertEqual(sorted(s.findAllPeople(i,j,k)), o)


if __name__ == '__main__':
    unittest.main(verbosity=2)