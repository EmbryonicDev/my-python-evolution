from random import choice, shuffle, randint
from string import ascii_lowercase, digits


def generate_strong_password(psw_count: int, numbers: bool, special_chars: bool):
    special = '!?=+-()#'
    choice_pool = ascii_lowercase
    # one letter to begin password
    psw = choice(choice_pool)

    # if numbers are required, add at least one
    if numbers:
        psw = add_char(digits, psw)
        choice_pool += digits

    # if special chars are required, add at least one
    if special_chars:
        psw = add_char(special, psw)
        choice_pool += special

    # build the rest of the password from pool
    while len(psw) < psw_count:
        psw = add_char(choice_pool, psw)

    return psw


def add_char(pool: str, psw: str):
    # get random char from pool
    new_char = choice(pool)
    # randomly add to beginning or end of psw
    if randint(1, 2) == 1:
        return new_char + psw
    else:
        return psw + new_char


if __name__ == '__main__':
    print()
    print('letters only: ')
    print(generate_strong_password(14, False, False))
    print()
    print('letters & nums: ')
    print(generate_strong_password(2, True, False))
    print()
    print('letters & special: ')
    print(generate_strong_password(2, False, True))
    print()
    print('combined:')
    print(generate_strong_password(5, True, True))
    print()
