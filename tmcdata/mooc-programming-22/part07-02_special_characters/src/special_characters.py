import string


def separate_characters(my_string: str):
    letters = ''
    punctuation = ''
    other = ''
    for char in my_string:
        if char in string.ascii_letters:
            letters += char
        elif char in string.punctuation:
            punctuation += char
        else:
            other += char
    return (letters, punctuation, other)


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
