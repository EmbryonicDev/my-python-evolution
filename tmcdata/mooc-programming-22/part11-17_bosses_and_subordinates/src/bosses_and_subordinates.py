# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)


def count_subordinates(employee: Employee):
    count = 0

    for child in employee.subordinates:
        count += count_subordinates(child) + 1
    return count


if __name__ == "__main__":
    print('\nPart 1')
    t1 = Employee("Sally")
    t2 = Employee("Eric")
    t3 = Employee("Matthew")
    t4 = Employee("Emily")
    t5 = Employee("Adele")
    t6 = Employee("Claire")
    t1.add_subordinate(t4)
    t1.add_subordinate(t6)
    t4.add_subordinate(t2)
    t4.add_subordinate(t3)
    t4.add_subordinate(t5)
    print(count_subordinates(t1))
    print(count_subordinates(t4))
    print(count_subordinates(t5))

    print('\nPart 2')
    t1 = Employee("Sally")
    t2 = Employee("Matthew")
    t3 = Employee("Eric")
    t4 = Employee("Andy")
    t5 = Employee("Emily")
    t6 = Employee("James")
    t7 = Employee("John")
    t8 = Employee("Tina")
    t9 = Employee("Theodore")
    t10 = Employee("Arthur")
    t11 = Employee("Jack")
    t12 = Employee("Lea")
    t1.add_subordinate(t3)
    t1.add_subordinate(t4)
    t1.add_subordinate(t7)
    t3.add_subordinate(t8)
    t3.add_subordinate(t9)
    t3.add_subordinate(t10)
    t3.add_subordinate(t12)
    t9.add_subordinate(t2)
    t2.add_subordinate(t5)
    t2.add_subordinate(t11)
    t5.add_subordinate(t6)

    print('T1 - Sally:', count_subordinates(t1))
    print('T2 - Mathew:', count_subordinates(t2))
    print('T3 - Eric:', count_subordinates(t3))
    print('T4 - Andy:', count_subordinates(t4))
    print('T5 - Emily:', count_subordinates(t5))
    print('T6 - James:', count_subordinates(t6))
    print('T7 - John:', count_subordinates(t7))
    print('T8 - Tina:', count_subordinates(t8))
    print('T9 - Theodore:', count_subordinates(t9))
    print('T10 - Arthur:', count_subordinates(t10))
    print('T11 - Jack:', count_subordinates(t11))
    print('T12 - Lea:', count_subordinates(t12))
