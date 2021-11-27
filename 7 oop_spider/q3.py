class BankAccount:
    interest_rate = 0.25

    def __init__(self, name, number, balance) -> None:
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if money > self.balance:
            print("取款失败")
        else:
            self.balance -= money

    def add_interest(self):
        self.balance += self.balance * self.interest_rate


class CreditAccount(BankAccount):
    credit_balance = 5000

    def __init__(self, name, number, balance) -> None:
        super().__init__(name, number, balance)

    def withdraw(self, money):
        if money > self.credit_balance:
            print("取款失败")
        else:
            self.credit_balance -= money


def main():
    ca = CreditAccount(1, 2, 3000)
    ca.withdraw(6000)


if __name__ == "__main__":
    main()