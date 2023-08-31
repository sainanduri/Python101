from BankAccount import BankAccount
from bah_exceptions import UnsupportedTimePeriod


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        """
        constructor for SavingsBankAccount. Takes account number and holder name.
        :param account_number:
        :type account_number:
        :param account_holder:
        :type account_holder:
        :param interest_rate:
        :type interest_rate:
        """
        super().__init__(account_number=account_number, account_holder=account_holder)
        if interest_rate < 0:
            raise ValueError(f"Invalid interest rate {interest_rate}")
        self.interest_rate = interest_rate

    def add_interest(self, time):
        """
        Adds interest based on number of years
        :param time: time in years
        :type time: int
        :return: balance
        :rtype: int
        :return interest
        :rtype int
        """
        if time is None or time < 0:
            raise ValueError("time cannot be None or Negative")
        if type(time) != int:
            raise UnsupportedTimePeriod("time period can only be round numbers")
        # I = PTR/100
        interest_amount = (self.balance * time * self.interest_rate) // 100
        self.balance += interest_amount
        print(f"Interest Amount:{interest_amount}, Balance:{self.balance}")
        return self.balance, interest_amount
