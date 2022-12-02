from datetime import datetime, timedelta, time, date


def add_student(name: str, start_time: time):
    return {
        'name': name,
        "start_time": start_time
    }


def add_submission(name: str, end_time: time):
    return {
        'name': name,
        'end_time': end_time
    }


def cheaters():
    students = []
    students_submissions = []
    cheaters_list = []

    with open('start_times.csv') as start_exam_file, open('submissions.csv') as submissions_file:
        # get student start times
        for line in start_exam_file:
            parts = line.strip().split(';')
            name = parts[0]
            start_time = parts[1].split(':')
            start_time = time(
                hour=int(start_time[0]), minute=int(start_time[1]))
            students.append(add_student(
                name, start_time))

        #  get all submissions
        for line in submissions_file:
            parts = line.strip().split(';')
            name = parts[0]
            end_time = parts[3].split(':')
            end_time = time(
                hour=int(end_time[0]), minute=int(end_time[1]))
            students_submissions.append(add_submission(name, end_time))

    # get max time
    for student in students:
        max_time = student['start_time']
        for submission in students_submissions:
            if (submission['name'] == student['name']) and submission['end_time'] > max_time:
                student['end_time'] = submission['end_time']
                max_time = submission['end_time']

    # get cheaters
    for student in students:
        max_time = datetime.combine(
            date.today(), student['start_time']) + timedelta(hours=3)
        converted_end_time = datetime.combine(
            date.today(), student['end_time'])
        if converted_end_time > max_time:
            cheaters_list.append(student['name'])

    return cheaters_list


if __name__ == '__main__':
    print(cheaters())
