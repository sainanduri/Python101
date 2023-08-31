from BankAccount import BankAccount
from bah_exceptions import InSufficientBalance


class CheckinAccount(BankAccount):
    def __init__(self, account_number, account_holder, overdraft_limit):
        super().__init__(account_number=account_number, account_holder=account_holder)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """

        :param amount:
        :type amount:
        :return:
        :rtype:
        """
        self.validate_amount(amount)
        if self.balance + self.overdraft_limit < amount:
            raise InSufficientBalance(f"cannot withdraw {amount} please choose an amount lower than"
                                      f" {self.balance + self.overdraft_limit}")
        self.balance -= amount
        print(f"New balance after depositing {amount} is {self.balance}")
        return self.balance
