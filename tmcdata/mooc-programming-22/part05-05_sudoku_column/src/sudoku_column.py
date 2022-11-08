def column_correct(sudoku: list, column_no: int):
    numbers = []

    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)

    return True


if __name__ == "__main__":
    sudoku_list = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(column_correct(sudoku_list, 0))
    print(column_correct(sudoku_list, 3))
