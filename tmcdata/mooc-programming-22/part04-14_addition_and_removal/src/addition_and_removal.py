list = []
number = 0
while True:
    print("The list is now", list)
    action = input("a(d)d, (r)emove or e(x)it: ")
    if action == 'x':
        break
    elif action == 'd':
        number += 1
        list.append(number)
    elif action == 'r':
        list.remove(number)
        number -= 1
print("Bye!")
