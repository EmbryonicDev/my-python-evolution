def filter_incorrect():
    with open('lottery_numbers.csv') as input_file, open('correct_numbers.csv', 'w') as result_file:
        for line in input_file:
            error = False
            parts = line.strip().split(';')
            week = parts[0].split(' ')
            try:
                int(week[1])
            except:
                error = True
            number_list = parts[1].split(',')
            breakpoint()
            for number in number_list:
                try:
                    int(number)
                    if int(number) < 1 or int(number) > 39:
                        error = True
                except:
                    error = True
            # check for duplicate numbers
            if len(number_list) != 7 or len(set(number_list)) != 7:
                error = True
            # write to file if no error
            if not error:
                result_file.write(line)


if __name__ == '__main__':
    filter_incorrect()
