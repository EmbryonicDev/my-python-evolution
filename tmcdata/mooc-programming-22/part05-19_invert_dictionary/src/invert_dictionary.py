def invert(dictionary: dict):
    # my solution
    # temp_dict = dict(map(reversed, dictionary.items()))

    # dictionary.clear()
    # for key, value in temp_dict.items():
    #     dictionary[key] = value

    # model solution
    copy = {}
    for item in dictionary:
        copy[item] = dictionary[item]

    dictionary.clear()

    for item in copy:
        dictionary[copy[item]] = item


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
