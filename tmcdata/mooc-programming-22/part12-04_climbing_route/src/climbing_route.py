class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"


def sort_by_length(items: list):
    def order_by_longest_length(item: dict):
        return item.length
    return sorted(items, key=order_by_longest_length, reverse=True)


def sort_by_difficulty(routes: list):
    def order_by_most_difficult(route: dict):
        return route.grade
    return sorted(routes, key=order_by_most_difficult, reverse=True)


if __name__ == '__main__':
    print('\nPart 1')
    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 11, "7A")
    r3 = ClimbingRoute("Synchro", 14, "8C+")
    r4 = ClimbingRoute("Small steps", 12, "6A+")
    routes = [r1, r2, r3, r4]
    for route in sort_by_length(routes):
        print(route)

    print('\nPart 2')
    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 11, "7A")
    r3 = ClimbingRoute("Synchro", 14, "8C+")
    r4 = ClimbingRoute("Small steps", 12, "6A+")
    routes = [r1, r2, r3, r4]
    for route in sort_by_difficulty(routes):
        print(route)
