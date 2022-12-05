from string import ascii_letters, digits


def change_case(org_string: str):
    new_string = ''
    for letter in org_string:
        if letter.isupper():
            new_string += letter.lower()
        else:
            new_string += letter.upper()
    return new_string


def split_in_half(orig_string: str):
    split_at = int(len(orig_string) / 2)
    return orig_string[0:split_at], orig_string[split_at:]


def remove_special_characters(orig_string: str):
    new_string = ''
    allowed = ascii_letters + digits + ' '
    for char in orig_string:
        if char in allowed:
            new_string += char
    return new_string


if __name__ == '__main__':
    print(change_case('dEwAlD'))
    print()
    print(split_in_half('123456789'))
    print()
    print(remove_special_characters("This is a test, lets see how it goes!!!11!"))
