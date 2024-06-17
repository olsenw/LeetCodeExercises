# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two arrays of strings list1 and list2, find the common strings with
    the least index sum.

    A common string is a string that appears in both list1 and list2.

    A common string with the least index sum is a common string such that if it
    appeared at list1[i] and list2[j] then i + j should be the minimum value
    among all the other common strings.

    Return all the common strings with the least index sum. Return the answer in
    any order.
    '''
    def findRestaurant_fails(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {i:j for j,i in enumerate(list1)}
        answer = []
        t = 2001
        for j,i in enumerate(list2):
            if i in d:
                answer.append(i)
                t = d[i] + j
                break
        if j+1 < len(list2) and list2[j+1] in d and t == d[list2[j+1]] + j + 1:
            answer.append(list2[j+1])
        return answer

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {i:j for j,i in enumerate(list1)}
        a = {}
        for j,i in enumerate(list2):
            if i in d:
                a[i] = d[i] + j
        answer = []
        target = 20001
        for i in a:
            if a[i] < target:
                target = a[i]
                answer = [i]
            elif a[i] == target:
                answer.append(i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["Shogun","Tapioca Express","Burger King","KFC"]
        j = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
        o = ["Shogun"]
        self.assertEqual(s.findRestaurant(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["Shogun","Tapioca Express","Burger King","KFC"]
        j = ["KFC","Shogun","Burger King"]
        o = ["Shogun"]
        self.assertEqual(s.findRestaurant(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["happy","sad","good"]
        j = ["sad","happy","good"]
        o = ["sad","happy"]
        self.assertEqual(s.findRestaurant(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)