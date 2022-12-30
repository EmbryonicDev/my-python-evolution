import csv
from string import punctuation


def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
        content = f.read()

    # remove line breaks and punctuation
    content = content.replace("\n", " ")
    for punctuation_mark in punctuation:
        content = content.replace(punctuation_mark, "")

    words = content.split(" ")
    return {word: words.count(word) for word in words if words.count(word) >= lower_limit}


if __name__ == '__main__':
    print(most_common_words("comprehensions.txt", 3))
