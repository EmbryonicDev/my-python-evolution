from datetime import datetime, timedelta
import csv


def final_points():
    students = {}

    with open('start_times.csv') as times_file, open('submissions.csv') as submissions_file:

        # get student start times
        for line in csv.reader(times_file, delimiter=';'):
            name = line[0]
            start_time = datetime.strptime(line[1], '%H:%M')
            students[name] = {'start_time': start_time, 'tasks': {}}

        # get all submission data to update students dict
        for line in csv.reader(submissions_file, delimiter=';'):
            name = line[0]
            task_num = int(line[1])
            task_points = int(line[2])
            end_time = datetime.strptime(line[3], "%H:%M")

            for student in students:
                if name == student:
                    students[student]['end_time'] = end_time
                    # add tasks only if end time is less than 3 hours from start
                    if students[student]['end_time'] - students[student]['start_time'] < timedelta(hours=3):
                        # add task to tasks if task num not found
                        if task_num not in students[student]['tasks']:
                            students[student]['tasks'][task_num] = task_points
                        # if task num found, only add if new value is greater than old value
                        else:
                            for key, value in students[student]['tasks'].items():
                                if key == task_num and task_points > value:
                                    students[student]['tasks'][task_num] = task_points

        # get sum of all task points & add to final_points dict
        final_points = {}
        for student in students:
            sum_points = 0
            for key, value in students[student]['tasks'].items():
                sum_points += value
            final_points[student] = sum_points

    return final_points


if __name__ == '__main__':
    print(final_points())
