def line(num, text):
    if text == "":
        print("*" * num)
    else:
        print(text[0] * num)


def box_of_hashes(height):
    while height > 0:
        line(10, "#")
        height -= 1


# test function
if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(1)
