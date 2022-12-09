class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"Preset: {self.name} ({self.weight} kg)"


if __name__ == '__main__':
    print('\nPart 1')
    book = Present("ABC Book", 2)
    print("The name of the present:", book.name)
    print("The weight of the present:", book.weight)
    print("Present:", book)
