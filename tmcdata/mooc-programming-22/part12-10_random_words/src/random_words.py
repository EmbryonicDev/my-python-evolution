from random import choice


def word_generator(characters: str, length: int, amount: int):
    # first attempt
    # def get_char(length: int):
    #     word = ''
    #     for i in range(length):
    #         word += characters[random.randint(0, len(characters)-1)]
    #     return word
    # return (get_char(length) for i in range(amount))

    # second attempt
    return ("".join([choice(characters) for i in range(length)]) for j in range(amount))


if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
