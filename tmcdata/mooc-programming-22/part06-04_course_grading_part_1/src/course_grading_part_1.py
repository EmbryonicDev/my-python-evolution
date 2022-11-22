
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

students1 = {}
with open(student_info) as file:
    for line in file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        students1[int(parts[0])] = parts[1] + " " + \
            parts[2].replace('\n', '')

exercises1 = {}
with open(exercise_data) as file:
    for line in file:
        line = line.replace('\n', '')
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        # convert to int
        for i in range(0, len(parts)):
            parts[i] = int(parts[i])
        exercises1[int(parts[0])] = parts[1:]

for id, student in students1.items():
    if id in exercises1:
        my_sum = sum(exercises1[id])
        print(f"{student} {my_sum}")
