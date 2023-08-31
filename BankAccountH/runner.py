from CheckinAccount import CheckinAccount
from SavingsAccount import SavingsAccount

savings = SavingsAccount(account_number=123456, account_holder="Vaishnavi", interest_rate=10)
checking = CheckinAccount(account_number=654321, account_holder="Bindu", overdraft_limit=500)

print(savings.deposit(500))
print(savings.add_interest(time=10))

checking.deposit(200)
print(checking.withdraw(100))
print(checking.withdraw(700))
