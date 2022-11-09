def remove_smallest(numbers: list):
    smallest_num = min(numbers)
    numbers.remove(smallest_num)


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
