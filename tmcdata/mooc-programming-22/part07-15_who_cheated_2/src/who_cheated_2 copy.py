from datetime import datetime, timedelta
import csv


def final_points():
    students = {}
    final_points = {}

    with open('start_times.csv') as times_file, open('submissions.csv') as submissions_file:

        # get student start times
        for line in csv.reader(times_file, delimiter=';'):
            name = line[0]
            start_time = datetime.strptime(line[1], '%H:%M')
            students[name] = {'start_time': start_time, 'tasks': []}
        # print(students)
        # students.append({'name': name, "start_time": start_time, 'tasks': []})

        # get all submission:
        for line in csv.reader(submissions_file, delimiter=';'):
            name = line[0]
            task = line[1]
            points = int(line[2])
            end_time = datetime.strptime(line[3], "%H:%M")

            # for student in students:
            for student in students:
                if name == student:
                    students[name]['end_time'] = end_time
                    if students[name]['end_time'] - students[name]['start_time'] < timedelta(hours=3):
                        students[name]['tasks'].append({task, points})
            # print(students)

        for student in students:
            print(student)
            filtered_points = {}
            for i in range(1, 9):
                filtered_points[i] = 0

            for index, value in filtered_points.items():
                highest_value = value

        #         for tasks in students[student]['tasks']:
        #             print(tasks[1], index)
            # if int(task[0]) == index and task[1] > highest_value:
            #     print('hello')
            #         if int(task[0]) == index and task[1] > highest_value:
            #             highest_value = task[1]
            #         filtered_points[index] = highest_value
            # students[name]['final_points'] = filtered_points

            # sum_points = 0
            # for key, value in students[name]['final_points'].items():
            #     sum_points += value
            # final_points[name] = sum_points

            # print(students)

    # for student in students:
    #     filtered_points = {}
    #     for i in range(1, 9):
    #         filtered_points[i] = 0

    #     for task_key, task_value in filtered_points.items():
    #         highest_value = task_value
    #         for task in student['tasks']:
    #             if int(task[0]) == task_key and task[1] > highest_value:
    #                 highest_value = task[1]
    #             filtered_points[task_key] = highest_value
    #     student['final_points'] = filtered_points

    #     sum_points = 0
    #     for key, value in student['final_points'].items():
    #         sum_points += value
    #     final_points[student['name']] = sum_points

    return final_points


if __name__ == '__main__':
    print(final_points())
