def line(num, text):
    if text == "":
        print("*" * num)
    else:
        print(text[0] * num)


def square_of_hashes(size):
    counter = size
    while counter > 0:
        line(size, "#")
        counter -= 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
    square_of_hashes(3)
