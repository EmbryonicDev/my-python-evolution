def largest():
    number_list = []
    with open('numbers.txt') as new_file:
        for line in new_file:
            line = line.replace('\n', '')
            number_list.append(line)
    return int(max(number_list))


if __name__ == "__main__":
    largest()
