# Write your solution here!
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        shape = 'rectangle' if self.width != self.height else 'square'
        return f"{shape} {self.width}x{self.height}"

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)


if __name__ == '__main__':
    square = Square(4)
    print(square)
    print("area:", square.area())
