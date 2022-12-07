def smallest_average(person1: dict, person2: dict, person3: dict):
    persons = [person1, person2, person3]
    min_points = 9999999
    dumbest = ''

    for person in persons:
        total = 0
        for key, value in person.items():
            if 'result' in key:
                total += value
        if total < min_points:
            min_points = total
            dumbest = person
    return dumbest


if __name__ == '__main__':
    person1 = {"name": "Mary", "result1": 9, "result2": 9, "result3": 9}
    person2 = {"name": "Gary", "result1": 7, "result2": 7, "result3": 7}
    person3 = {"name": "Larry", "result1": 8, "result2": 8, "result3": 8}

    print(smallest_average(person1, person2, person3))
