from bank_accounts import *

Herway = BankAccount(1000, "Herway")

Mok = BankAccount(1000, "Mok")

print(Herway.getBalance())
print(Mok.getBalance())

Herway.deposit(1000)
Herway.withdraw(20000)

Herway.transfer(1000, Mok)

T = InterestRewardsAcct(1000, "T")

T.deposit(100)
print(Mok.getBalance())

T.transfer(1000, Mok)

print(Mok.getBalance())

D = SavingAcct(1000, "D")
D.deposit(1000)
D.withdraw(2050)
