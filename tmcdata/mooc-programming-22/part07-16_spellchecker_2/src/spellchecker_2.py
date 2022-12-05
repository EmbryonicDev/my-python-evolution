from difflib import get_close_matches

dictionary = []
with open('wordlist.txt') as file:
    for line in file:
        dictionary.append(line.strip())

text = input('Write text: ')
suggestions = {}
for word in text.split(' '):
    if word.lower() in dictionary:
        print(word, end=' ')
    else:
        print(f"*{word}*", end=' ')
        suggestions[word] = get_close_matches(word, dictionary)

print('\nsuggestions:')
for key, value in suggestions.items():
    print(f"{key}: {', '.join(value)}")
