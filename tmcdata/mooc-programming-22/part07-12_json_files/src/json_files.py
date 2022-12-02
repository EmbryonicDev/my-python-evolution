import json


def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
    people = json.loads(data)
    for person in people:
        hobbies = ", ".join(person['hobbies'])
        print(
            f"{person['name']} {person['age']} years ({hobbies})")


if __name__ == '__main__':
    print('File 1')
    print_persons('file1.json')
    print()
    print('File 2')
    print_persons('file2.json')
    print()
    print('File 3')
    print_persons('file3.json')
    print()
    print('File 4')
    print_persons('file4.json')
    print()
