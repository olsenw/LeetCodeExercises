# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxes i,
    numberOfUnitsPerBox i]:
    * numberOfBoxes i is the number of boxes of type i.
    * numberOfUnitsPerBox is the number of units in each box of the type
      i.

    Also given an integer truckSize, which is the maximum number of
    boxes that can be put on the truck. Any box may be put on the truck
    as long as the number of boxes does not exceed truckSize.

    Return the maximum total number of units that can be put on the
    truck.
    '''
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # boxTypes.sort(key=lambda x: (-x[1], x[0]))
        boxTypes.sort(key=lambda x: -x[1])
        units = 0
        for b, u in boxTypes:
            if truckSize > 0:
                t = min(truckSize, b)
                units += u * t
                truckSize -= t
            else:
                break
        return units

    def maximumUnitsBetter(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        units = 0
        for b, u in boxTypes:
            if truckSize >= b:
                units += u * b
                truckSize -= b
            else:
                units += u * truckSize
                break
        return units

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,3],[2,2],[3,1]]
        j = 4
        o = 8
        self.assertEqual(s.maximumUnits(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[5,10],[2,5],[4,7],[3,9]]
        j = 10
        o = 91
        self.assertEqual(s.maximumUnits(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)