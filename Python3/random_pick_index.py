# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import random
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Given an integer array nums with possible duplicates, randomly output the index
of a given target number. It is assumed that the given target number exists in
the array.

Implement the Solution class:
'''
class Solution:
    '''
    Initializes the object with the array nums.
    '''
    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for i,j in enumerate(nums):
            self.indices[j].append(i)
        return

    '''
    Picks a random index i from nums where nums[i] == target. If there are
    multiple valid i's, then each index should have an equal probability of
    returning.
    '''
    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])

class UnitTesting(unittest.TestCase):
    '''
    Tested online due to random output of answers
    '''
    pass