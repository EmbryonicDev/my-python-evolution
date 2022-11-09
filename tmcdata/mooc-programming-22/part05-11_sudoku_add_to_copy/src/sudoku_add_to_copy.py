def print_sudoku(sudoku: list):
    c_count = 0

    for row in sudoku:
        b_count = 0
        for cell in row:
            b_count += 1
            if cell == 0:
                print("_", end=" ")
            else:
                print(cell, end=" ")
            if b_count % 3 == 0 and b_count < 8:
                print(" ", end="")
        c_count += 1
        if c_count % 3 == 0 and c_count < 8:
            print()
        print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    # only works on 1 dimensional lists:
    # new_list = sudoku[:] 
    
    # works on 2 dimension:
    new_list = []
    for r in sudoku:
        new_list.append(r[:])
    
    # works on all dimensional lists:
    # {import copy} first!
    # new_list = copy.deepcopy(sudoku)
    
    # also works on all dimensional lists:
    # new_list = [item[:] for item in sudoku]
    
    new_list[row_no][column_no] = number
    
    return new_list


if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 1, 1, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)