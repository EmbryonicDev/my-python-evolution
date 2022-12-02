import urllib.request
import json


def retrieve_all():
    my_request = urllib.request.urlopen(
        "https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.loads(my_request.read())
    open_courses = []
    for entry in data:
        if entry['enabled'] == True:
            course = entry['fullName'], entry['name'], entry['year'], sum(
                entry['exercises'])
            open_courses.append(course)
    return open_courses


def retrieve_course(course_name: str):
    my_url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request = urllib.request.urlopen(my_url)
    data = json.loads(my_request.read())
    course_data = {}
    hours = 0
    exercises = 0
    max_students = 0

    for key, value in data.items():
        hours += value['hour_total']
        exercises += value['exercise_total']
        if value['students'] > max_students:
            max_students = value['students']

    course_data['weeks'] = len(data)
    course_data['students'] = max_students
    course_data['hours'] = hours
    course_data['hours_average'] = int(hours / course_data['students'])
    course_data['exercises'] = exercises
    course_data['exercises_average'] = int(exercises / course_data['students'])
    return course_data


if __name__ == '__main__':
    # part 1
    print(retrieve_all())

    # part 2
    print()
    print()
    print(retrieve_course('CCFUN'))
    print()
    print()
