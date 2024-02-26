class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initBalance, owner):
        self.balance = initBalance
        self.owner = owner
        print(
            f'Bank account for {self.owner} created with balance of "${self.balance}"'
        )

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited into account for {self.owner}")
        print(f"New balance is ${self.balance}")

    def withdraw(self, amount):
        try:
            self.viableTransfer(amount)
            self.balance -= amount
            print(f"${amount} withdrawn from account for {self.owner}")
            print(f"New balance is ${self.balance}")
        except BalanceException as e:
            print(e)

    def transfer(self, amount, recipient):
        try:
            self.viableTransfer(amount)
            self.balance -= amount
            recipient.balance += amount
            print(f"${amount} transferred to account for {recipient.owner}")
            print(f"{recipient.owner} New balance is ${self.balance}")
        except BalanceException as e:
            print(e)

    def viableTransfer(self, amount):
        if amount <= self.balance:
            return
        else:
            raise BalanceException(
                f"Account {self.owner} insufficient funds, {self.balance} available, {amount} requested"
            )


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("Deposit of ${amount} has been made to account for {self.owner}")
        print(f"New balance is ${self.balance}")


class SavingAcct(InterestRewardsAcct):
    def __init__(self, initBalance, owner):
        super().__init__(initBalance, owner)
        self.fee = 0.005

    def withdraw(self, amount):
        try:
            self.viableTransfer(amount * self.fee + amount)
            self.balance -= amount * self.fee + amount
            print(f"${amount} withdrawn from account for {self.owner}")
            print(f"New balance is ${self.balance}")
        except BalanceException as e:
            print(e)
