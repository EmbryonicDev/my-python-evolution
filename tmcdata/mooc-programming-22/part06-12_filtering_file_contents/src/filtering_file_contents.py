def clear_file(filename: str):
    open(filename, 'w').close()


def check_problem(problem: str, splitter: str, solution: int):
    problem = problem.split(splitter)
    num1 = int(problem[0])
    num2 = int(problem[1])
    if ((splitter == '-' and num1 - num2 == solution) or
            (splitter == '+' and num1 + num2 == solution)):
        return 'correct.csv'
    else:
        return 'incorrect.csv'


def filter_solutions():
    clear_file('correct.csv')
    clear_file('incorrect.csv')
    with open('solutions.csv') as file:
        for line in file:
            parts = line.strip().split(';')
            parts[2] = int(parts[2])
            if '-' in parts[1]:
                splitter = '-'
            if '+' in parts[1]:
                splitter = '+'
            filename = check_problem(parts[1], splitter, parts[2])
            # write to file
            with open(filename, 'a') as file:
                file.write(line)


if __name__ == "__main__":
    filter_solutions()
