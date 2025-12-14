# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter, defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given the array orders, which represents the orders that customers have done
    in a restaurant. More specifically
    orders[i] = [customerNamei, tableNumberi, foodItemi] where customerNamei is
    the name of the customer, tableNumberi is the table customer sit at, and
    foodItemi is the item customer orders.

    Return the restaurant's "display table". The "display table" is a table
    whose row entries denote how many of each food item each table ordered. The
    first column is the table number and the remaining columns correspond to
    each food item in alphabetical order. The first row should be a header whose
    first column is "Table", followed by the names of the food items. Note that
    the customer names are not part of the table. Additionally, the rows should
    be sorted in numerically increasing order.
    '''
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food = set()
        tables = defaultdict(Counter)
        for name, table, order in orders:
            food.add(order)
            tables[int(table)][order] += 1
        answer = [["Table"]]
        food = sorted(food)
        for f in food:
            answer[0].append(f)
        for t in sorted(tables.keys()):
            answer.append([str(t)])
            for f in food:
                answer[-1].append(str(tables[t][f]))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
        o = [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
        self.assertEqual(s.displayTable(i), o)

    def test_two(self):
        s = Solution()
        i = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
        o = [["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]]
        self.assertEqual(s.displayTable(i), o)

    def test_three(self):
        s = Solution()
        i = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
        o = [["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]
        self.assertEqual(s.displayTable(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)