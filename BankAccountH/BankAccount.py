from bah_exceptions import InSufficientBalance

class BankAccount:
    """
    BankAccount class is the base class for differnt types of bank accounts.
    """

    def __init__(self, account_number, account_holder):
        """
        constructor for BankAccount. Takes account number and holder name.
        :param account_number: account number
        :type account_number: int
        :param account_holder: name on the account
        :type account_holder: str
        """
        if type(account_number) != int or type(account_holder) != str:
            raise ValueError(f"Invalid account number {account_number} or account holder {account_holder}")
        if account_number is None or account_holder is None:
            raise ValueError(f"account number {account_number} or account holder {account_holder} cannot be None")
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """
        Deposits the amount in bank account
        :param amount: amount to deposit
        :type amount: int
        :return: remaining balance
        :rtype: int
        """
        self.validate_amount(amount)
        self.balance += amount
        print(f"New balance after depositing {amount} is {self.balance}")
        return self.balance

    def withdraw(self, amount):
        """
        Withdraw the amount
        :param amount: amount to withdraw
        :type amount: int
        :return: remaining balance
        :rtype: int
        """
        self.validate_amount(amount)
        if self.balance - amount < 0:
            raise InSufficientBalance(f"cannot withdraw {amount} please choose an amount lower than {self.balance}")
        self.balance -= amount
        print(f"New balance after depositing {amount} is {self.balance}")
        return self.balance

    def validate_amount(self, amount):
        """
        Validates the amount given before withdraw or deposit
        :param amount: amount given
        :type amount: int
        :return: None
        :rtype: None
        :raises ValueError if amount is invalid
        """
        if type(amount) != int:
            raise ValueError("only round numbers can be deposited")
        if amount is None:
            raise ValueError("amount cannot be None")
        if amount < 0:
            raise ValueError("Cannot deposit amount less than zero")
