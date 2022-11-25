def find_words(search_term: str):
    word_list = []

    with open('words.txt') as file:
        for word in file:
            word = word.strip()

            if search_term == word:
                word_list.append(word)

            elif '*' in search_term:
                if search_term.startswith('*'):
                    suffix = search_term[1:]
                    if word.endswith(suffix):
                        word_list.append(word)
                if search_term.endswith('*'):
                    prefix = search_term[0: len(search_term) - 1]
                    if word.startswith(prefix):
                        word_list.append(word)

            elif '.' in search_term:
                length = len(search_term)
                if len(word) == length:
                    match_count = 0
                    for i in range(0, length):
                        if word[i] == search_term[i] or search_term[i] == '.':
                            match_count += 1
                    if match_count == length:
                        word_list.append(word)
    return word_list


if __name__ == '__main__':
    print(find_words('caterpillar'))
    print(find_words('*vokes'))
    print(find_words('catni*'))
    print(find_words('p.ng'))
    print(find_words('.a.e'))
