from random import sample


def words(n: int, beginning: str):
    matching_words = []
    with open('words.txt') as file:
        for line in file:
            if line.strip().startswith(beginning):
                matching_words.append(line.strip())

    if len(matching_words) < n:
        error = f"I did not find {n} words that start with '{beginning}', only {len(matching_words)}"
        raise ValueError(error)

    return sample(matching_words, n)


if __name__ == '__main__':
    print()
    print(words(3, 'catn'))
    print()
    print(words(30, 'catn'))
