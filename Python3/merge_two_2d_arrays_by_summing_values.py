# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two 2D integer arrays nums1 and nums2.
    * nums1[i] = [idi, vali] indicate that the number with the id idi has a
      value equal to vali.
    * nums2[i] = [idi, vali] indicate that the number with the id idi has a
      value equal to vali

    Each array contains unique ids and is stored in ascending order by id.

    Merge the two arrays into one array that is sorted in ascending order by i,
    respecting the following conditions:
    * Only ids that appear in at least one of the two arrays should be included
      in the resulting array.
    * Each id should be included only once and its value should be the sum of
      the values of this id in the two arrays. If the id does not exist in one
      of the two arrays, then assume its value in that array to be 0.

    Return the resulting array. The returned array must be sorted in ascending
    order by id.
    '''
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        answer = []
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                answer.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                answer.append([nums1[i][0], nums1[i][1]])
                i += 1
            else:
                answer.append([nums2[j][0], nums2[j][1]])
                j += 1
        while i < len(nums1):
            answer.append([nums1[i][0], nums1[i][1]])
            i += 1
        while j < len(nums2):
            answer.append([nums2[j][0], nums2[j][1]])
            j += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,3],[4,5]]
        j = [[1,4],[3,2],[4,1]]
        o = [[1,6],[2,3],[3,2],[4,6]]
        self.assertEqual(s.mergeArrays(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[2,4],[3,6],[5,5]]
        j = [[1,3],[4,3]]
        o = [[1,3],[2,4],[3,6],[4,3],[5,5]]
        self.assertEqual(s.mergeArrays(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[148,597],[165,623],[306,359],[349,566],[403,646],[420,381],[566,543],[730,209],[757,875],[788,208],[932,695]]
        j = [[74,669],[87,399],[89,165],[99,749],[122,401],[138,16],[144,714],[148,206],[177,948],[211,653],[285,775],[309,289],[349,396],[386,831],[403,318],[405,119],[420,153],[468,433],[504,101],[566,128],[603,688],[618,628],[622,586],[641,46],[653,922],[672,772],[691,823],[693,900],[756,878],[757,952],[770,795],[806,118],[813,88],[919,501],[935,253],[982,385]]
        o = [[74,669],[87,399],[89,165],[99,749],[122,401],[138,16],[144,714],[148,803],[165,623],[177,948],[211,653],[285,775],[306,359],[309,289],[349,962],[386,831],[403,964],[405,119],[420,534],[468,433],[504,101],[566,671],[603,688],[618,628],[622,586],[641,46],[653,922],[672,772],[691,823],[693,900],[730,209],[756,878],[757,1827],[770,795],[788,208],[806,118],[813,88],[919,501],[932,695],[935,253],[982,385]]
        self.assertEqual(s.mergeArrays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)