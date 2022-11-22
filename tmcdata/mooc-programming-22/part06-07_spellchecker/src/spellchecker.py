text = input('Write text: ')

dictionary = []
with open('wordlist.txt') as file:
    for line in file:
        dictionary.append(line.strip())

text_list = text.split(' ')
for word in text_list:
    if word.lower() in dictionary:
        print(word, end=' ')
    else:
        print(f"*{word}*", end=' ')
