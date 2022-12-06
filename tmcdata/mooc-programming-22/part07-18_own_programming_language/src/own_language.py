from string import ascii_uppercase


def get_variables():
    my_variable = {}
    for i in ascii_uppercase:
        my_variable[i] = 0
    return my_variable


def run(instructions: list):
    results = []
    my_variables = get_variables()

    for instruction in instructions:
        parts = instruction.split(' ')
        command = parts[0]
        if command == 'PRINT':
            results.append(my_variables[parts[1]])
        elif command == 'MOV':
            my_variables[parts[1]] = int(parts[2])
        elif command == 'ADD':
            my_variables[parts[1]] += my_variables[parts[2]]

        elif instruction == 'END':
            break

    return results


if __name__ == '__main__':
    # part 1
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    print(run(program1))
