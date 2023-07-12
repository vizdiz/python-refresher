import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_successful_withdrawal(self):
        user_one = BankAccount(153.43, "Vismay", 119107)
        user_two = BankAccount(0.99, "Vihaan", 119107)

        user_one.withdraw(45.44)
        self.assertAlmostEquals(user_one.balance, 107.99)

        self.assertRaises(ValueError, user_two.withdraw, 1.00)

    def test_deposit(self):
        user = BankAccount(153.43, "Vismay", 119107)
        user.deposit(98.57)

        self.assertRaises(ValueError, user.deposit, -109829.98)
        self.assertAlmostEquals(user.balance, 252.00)

    def test_print_balance(self):
        user = BankAccount(153.43, "Vismay", 119107)
        self.assertIsNone(user.print_balance())


if __name__ == "__main__":
    unittest.main()
