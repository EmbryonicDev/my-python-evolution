def same_chars(text, index1, index2):
    if index1 < len(text) - 1 and index2 < len(text) - 1:
        if text[index1] == text[index2]:
            return True
    return False


# test code
if __name__ == "__main__":
    # same characters m and m
    print(same_chars("programmer", 6, 7))  # True
    # different characters p and r
    print(same_chars("programmer", 0, 4))  # False
    # the second index is not within the string
    print(same_chars("programmer", 0, 12))  # False
