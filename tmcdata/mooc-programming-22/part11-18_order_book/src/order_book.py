class Task:
    task_num = 0

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        Task.task_num += 1
        self.id = Task.task_num
        self.complete = False

    def mark_finished(self):
        print('marked finished in class Task')
        self.complete = True

    def is_finished(self):
        return self.complete

    def __str__(self):
        shared_text = f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer}"
        ending = "FINISHED" if self.complete else 'NOT FINISHED'
        return f"{shared_text} {ending}"


class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        new_task = Task(description, programmer, workload)
        self.orders.append(new_task)

    def all_orders(self):
        return self.orders

    def get_names(self):
        names = [task.programmer for task in self.orders]
        names = list(set(names))
        return sorted(names)

    def programmers(self):
        return self.get_names()

    def mark_finished(self, id: int):
        id_found = False
        for task in self.orders:
            if task.id == id:
                task.mark_finished()
                id_found = True
        if not id_found:
            raise ValueError("No Such ID found!")


if __name__ == '__main__':
    # print('\nPart 1:')
    # t1 = Task("program hello world", "Eric", 3)
    # print(t1.id, t1.description, t1.programmer, t1.workload)
    # print(t1)
    # print(t1.is_finished())
    # t1.mark_finished()
    # print(t1)
    # print(t1.is_finished())
    # t2 = Task("program webstore", "Adele", 10)
    # t3 = Task("program mobile app for workload accounting", "Eric", 25)
    # print(t2)
    # print(t3)

    # print('\nPart 2:')
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)
    # for order in orders.all_orders():
    #     print(order)
    # print()
    # for programmer in orders.programmers():
    #     print(programmer)

    print('\nPart 3:')
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    for order in orders.all_orders():
        print(order)

    orders.mark_finished(1)
    orders.mark_finished(2)

    for order in orders.all_orders():
        print(order)
