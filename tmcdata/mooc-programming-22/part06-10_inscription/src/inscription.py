def main():
    name = input("Whom should i sign this to: ")
    save_location = input("Where shall I save it: ")

    with open(save_location, 'w') as file:
        file.write(
            f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")


main()
