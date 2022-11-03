def line(num, text):
    if text == "":
        print("*" * num)
    else:
        print(text[0] * num)


def square(size, character):
    counter = size
    while counter > 0:
        line(size, character)
        counter -= 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
    print()
    square(3, "o")
