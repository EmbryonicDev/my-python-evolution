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

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"


if __name__ == '__main__':
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
