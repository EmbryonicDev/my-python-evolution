# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        my_sum = sum(self.numbers)
        length = len(self.numbers)
        return my_sum / length if length > 0 else 0


def main():
    results = NumberStats()
    even_numbers = NumberStats()
    odd_numbers = NumberStats()
    print('Please type in integer numbers:')
    while True:
        number = int(input())
        if number == - 1:
            break
        results.add_number(number)
        even_numbers.add_number(
            number) if number % 2 == 0 else odd_numbers.add_number(number)

    print(f"Sum of numbers: {results.get_sum()}")
    print(f"Mean of numbers: {results.average()}")
    print(f"Sum of even numbers: {even_numbers.get_sum()}")
    print(f"Sum of odd numbers: {odd_numbers.get_sum()}")


main()
