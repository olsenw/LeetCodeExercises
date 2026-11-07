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
    Given two 0-indexed integer arrays servers and tasks of lengths n and m
    respectively. servers[i] is the weight of the ith server, and tasks[j] is
    the time needed to process the jth task in seconds.

    Tasks are assigned to the servers using a task queue. Initially, all servers
    are free, and the queue is empty.

    At second j, the jth task is inserted into the queue (starting with the 0th
    task inserted at second 0). As long as there are free servers and the queue
    is not empty, the task in the front of the queue will be assigned to a free
    server with the smallest weight, and in case of a tie, it is assigned to a
    free server with the smallest index.

    If there are no free servers and the queue is not empty, wait until a server
    becomes free and immediately assign the next task. If multiple servers
    become free at the same time, then multiple tasks from the queue will be
    assigned in order of insertion following the weight and index priorities
    above.

    A server that is assigned task j at second t will be free again at second
    t + tasks[j].

    Build an array ans of length m, where ans[j] is the index of the server the
    jth task will be assigned to.

    Return the array ans.
    '''
    def assignTasks_incomplete(self, servers: list[int], tasks: list[int]) -> list[int]:
        m = len(servers)
        time = 0
        tasks.append(5 * 10**5)
        # server wight, server index
        availableServer = [(j,i) for i,j in servers]
        heapq.heapify(availableServer)
        # time task completion, task index, server wight, server index
        processServer = []
        # task time, task index
        taskQueue = deque()
        answer = []
        for i,j in enumerate(tasks):
            taskQueue.append((j,i))
            while processServer and processServer[0][0]:
                a,b,c = heapq.heappop(processServer)
                heapq.heappush(availableServer, (b,c))
            while availableServer and taskQueue:
                b,c = taskQueue.popleft()
                x,y = heapq.heappop(availableServer)
                heapq.heappush(processServer, ())
        return answer[:-1]

    # Note that this does not fill tasks when multiple queues available
    def assignTasks_brute_fails(self, servers: list[int], tasks: list[int]) -> list[int]:
        answer = []
        # weight, index
        idleHeap = [(j,i) for i,j in enumerate(servers)]
        heapq.heapify(idleHeap)
        # completion time, index
        busyHeap = []
        n = len(tasks)
        task = 0
        for t in range(5 * 10**5):
            while busyHeap and busyHeap[0][0] <= t:
                _, i = heapq.heappop(busyHeap)
                heapq.heappush(idleHeap, (servers[i], i))
            if idleHeap:
                _, i = heapq.heappop(idleHeap)
                answer.append(i)
                heapq.heappush(busyHeap, (t + tasks[task], i))
                task += 1
            if task == n:
                break
        return answer

    # my issues was when processing time
    # it is important to process time at start to fully release all queued items
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        answer = []
        availableServer = [(j,i) for i,j in enumerate(servers)]
        heapq.heapify(availableServer)
        processingServer = []
        time = 0
        for i,j in enumerate(tasks):
            time = max(time,i)
            pass
            while processingServer and processingServer[0][0] <= time:
                a,b,c = heapq.heappop(processingServer)
                heapq.heappush(availableServer, (b,c))
            if not availableServer:
                time,b,c = heapq.heappop(processingServer)
                heapq.heappush(processingServer, (time + j, b, c))
                answer.append(c)
            else:
                b,c = heapq.heappop(availableServer)
                heapq.heappush(processingServer, (time + j, b, c))
                answer.append(c)
            # time += 1
        return answer

    # attempt to adjust my answer to match editorial answer
    def assignTasks_works(self, servers: list[int], tasks: list[int]) -> list[int]:
        answer = []
        availableServer = [(j,i) for i,j in enumerate(servers)]
        heapq.heapify(availableServer)
        processingServer = []
        time = 0
        for i,j in enumerate(tasks):
            time = max(time, i)
            pass
            while processingServer and processingServer[0][0] <= time:
                a,b,c = heapq.heappop(processingServer)
                heapq.heappush(availableServer, (b,c))
            if not availableServer:
                time = processingServer[0][0]
                while processingServer and processingServer[0][0] <= time:
                    a,b,c = heapq.heappop(processingServer)
                    heapq.heappush(availableServer, (b,c))
            b,c = heapq.heappop(availableServer)
            heapq.heappush(processingServer, (time + j, b, c))
            answer.append(c)
            # time += 1
        return answer

    # based on LeetCode editorial
    # https://leetcode.com/problems/process-tasks-using-servers/?envType=daily-question&envId=2026-11-07
    # the difference was when time was updated
    # this fills tasks to queue when available
    def assignTasks_(self, servers: list[int], tasks: list[int]) -> list[int]:
        # time compete, server index
        busy = []
        # server weight, server index
        idle = [(j,i) for i,j in enumerate(servers)]
        heapq.heapify(idle)
        time = 0
        answer = []
        for i, task in enumerate(tasks):
            time = max(time, i)
            while busy and busy[0][0] <= time:
                _, idx = heapq.heappop(busy)
                heapq.heappush(idle, (servers[idx], idx))
            if not idle:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    _, idx = heapq.heappop(busy)
                    heapq.heappush(idle, (servers[idx], idx))
            _, idx = heapq.heappop(idle)
            answer.append(idx)
            heapq.heappush(busy, (time + task, idx))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,3,2]
        j = [1,2,3,2,1,2]
        o = [2,2,0,2,1,2]
        self.assertEqual(s.assignTasks(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5,1,4,3,2]
        j = [2,1,2,4,5,2,1]
        o = [1,4,1,4,1,3,2]
        self.assertEqual(s.assignTasks(i,j), o)

    def test_three(self):
        s = Solution()
        i = [338,890,301,532,284,930,426,616,919,267,571,140,716,859,980,469,628,490,195,664,925,652,503,301,917,563,82,947,910,451,366,190,253,516,503,721,889,964,506,914,986,718,520,328,341,765,922,139,911,578,86,435,824,321,942,215,147,985,619,865]
        j = [773,537,46,317,233,34,712,625,336,221,145,227,194,693,981,861,317,308,400,2,391,12,626,265,710,792,620,416,267,611,875,361,494,128,133,157,638,632,2,158,428,284,847,431,94,782,888,44,117,489,222,932,494,948,405,44,185,587,738,164,356,783,276,547,605,609,930,847,39,579,768,59,976,790,612,196,865,149,975,28,653,417,539,131,220,325,252,160,761,226,629,317,185,42,713,142,130,695,944,40,700,122,992,33,30,136,773,124,203,384,910,214,536,767,859,478,96,172,398,146,713,80,235,176,876,983,363,646,166,928,232,699,504,612,918,406,42,931,647,795,139,933,746,51,63,359,303,752,799,836,50,854,161,87,346,507,468,651,32,717,279,139,851,178,934,233,876,797,701,505,878,731,468,884,87,921,782,788,803,994,67,905,309,2,85,200,368,672,995,128,734,157,157,814,327,31,556,394,47,53,755,721,159,843]
        o = [26,50,47,11,56,31,18,55,32,9,4,2,23,53,43,0,44,30,6,51,29,51,15,17,22,34,38,33,42,3,25,10,49,51,7,58,16,21,19,31,19,12,41,35,45,52,13,59,47,36,1,28,48,39,24,8,46,20,5,54,27,37,14,57,40,59,8,45,4,51,47,7,58,4,31,23,54,7,9,56,2,46,56,1,17,42,11,30,12,44,14,32,7,10,23,1,29,27,6,10,33,24,19,10,35,30,35,10,17,49,50,36,29,1,48,44,7,11,24,57,42,30,10,55,3,20,38,15,7,46,32,21,40,16,59,30,53,17,18,22,51,11,53,36,57,26,5,36,56,55,31,34,57,7,52,37,31,10,0,51,41,2,32,25,0,7,49,47,13,14,24,57,28,4,45,43,39,38,8,2,44,45,29,25,25,12,54,5,44,30,27,23,26,7,33,58,41,25,52,40,58,9,52,40]
        self.assertEqual(s.assignTasks(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)