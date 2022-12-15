class BankAccount:
    def __init__(self, name: str, acc_num: str, balance: float):
        self.__name = name
        self.__acc_num = acc_num
        self.__balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()
        else:
            raise ValueError("Deposit needs be bigger than zero!!!")

    def withdraw(self, amount: float):
        if amount < self.__balance:
            self.__balance -= amount
            self.__service_charge()
        else:
            raise ValueError("You don't have that much!!!")

    def __service_charge(self):
        self.__balance -= self.__balance * 0.01

    @property
    def balance(self):
        return self.__balance


if __name__ == '__main__':
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)
