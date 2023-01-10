# Write your solution here
import re


def is_dotw(my_string: str):
    return True if re.search('Mon|Tue|Wed|Thu|Fri|Sat|Sun', my_string) else False


def all_vowels(my_string: str):
    return True if re.search('^[aeiou]*$', my_string) else False


if __name__ == "__main__":
    print('\nPart 1:')
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))

    print('\nPart 2:')
    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))
