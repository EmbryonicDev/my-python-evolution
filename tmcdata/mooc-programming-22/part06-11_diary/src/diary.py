def add_entry(entry: str):
    with open('diary.txt', 'a') as diary:
        diary.write(entry + '\n')


def read_entry():
    with open('diary.txt') as diary:
        for line in diary:
            print(line.strip())


while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    function = int(input('Function: '))
    if function == 0:
        break
    elif function == 1:
        entry = input('Diary entry: ')
        add_entry(entry)
        print('Diary saved')
    elif function == 2:
        print('Entries:')
        read_entry()

print('Bye now!')
