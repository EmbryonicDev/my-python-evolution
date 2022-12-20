# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents

    def amount(self, money):
        return f"{money.euros}.{money.cents:02d}"

    def __eq__(self, another):
        amount1, amount2 = self.amount(self), self.amount(another)
        return amount1 == amount2

    def __lt__(self, another):
        amount1, amount2 = self.amount(self), self.amount(another)
        return amount1 < amount2

    def __gt__(self, another):
        amount1, amount2 = self.amount(self), self.amount(another)
        return amount1 > amount2

    def __ne__(self, another):
        amount1, amount2 = self.amount(self), self.amount(another)
        return amount1 != amount2

    def __str__(self):
        return f"{self.euros}.{self.cents:02d} eur"


if __name__ == '__main__':
    print('\nPart 1')
    e1 = Money(4, 10)
    e2 = Money(2, 5)  # two euros and five cents

    print(e1)
    print(e2)

    print('\nPart 2')
    e3 = Money(4, 10)
    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)

    print('\nPart 3')
    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)
