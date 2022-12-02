from datetime import datetime, timedelta, time, date
import csv


def cheaters():
    students = []
    students_submissions = []
    cheaters_list = []

    with open('start_times.csv') as start_exam_file, open('submissions.csv') as submissions_file:
        # get student start times
        for line in csv.reader(start_exam_file, delimiter=';'):
            name = line[0]
            start_time = datetime.strptime(line[1], '%H:%M')
            students.append({'name': name, "start_time": start_time})

        #  get all submissions
        for line in csv.reader(submissions_file, delimiter=';'):
            name = line[0]
            end_time = datetime.strptime(line[3], "%H:%M")
            students_submissions.append({'name': name, 'end_time': end_time})

    # get max time & cheaters
    for student in students:
        max_time = student['start_time']
        for submission in students_submissions:
            if (submission['name'] == student['name']) and submission['end_time'] - student['start_time'] > timedelta(hours=3):
                if student['name'] not in cheaters_list:
                    cheaters_list.append(student['name'])

    return cheaters_list


if __name__ == '__main__':
    print(cheaters())
