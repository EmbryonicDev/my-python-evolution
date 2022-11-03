def line(num, text):
    if text == "":
        print("*" * num)
    else:
        print(text[0] * num)


def shape(num1, text1, num2, text2):
    counter = 1
    while counter <= num1:
        line(counter, text1)
        counter += 1
    counter = num2
    while counter > 0:
        line(num1, text2)
        counter -= 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")
