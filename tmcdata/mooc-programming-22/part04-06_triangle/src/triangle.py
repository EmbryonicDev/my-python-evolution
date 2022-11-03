def line(num, text):
    if text == "":
        print("*" * num)
    else:
        print(text[0] * num)


def triangle(size):
    counter = 1
    while counter <= size:
        line(counter, "#")
        counter += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
