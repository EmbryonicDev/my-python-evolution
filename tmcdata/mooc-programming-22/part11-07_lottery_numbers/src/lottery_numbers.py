class LotteryNumbers:
    def __init__(self, weekNum: int, numbers: list):
        self.__weekNum = weekNum
        self.__numbers = numbers

    def number_of_hits(self, numbers: list):
        return len(['*yOu_HaVe_A_hIt*' for num in numbers if num in self.__numbers])

    def hits_in_place(self, numbers: list):
        return [num if num in self.__numbers else -1 for num in numbers]


if __name__ == '__main__':
    print('\nPart 1')
    week5 = LotteryNumbers(5, [1, 2, 3, 4, 5, 6, 7])
    my_numbers = [1, 4, 7, 11, 13, 19, 24]
    print(week5.number_of_hits(my_numbers))

    print('\nPart 2')
    week8 = LotteryNumbers(8, [1, 2, 3, 10, 20, 30, 33])
    my_numbers = [1, 4, 7, 10, 11, 20, 30]
    print(week8.hits_in_place(my_numbers))
