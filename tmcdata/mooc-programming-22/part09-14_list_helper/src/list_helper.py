class ListHelper:
    def __init__(self, numbers: list):
        self.__numbers = numbers

    @classmethod
    def greatest_frequency(self, my_list: list):
        winner = ''
        highest_count = 0
        counter = 0
        for num in my_list:
            for num1 in my_list:
                if num == num1:
                    counter += 1
            if counter > highest_count:
                winner = num
                highest_count = counter
                counter = 0
        return winner

    @classmethod
    def doubles(self, my_list: list):
        numbers_copy = my_list[:]
        unique_nums = []
        for i in range(len(my_list)):
            num = numbers_copy.pop(0)
            if num not in unique_nums and num in numbers_copy:
                unique_nums.append(num)
        return len(unique_nums)


if __name__ == '__main__':
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
