# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    '''
    Given a data structure of employee information, including the employee's
    unique ID, importance value, and the direct subordinates' IDs.

    Given an array of employees employees where:
    * employees[i].id is the ID of the ith employee.
    * employees[i].importance is the importance value of the ith employee.
    * employees[i].subordinates is a list of the IDs of the direct subordinates
      of the ith employee.
    
    Given an integer id that represents an employee's ID, return the total
    importance value value of this employee and all their direct and indirect
    subordinates.
    '''
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {e.id: e for e in employees}
        def dfs(node: Employee) -> int:
            return node.importance + sum(dfs(d[i]) for i in node.subordinates)
        return dfs(d[id])

    def getImportance_without_class(self, employees: List['Employee'], id: int) -> int:
        d = {e[0]: e for e in employees}
        def dfs(node: int) -> int:
            return d[node][1] + sum(dfs(i) for i in d[node][2])
        return dfs(id)
    
class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [Employee(*e) for e in [[1,5,[2,3]],[2,3,[]],[3,3,[]]]]
        j = 1
        o = 11
        self.assertEqual(s.getImportance(i,j), o)

    def test_two(self):
        s = Solution()
        i = [Employee(*e) for e in [[1,2,[5]],[5,-3,[]]]]
        j = 5
        o = -3
        self.assertEqual(s.getImportance(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)