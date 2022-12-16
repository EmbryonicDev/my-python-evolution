class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__all_items = []

    def add_item(self, item: Item):
        if item.weight() < (self.__max_weight - self.weight()):
            self.__all_items.append(item)

    def weight(self):
        weight = 0
        for item in self.__all_items:
            weight += item.weight()
        return weight

    def print_items(self):
        for item in self.__all_items:
            print(item)

    def __str__(self):
        return f"{len(self.__all_items)} {'item' if len(self.__all_items) == 1 else 'items'} ({self.weight()} kg)"


class CargoHold:
    pass


if __name__ == '__main__':
    print('\nPart 1')
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)

    print("Name of the book:", book.name())
    print("Weight of the book:", book.weight())

    print("Book:", book)
    print("Phone:", phone)
    book = Item("ABC Book", 2)

    print('\nPart 2 & 3')
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)
    suitcase = Suitcase(5)
    print(suitcase)
    suitcase.add_item(book)
    print(suitcase)
    suitcase.add_item(phone)
    print(suitcase)
    suitcase.add_item(brick)
    print(suitcase)

    print('\nPart 4')
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight} kg")
