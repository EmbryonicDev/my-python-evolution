# Write your solution here
def line(num, text):
    if text == "":
        print("*" * num)
    else:
        print(text[0] * num)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
    line(4, "")
