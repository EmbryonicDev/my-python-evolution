def prime_numbers():
    def isprime(n):
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

    # generate the first 2000 prime numbers
    for i in range(2, 2001):
        if isprime(i):
            yield i


if __name__ == '__main__':
    numbers = prime_numbers()
    for i in range(30):
        print(next(numbers))

    # temp = [x for x in range(1, 100) if prime_numbers()]
    # print(temp)
