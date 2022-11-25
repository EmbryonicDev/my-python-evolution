import math
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
course_information = input("Course information: ")


def convert_to_int(parts: list):
    for i in range(0, len(parts)):
        parts[i] = int(parts[i])


students1 = {}
with open(student_info) as file:
    for line in file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        students1[int(parts[0])] = parts[1] + " " + parts[2].strip()

exercises1 = {}
with open(exercise_data) as file:
    for line in file:
        line = line.strip()
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        convert_to_int(parts)
        exercises1[parts[0]] = parts[1:]

points = {}
with open(exam_points) as file:
    for line in file:
        line = line.strip()
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        convert_to_int(parts)
        points[parts[0]] = parts[1:]

course_info = {}
with open(course_information) as file:
    for line in file:
        parts = line.split(':')
        course_info[parts[0]] = parts[1]


def get_points(all_points: int):
    borders = [15, 18, 20, 24, 28, 100]
    grade = 0
    for point in borders:
        if all_points < point:
            return grade
        grade += 1


with open('results.csv', 'w') as csv_file, open('results.txt', 'w') as txt_file:
    # print txt file header
    header = f"{course_info['name'].strip()}, {course_info['study credits'].strip()} credits"
    txt_file.write(header+'\n')
    txt_file.write('='*len(header)+'\n')
    txt_file.write(
        f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")

    # define variables
    for id, student in students1.items():
        exercises = sum(exercises1[id])
        exercise_points = math.floor(sum(exercises1[id])/4)
        student_points = sum(points[id])
        total_points = student_points + exercise_points
        grade = get_points(total_points)

        # write student data to txt file
        txt_file.write(
            f"{student:30}{exercises:<10}{exercise_points:<10}{student_points:<10}{total_points:<10}{grade:<10}\n")

        # write student data to csv file
        csv_file.write(f"{id};{student};{grade}\n")
