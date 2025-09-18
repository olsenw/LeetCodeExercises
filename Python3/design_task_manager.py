# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
There is a task management system that allows users to manage their tasks, each
associated with a priority. The system should efficiently handle adding,
modifying, executing, and removing tasks.

Implement the TaskManager class
'''
class TaskManager:
    '''
    Initializes the task manager with a list of user-task-priority triples. Each
    element in the input list is of the form [userId, taskId, priority], which
    adds a task to the specified user with the given priority.
    '''
    def __init__(self, tasks: List[List[int]]):
        self.taskPriority = dict()
        self.taskUser = dict()
        self.heap = []
        for i,j,k in tasks:
            self.add(i,j,k)

    '''
    Adds a task with the specified taskId and priority to the user with userId.
    It is guaranteed that taskId does not exist in the system.
    '''
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskPriority[taskId] = priority
        self.taskUser[taskId] = userId
        heapq.heappush(self.heap, (-priority, -taskId))

    '''
    Updates the priority of the existing taskId to newPriority. It is guaranteed
    that taskId exists in the system.
    '''
    def edit(self, taskId: int, newPriority: int) -> None:
        self.taskPriority[taskId] = newPriority
        heapq.heappush(self.heap, (-newPriority, -taskId))

    '''
    Removes the task identified by the taskId from the system. If it guaranteed
    that taskId exists in the system.
    '''
    def rmv(self, taskId: int) -> None:
        del self.taskPriority[taskId]
        del self.taskUser[taskId]

    '''
    Executes the task with the highest priority across all users. If there are
    multiple tasks with the same highest priority, execute the one with the
    highest taskId. After executing, the taskId is removed from the system.
    Return the userId associated with the executed task. If no tasks are
    available, return -1.
    '''
    def execTop(self) -> int:
        while self.heap:
            priority, taskId = heapq.heappop(self.heap)
            priority *= -1
            taskId *= -1
            if taskId in self.taskPriority and self.taskPriority[taskId] == priority:
                userId = self.taskUser[taskId]
                self.rmv(taskId)
                return userId
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
        s.add(4, 104, 5)
        s.edit(102, 8)
        self.assertEqual(s.execTop(), 3)
        s.rmv(101)
        s.add(5, 105, 15)
        self.assertEqual(s.execTop(), 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)