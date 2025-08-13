# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
There is a supermarket that is frequented by many customers. The products
sold at the supermarket are represented as two parallel integer arrays
products and prices, where the ith product has an ID of products[i] and a
price of prices[i].

When a customer is paying, their bill is represented as two parallel integer
arrays product and amount, where the jth product they purchased has an ID of
product[j] and an amount[j] is how much of the product they bought. Their
subtotal is calculated as the sum of each
amount[j] * (price of the jth product).

The supermarket decided to have a sale. Every nth customer paying for their
groceries will be give a percentage discount. The discount amount is given
by discount, where they will be given discount percent off their subtotal.
More formally, if their subtotal is bill, then they would actually pay
bill * ((100 - discount) / 100)

Implement the Cashier class:
'''
class Cashier:
    '''
    Initializes the object with n, the discount, and the products and their
    prices.
    '''
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.c = 0
        self.discount = (100 - discount) / 100
        self.products = {i:j for i,j in zip(products, prices)}

    '''
    Returns the final total of the bill with the discount applied (if any).
    Answers within 10^-5 of the actual value will be accepted.
    '''
    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = sum(self.products[i] * j for i,j in zip(product, amount))
        self.c += 1
        if self.c == self.n:
            self.c = 0
            bill *= self.discount
        return bill

class UnitTesting(unittest.TestCase):
    def test_one(self):
        i = 3
        j = 50
        k = [1,2,3,4,5,6,7]
        l = [100,200,300,400,300,200,100]
        s = Cashier(i,j,k,l)
        self.assertEqual(s.getBill([1,2],[1,2]), 500.0)
        self.assertEqual(s.getBill([3,7],[10,10]), 4000.0)
        self.assertEqual(s.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]), 800.0)
        self.assertEqual(s.getBill([4],[10]), 4000.0)
        self.assertEqual(s.getBill([7,3],[10,10]), 4000.0)
        self.assertEqual(s.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]), 7350.0)
        self.assertEqual(s.getBill([2,3,5],[5,3,2]), 2500.0)


if __name__ == '__main__':
    unittest.main(verbosity=2)