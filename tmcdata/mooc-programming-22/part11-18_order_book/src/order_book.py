class Task:
    complete = False
    task_num = 0

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        Task.task_num += 1
        self.id = Task.task_num

    def mark_finished(self):
        Task.complete = True

    def is_finished(self):
        return Task.complete

    def __str__(self):
        shared_text = f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer}"
        ending = "FINISHED" if Task.complete else 'NOT FINISHED'
        return f"{shared_text} {ending}"


if __name__ == '__main__':
    print('\nPart 1:')
    t1 = Task("program hello world", "Eric", 3)
    print(t1.id, t1.description, t1.programmer, t1.workload)
    print(t1)
    print(t1.is_finished())
    t1.mark_finished()
    print(t1)
    print(t1.is_finished())
    t2 = Task("program webstore", "Adele", 10)
    t3 = Task("program mobile app for workload accounting", "Eric", 25)
    print(t2)
    print(t3)

