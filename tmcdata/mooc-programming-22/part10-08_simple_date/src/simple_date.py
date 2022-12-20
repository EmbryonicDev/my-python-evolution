class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def get_date(self):
        return int(f"{self.__year}{self.__month:02d}{self.__day:02d}")

    def __lt__(self, another):
        return self.get_date() < another.get_date()

    def __gt__(self, another):
        return self.get_date() > another.get_date()

    def __eq__(self, another):
        return self.get_date() == another.get_date()

    def __ne__(self, another):
        return self.get_date() != another.get_date()

    def __add__(self, days: int):
        newDate = SimpleDate(self.__day, self.__month, self.__year)
        days_to_add = days

        while days_to_add > 0:
            if days_to_add >= 360:
                newDate.__year += 1
                days_to_add -= 360
            elif days_to_add >= 30:
                if newDate.__month == 12:
                    newDate.__year += 1
                    newDate.__month = 0
                else:
                    newDate.__month += 1
                    days_to_add -= 30
            else:
                if newDate.__day == 30:
                    newDate.__month += 1
                    newDate.__day = 0
                else:
                    newDate.__day += 1
                    days_to_add -= 1

        return newDate

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
