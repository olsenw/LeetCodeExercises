# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Write a program that will automate all the incoming transactions (transfer,
deposit, and withdraw). The bank has n accounts numbered from 1 to n. The
initial balance of each account is stored in a 0-indexed integer array balance,
with the (i + 1)^th account having an initial balance of balance[i].

Execute all the valid transactions. A transaction is valid if:
* The given account number(s) are between 1 and n, and
* The amount of money withdrawn or transferred from is less than or equal to the
  balance of the account.

Implement the Bank class:
'''
class Bank:
    '''
    Initializes the object with the 0-indexed integer array balance.
    '''
    def __init__(self, balance: List[int]):
        self.balances = [0] + balance

    def account(self, account: int) -> int:
        if 0 < account < len(self.balances):
            return self.balances[account]
        return -1
    
    '''
    Transfers money dollars from the account numbered account1 to the account
    numbered account2. Return true if the transaction was successful, false
    otherwise.
    '''
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        a = self.account(account1)
        b = self.account(account2)
        if a == -1 or b == -1:
            return False
        if a < money:
            return False
        self.balances[account1] -= money
        self.balances[account2] += money
        return True

    '''
    Deposit money dollars into the account numbered account. Return true if the
    transaction was successful, false otherwise.
    '''
    def deposit(self, account: int, money: int) -> bool:
        a = self.account(account)
        if a == -1:
            return False
        self.balances[account] += money
        return True

    '''
    Withdraw money dollars from the account numbered account. Return true if the
    transaction was successful, false otherwise.
    '''
    def withdraw(self, account: int, money: int) -> bool:
        a = self.account(account)
        if a < money:
            return False
        self.balances[account] -= money
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Bank([10, 100, 20, 50, 30])
        self.assertEqual(s.withdraw(3,10), True)
        self.assertEqual(s.transfer(5, 1, 10), True)
        self.assertEqual(s.deposit(5, 20), True)
        self.assertEqual(s.transfer(3, 14, 15), False)
        self.assertEqual(s.withdraw(10, 50), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)