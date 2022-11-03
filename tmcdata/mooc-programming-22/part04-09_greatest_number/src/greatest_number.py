def greatest_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    return num3


# test code
if __name__ == "__main__":
    print(greatest_number(3, 4, 1))  # 4
    print(greatest_number(99, -4, 7))  # 99
    print(greatest_number(0, 0, 0))  # 0
