class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __value(self):
        # convert date to total days
        return (self.__year * 360) + (self.__month * 30) + self.__day

    def __to_date(self, days: int):
        # convert days to date
        months = days // 30
        years = months // 12
        days -= months * 30
        months -= years * 12
        return SimpleDate(days, months, years)

    def __lt__(self, another):
        return self.__value() < another.__value()

    def __gt__(self, another):
        return self.__value() > another.__value()

    def __eq__(self, another):
        return self.__value() == another.__value()

    def __ne__(self, another):
        return self.__value() != another.__value()

    def __add__(self, days_to_add: int):
        return self.__to_date(self.__value() + days_to_add)

    def __sub__(self, another):
        amount = self.__value() - another.__value()
        return amount if amount > 0 else amount * -1

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"


if __name__ == '__main__':
    print('\nPart 1')
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)
    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)

    print('\nPart 2')
    d3 = d1 + 3
    d4 = d2 + 400
    print(d1)
    print(d2)
    print(d3)
    print(d4)

    print('\nPart 3')
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)
    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
