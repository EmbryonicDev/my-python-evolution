from random import choice
from string import ascii_lowercase


def generate_password(psw_count: int):
    psw = ''
    for i in range(psw_count):
        psw += choice(ascii_lowercase)
    return psw


if __name__ == '__main__':
    for i in range(10):
        print(generate_password(12))
