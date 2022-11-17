def add_student(database: dict, name: str):
    database[name] = {'courses': []}


def print_student(database: dict, name: str):
    if name in database:
        courses = database[name]['courses']
        course_count = len(courses)
        filler_text = "completed courses"
        grade_sum = 0

        print(f"{name}:")
        if course_count < 1:
            print(f" no {filler_text}")
        else:
            print(f" {course_count} {filler_text}:")
            for course in courses:
                grade_sum += float(course['grade'])
                print(f"  {course['name']} {course['grade']}")
            print(f" average grade {grade_sum / course_count}")
    else:
        print(f"{name}: no such person in the database")


def add_course(database: dict, name: str, course_and_grade: tuple):
    course_name = course_and_grade[0]
    grade = course_and_grade[1]
    courses = database[name]['courses']
    new_course = True

    if grade > 0:
        for course in courses:
            if course_name in course['name']:
                new_course = False
                if course['grade'] < grade:
                    course['grade'] = grade
        if new_course:
            course = {'name': course_name, 'grade': grade}
            courses.append(course)


def summary(database: dict):
    most_courses = 0
    most_courses_person = ''
    highest_average = 0
    highest_average_person = ''

    for name in database:
        courses = database[name]['courses']
        course_count = len(courses)
        grade_sum = 0

        for course in courses:
            grade_sum += (course['grade'])

        if grade_sum / course_count > highest_average:
            highest_average = float(grade_sum / course_count)
            highest_average_person = name

        if course_count > most_courses:
            most_courses = course_count
            most_courses_person = name

    print(f"students {len(database)}")
    print(f"most courses completed {most_courses} {most_courses_person}")
    print(f"best average grade {highest_average} {highest_average_person} ")


if __name__ == "__main__":
    students = {}

    # part 1: adding student
    print('\nPart 1:')
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")

    # part 2: adding completed courses
    print('\nPart 2:')
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")

    # part 3: repeating courses
    print('\nPart 3:')
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")

    # part 4: summary of database:
    print('\nPart 4:')
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
