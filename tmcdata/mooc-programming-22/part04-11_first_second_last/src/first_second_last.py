def get_word(sentence, word_num):
    counter = 0
    while counter < word_num:
        if " " in sentence:
            index = sentence.find(' ')
            word = sentence[0:index]
            if " " in sentence:
                sentence = sentence[index + 1:]
        else:
            word = sentence
            break
        counter += 1
    return word


def first_word(sentence):
    return get_word(sentence, 1)


def second_word(sentence):
    return get_word(sentence, 2)


def last_word(sentence):
    return get_word(sentence, len(sentence))


# test code
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word("first second"))
    print(second_word("first second"))
    print(last_word(sentence))
