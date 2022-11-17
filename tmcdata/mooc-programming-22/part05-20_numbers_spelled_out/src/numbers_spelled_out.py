def dict_of_numbers():
    counter = 1
    numbers = {0: 'zero'}
    small_nums = ['one', 'two', 'three', 'four',
                  'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
             'fifteen', 'sixteen', 'seventeen',       'eighteen', 'nineteen']
    twenty_plus = ['twenty', 'thirty', 'forty',
                   'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    # 0 - 9
    for number in small_nums:
        numbers[counter] = number
        counter += 1

    # 10 - 19
    for number in teens:
        numbers[counter] = number
        counter += 1

    # my solution
    # 20 - 99
    # for big_num in twenty_plus:
    #     for i in range(10):
    #       if counter % 10 == 0:
    #         numbers[counter] = big_num
    #       else:
    #         new_num = f"{big_num}-{small_nums[i-1]}"
    #         numbers[counter] = new_num
    #       counter += 1

    # alternatively - based on model solution:
    # 20 - 99
    for i in range(2, 10):
        numbers[i * 10] = twenty_plus[i - 2]
        for j in range(1, 10):
            numbers[i * 10 + j] = twenty_plus[i - 2] + "-" + small_nums[j - 1]

    return numbers


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
