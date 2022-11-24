import math
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")


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


def get_points(all_points: int):
    borders = [15, 18, 20, 24, 28, 100]
    grade = 0
    for point in borders:
        if all_points < point:
            return grade
        grade += 1


print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10} ")
for id, student in students1.items():
    if id in exercises1:
        exercises = sum(exercises1[id])
        exercise_points = math.floor(sum(exercises1[id])/4)
        student_points = sum(points[id])
        total_points = student_points + exercise_points
        grade = get_points(total_points)
        print(f"{student:30}{exercises:<10}{exercise_points:<10}{student_points:<10}{total_points:<10}{grade:<10}")
