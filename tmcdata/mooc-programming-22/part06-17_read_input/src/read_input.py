def read_input(user_prompt: str, min_num: int, max_num: int):
    while True:
        try:
            number = int(input(f"{user_prompt}"))
            if min_num < number < max_num:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {min_num} and {max_num}")


if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
