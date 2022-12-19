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

    def heaviest_item(self):
        heaviest = None
        for item in self.__all_items:
            if heaviest == None:
                heaviest = item
            else:
                if item.weight() >= heaviest.weight():
                    heaviest = item
        return heaviest

    def __str__(self):
        return f"{len(self.__all_items)} {'item' if len(self.__all_items) == 1 else 'items'} ({self.weight()} kg)"


class CargoHold:
    def __init__(self, max_weight: int, cargo_hold=None):
        self.__max_weight = max_weight
        self.__cargo_hold = []

    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() < (self.__max_weight - self.weight()):
            self.__cargo_hold.append(suitcase)

    def weight(self):
        weight = 0
        for item in self.__cargo_hold:
            weight += item.weight()
        return weight

    def print_items(self):
        for suitcase in self.__cargo_hold:
            suitcase.print_items()

    def __str__(self):
        count = len(self.__cargo_hold)
        space = self.__max_weight
        if count > 0:
            space = self.__max_weight - self.weight()
        return f"{count} {'suitcase' if count == 1 else 'suitcases'}, space for {space} kg"


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
    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)
    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight} kg")

    print('\nPart 5')
    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")

    print('\nPart 6')
    cargo_hold = CargoHold(1000)
    print(cargo_hold)
    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)
    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)
    cargo_hold.add_suitcase(adas_suitcase)
    print(cargo_hold)
    cargo_hold.add_suitcase(peters_suitcase)
    print(cargo_hold)

    print('\nPart 7')
    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
