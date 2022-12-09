# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"


class Room:
    def __init__(self):
        self.people_in_room = []

    def add(self, person: Person):
        self.people_in_room.append(person)

    def is_empty(self):
        return len(self.people_in_room) == 0

    def get_contents(self):
        total_height = 0
        count = len(self.people_in_room)
        for person in self.people_in_room:
            total_height += person.height
        return total_height, count

    def print_contents(self):
        contents = self.get_contents()
        print(
            f"There are {contents[1]} persons in the room, and their combined height is {contents[0]} cm")
        for person in self.people_in_room:
            print(person)

    def shortest(self):
        shortest_person = ''
        shortest_height = 999
        for person in self.people_in_room:
            if person.height < shortest_height:
                shortest_height = person.height
                shortest_person = person
        return None if len(self.people_in_room) == 0 else shortest_person

    def remove_shortest(self):
        shortest = self.shortest()
        if not self.is_empty():
            self.people_in_room.remove(shortest)
        return shortest


if __name__ == "__main__":
    print("\nPart1")
    room = Room()
    print("Is the room empty?", room.is_empty())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))
    print("Is the room empty?", room.is_empty())
    room.print_contents()

    print("\nPart2")
    room = Room()
    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    print()
    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())
    print()
    room.print_contents()

    print("\nPart3")
    room = Room()
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()
    print()
    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")
    print()
    room.print_contents()
