# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __amount(self, money):
        return float(f"{money.__euros}.{money.__cents:02d}")

    def __eq__(self, another):
        amount1, amount2 = self.__amount(self), self.__amount(another)
        return amount1 == amount2

    def __lt__(self, another):
        amount1, amount2 = self.__amount(self), self.__amount(another)
        return amount1 < amount2

    def __gt__(self, another):
        amount1, amount2 = self.__amount(self), self.__amount(another)
        return amount1 > amount2

    def __ne__(self, another):
        amount1, amount2 = self.__amount(self), self.__amount(another)
        return amount1 != amount2

    def __add__(self, another):
        amount1, amount2 = self.__amount(self), self.__amount(another)
        return f"{(amount1 + amount2):.2f} eur"

    def __sub__(self, another):
        amount1, amount2 = self.__amount(self), self.__amount(another)
        if amount1 - amount2 < 0:
            raise ValueError('A negative result is not allowed')
        return f"{(amount1 - amount2):.2f} eur"

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"


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

    print('\nPart 4')
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1
