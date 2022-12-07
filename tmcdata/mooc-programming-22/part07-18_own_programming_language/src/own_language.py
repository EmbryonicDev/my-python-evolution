from string import ascii_uppercase


def get_variables():
    my_variable = {}
    for i in ascii_uppercase:
        my_variable[i] = 0
    return my_variable


def calculate(command: str, variable: int, value: int):
    if command == "ADD":
        return variable + value
    elif command == "SUB":
        return variable - value
    elif command == 'MUL':
        return variable * value


def get_locations(instructions: list):
    locations = {}
    for instruction in instructions:
        parts = instruction.split(' ')
        if len(parts) < 2 and parts[0] != 'END':
            locations[parts[0]] = instructions.index(instruction)
    return locations


def check_condition(value1, value2, operator):
    if operator == '==':
        return value1 == value2
    elif operator == '!=':
        return value1 != value2
    elif operator == '<':
        return value1 < value2
    elif operator == '<=':
        return value1 <= value2
    elif operator == '>':
        return value1 > value2
    elif operator == '>=':
        return value1 >= value2


def run(instructions: list):
    results = []
    my_variables = get_variables()
    calc_commands = ['ADD', 'SUB', 'MUL']
    locations = get_locations(instructions)

    def get_value(value):
        return int(value) if value not in ascii_uppercase else my_variables[value]

    index = 0
    while index < len(instructions):
        parts = instructions[index].split(' ')
        command = parts[0]
        if command == 'PRINT':
            print_value = get_value(parts[1])
            results.append(print_value)
            index += 1
        elif command == 'MOV':
            mov_value = get_value(parts[2])
            my_variables[parts[1]] = mov_value
            index += 1
        elif command in calc_commands:
            value = get_value(parts[2])
            my_variables[parts[1]] = calculate(
                command, my_variables[parts[1]], value)
            index += 1
        elif command == 'IF':
            value1 = get_value(parts[1])
            value2 = get_value(parts[3])
            operator = parts[2]
            jump_location = locations[f"{parts[5]}:"]
            index = jump_location if check_condition(
                value1, value2, operator) else index + 1
        elif command == 'JUMP':
            jump_location = locations[f"{parts[1]}:"]
            index = jump_location
        else:
            index += 1

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

    # part 2
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)

    # part 3
    program3 = []
    program3.append("MOV A 1")
    program3.append("MOV B 1")
    program3.append("begin:")
    program3.append("PRINT A")
    program3.append("ADD B 1")
    program3.append("MUL A B")
    program3.append("IF B <= 10 JUMP begin")
    program3.append("END")
    result = run(program3)
    print(result)

    # part 4
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)

    test_program = [
        'MOV N 100',
        'PRINT 2',
        'MOV A 3',
        'start:',
        'MOV B 2',
        'MOV Z 0',
        'test:',
        'MOV C B',
        'new:',
        'IF C == A JUMP virhe',
        'IF C > A JUMP pass_by',
        'ADD C B',
        'JUMP new',
        'virhe:',
        'MOV Z 1',
        'JUMP pass_by2',
        'pass_by:',
        'ADD B 1',
        'IF B < A JUMP test',
        'pass_by2:',
        'IF Z == 1 JUMP pass_by3',
        'PRINT A',
        'pass_by3:',
        'ADD A 1',
        'IF A <= N JUMP start']
    result = run(test_program)
    print(result)
