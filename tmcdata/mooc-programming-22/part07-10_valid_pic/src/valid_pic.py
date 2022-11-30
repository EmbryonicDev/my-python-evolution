from datetime import datetime


def is_it_valid(pic: str):
    if len(pic) != 11:
        return False

    control_string = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    control_char = pic[-1]
    integer = int(pic[0:6] + pic[7:-1])
    index = integer % 31

    if pic[6] == '+':
        year = int('18' + pic[4:6])
    elif pic[6] == '-':
        year = int('19' + pic[4:6])
    elif pic[6] == 'A':
        year = int('20' + pic[4:6])

    try:
        date = datetime(year, int(pic[2:4]), int(pic[0:2]))
    except ValueError:
        return False

    return control_char == control_string[index]


if __name__ == '__main__':
    print(is_it_valid('290200-1239'))
    print(is_it_valid('230827-906F'))
    print(is_it_valid('120488+246L'))
    print(is_it_valid('310823A9877'))
    print(is_it_valid('230827-906F1'))
