from random import choice, shuffle
from string import ascii_lowercase, digits


def get_pool(numbers: bool, special_chars: bool):
    letters = list(ascii_lowercase)
    letters_nums = letters[::-1]
    letters_special = letters[::-1]
    special = ['!', '?', '=', '+', '-', '(', ')', '#']
    for number in digits:
        letters_nums.append(number)
    for char in special:
        letters_special.append(char)
    combined = letters_special[::-1]
    for number in digits:
        combined.append(number)

    all_pools = (letters, letters_nums, letters_special, combined)

    return all_pools


def generate_strong_password(psw_count: int, numbers: bool, special_chars: bool):
    pool = get_pool(numbers, special_chars)
    special = ['!', '?', '=', '+', '-', '(', ')', '#']
    find_letter = False
    find_number = False
    find_special = False
    psw = ''
    
    if not numbers and not special_chars:
        for i in range(psw_count):
          psw += choice(pool[0])
    elif numbers and not special_chars:
        while True:
            if find_number and find_letter:
                break
            psw = ''
            find_letter = False
            find_number = False          
            for i in range(psw_count):
                psw += choice(pool[1])
            for char in psw:
                if char in digits:
                    find_number = True
                if char in ascii_lowercase:
                    find_letter = True 
    elif not numbers and special_chars:
        while True:
            if find_special and find_letter:
                break
            psw = ''
            find_letter = False
            find_special = False            
            for i in range(psw_count):
                psw += choice(pool[2])
            for char in psw:
                if char in special:
                    find_special = True
                if char in ascii_lowercase:
                    find_letter = True
    else:
        while True:
            if find_special and find_letter and find_number:
                break
            psw = ''
            find_letter = False
            find_number = False
            find_special = False
            for i in range(psw_count):
                psw += choice(pool[3])
            for char in psw:
                if char in special:
                    find_special = True
                if char in ascii_lowercase:
                    find_letter = True
                if char in digits:
                    find_number = True                    

    return psw


if __name__ == '__main__':
    print()
    print('letters only: ')
    print(generate_strong_password(2, False, False))
    print()
    print('letters & nums: ')
    print(generate_strong_password(8, True, False))
    print()
    print('letters & special: ')
    print(generate_strong_password(8, False, True))
    print()
    print('combined:')
    print(generate_strong_password(8, True, True))
    print()
    print(generate_strong_password(4, True, True))