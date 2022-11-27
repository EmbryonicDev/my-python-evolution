def add_word(fin_word: str, eng_word: str):
    with open('dictionary.txt', 'a') as file:
        file.write(f"{fin_word};{eng_word}\n")


def search_word(search_term: str):
    with open('dictionary.txt') as file:
        for line in file:
            parts = line.split(';')
            if word in line:
                print(f"{parts[0]} - {parts[1].strip()}")


while True:
    print('1 - Add word, 2 - Search, 3 - Quit')
    function = int(input('Function: '))
    if function == 3:
        break
    elif function == 1:
        fin_word = input('The word in Finnish: ')
        eng_word = input('The word in English: ')
        add_word(fin_word, eng_word)
        print('Dictionary entry added')
    elif function == 2:
        word = input('Search term: ')
        search_word(word)
print('Bye!')
