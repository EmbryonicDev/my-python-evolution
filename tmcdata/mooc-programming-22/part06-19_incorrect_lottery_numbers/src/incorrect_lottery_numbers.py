def validate_week(week_num: str):
    error = False
    try:
        week_num = int(week_num)
    except ValueError:
        error = True
    return error


def validate_if_number(numbers: list):
    error = False
    # remove duplicates
    numbers = set(numbers)

    if len(numbers) != 7:
        error = True
    else:
        for num in numbers:
            try:
                num = int(num)
                if int(num) < 1 or int(num) > 39:
                    error = True
            except ValueError:
                error = True
    return error


def write_numbers(numbers: dict):
    with open('correct_numbers.csv', 'w') as file:
        for week_num, nums in numbers.items():

            file.write(f"week {week_num};")
            for i in range(0, len(nums)):
                if i != len(nums) - 1:
                    file.write(f"{nums[i]},")
                else:
                    file.write(f"{nums[i]}\n")


def filter_incorrect():
    numbers_dict = {}
    with open('lottery_numbers.csv') as file:
        for line in file:
            line = line.strip()
            parts = line.split(';')

            week_num_parts = parts[0].split(' ')
            week_num = week_num_parts[1]
            if validate_week(week_num):
                week_num = 'invalid week'

            numbers = parts[1].split(',')
            if validate_if_number(numbers):
                numbers = 'invalid numbers'

            if (week_num != 'invalid week' and
                    numbers != 'invalid numbers'):
                numbers_dict[week_num] = numbers

            write_numbers(numbers_dict)


if __name__ == '__main__':
    filter_incorrect()
