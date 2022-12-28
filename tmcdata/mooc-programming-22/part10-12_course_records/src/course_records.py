class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def change_grade(self, grade: int):
        self.__grade = grade

    def change_credits(self, credits: int):
        self.__credits = credits

    def name(self):
        return self.__name

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits

    def __str__(self):
        return f"{self.name()} ({self.credits()} cr) grade {self.grade()}"


class CourseCollection:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
        if grade > self.__courses[name].grade():
            self.__courses[name].change_grade(grade)
        self.__courses[name].change_credits(credits)

    def get_data(self, name):
        if name not in self.__courses:
            return None
        return self.__courses[name]

    def __get_credits(self):
        total = 0
        for courses in self.__courses.values():
            total += courses.credits()
        return total

    def __get_grades(self):
        total = 0
        for courses in self.__courses.values():
            total += courses.grade()
        return total

    def __get_mean(self):
        return self.__get_grades() / len(self.__courses)

    def __get_grades_distr(self):
        results = {}
        for i in range(5, 0, -1):
            count = ''
            for key in self.__courses:
                if self.__courses[key].grade() == i:
                    count += 'x'
            results[i] = count
        return results

    def get_stats(self):
        return {
            'total courses': len(self.__courses),
            'credits': self.__get_credits(),
            'mean': self.__get_mean(),
            'grade distribution': self.__get_grades_distr()
        }


class CourseApp:
    def __init__(self):
        self.__course_collection = CourseCollection()

    def help(self):
        print('1 add course')
        print('2 get course data')
        print('3 statistics')
        print('0 exit')

    def add_course(self):
        course = input('course: ')
        grade = int(input('grade: '))
        credits = int(input('credits: '))
        self.__course_collection.add_course(course, grade, credits)

    def get_data(self):
        course = input('course: ')
        data = self.__course_collection.get_data(course)
        if data == None:
            print('no entry for this course')
            return
        print(data)

    def get_stats(self):
        data = self.__course_collection.get_stats()
        print(
            f"{data['total courses']} completed courses, a total of {data['credits']} credits")
        print(f"mean {data['mean']:.1f}")
        print("grade distribution")
        for key, value in data['grade distribution'].items():
            print(f"{key}: {value}")

    def execute(self):
        self.help()
        while True:
            print('')
            command = input('command: ')
            if command == '0':
                break
            elif command == '1':
                self.add_course()
            elif command == '2':
                self.get_data()
            elif command == '3':
                self.get_stats()


app = CourseApp()
app.execute()
