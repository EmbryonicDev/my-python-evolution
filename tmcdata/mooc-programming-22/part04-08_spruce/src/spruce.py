def spruce(num):
    print("a spruce!")
    space_counter = num - 1
    star_counter = 1
    while star_counter <= num * 2:
        print(" " * space_counter + "*" * star_counter)
        star_counter += 2
        space_counter -= 1
    print(" " * (num - 1) + "*")


# test code
if __name__ == "__main__":
    spruce(5)
    spruce(3)
