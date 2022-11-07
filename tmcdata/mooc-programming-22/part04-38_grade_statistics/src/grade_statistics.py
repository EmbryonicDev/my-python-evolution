import math


def check_fail(points):
    if points < 10:
        return True


def get_points(data):
    integers = data.split()
    points = float(integers[0])
    exercises = int(integers[1])
    exercise_points = float(math.floor(exercises / 10))
    total_points = points + exercise_points
    return total_points


def get_grade(total_points, fail):
    boundaries = [15, 18, 21, 24, 28, 31]
    if fail:
        return 0

    for i in range(0, 6, 1):
        if total_points < boundaries[i]:
            return i


def get_pass_average(grades_list):
    pass_count = 0

    for number in grades_list:
        if number > 0:
            pass_count += 1

    return (pass_count / len(grades_list)) * 100


def get_grade_distro(grades_list):
    for i in range(5, -1, -1):
        stars = "*" * grades_list.count(i)
        print(f"  {i}: {stars}")


def main():
    all_points = []
    all_grades = []
    while True:
        raw_data = input("Exam points and exercises completed: ")

        if raw_data == "":
            break

        fail = check_fail(int(raw_data.split()[0]))
        points = get_points(raw_data)
        all_points.append(points)
        grade = get_grade(points, fail)
        all_grades.append(grade)

    print('Statistics: ')
    print("Points average:", sum(all_points) / len(all_points))
    print(f"Pass percentage: {get_pass_average(all_grades):.1f}")
    print('Grade distribution: ')
    get_grade_distro(all_grades)


main()
