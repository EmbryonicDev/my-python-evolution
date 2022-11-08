def row_correct(sudoku: list, row_no: int):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for number in numbers:
        if sudoku[row_no].count(number) > 1:
            return False

    return True
  
def column_correct(sudoku: list, column_no: int):
    numbers = []

    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)

    return True
  
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []

    for row in range(row_no, row_no + 3):
        for col in range(column_no, column_no + 3):
            num = sudoku[row][col]
            if num > 0 and num in numbers:
                return False
            numbers.append(num)

    return True
  
def sudoku_grid_correct(sudoku: list):
  # check rows
  rows = len(sudoku)
  for i in range(0, rows):
    row_correct(sudoku, i)
      
  # check columns
  columns = len(sudoku[0])
  for i in range(0, columns):
    if not column_correct(sudoku, i):
      return False
      
  # check blocks
  for row in range(0,9,3):
    for column in range(0,9,3):
      if not block_correct(sudoku, row, column):
        return False
    
  return True
      
  
if __name__ == "__main__":
  sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
  ]

  print(sudoku_grid_correct(sudoku1))

  sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
  ]

  print(sudoku_grid_correct(sudoku2))

