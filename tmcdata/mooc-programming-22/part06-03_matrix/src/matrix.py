def return_lines_list():
    lines = []
    with open('matrix.txt') as file:
        for line in file:
            line = line.replace('\n', '')
            parts = line.split(',')
            # convert to int
            for i in range(0, len(parts)):
                parts[i] = int(parts[i])
            lines.append(parts)
    return lines


def matrix_sum():
    lines = return_lines_list()
    my_sum = 0
    for line in lines:
        my_sum += sum(line)
    return my_sum


def matrix_max():
    lines = return_lines_list()
    my_max = -99999
    for line in lines:
        if max(line) > my_max:
            my_max = max(line)
    return my_max


def row_sums():
    lines = return_lines_list()
    row_sum_list = []
    for line in lines:
        row_sum_list.append(sum(line))
    return row_sum_list


if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
