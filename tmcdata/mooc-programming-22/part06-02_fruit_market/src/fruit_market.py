def read_fruits():
    with open('fruits.csv') as new_file:
        fruit_prices = {}
        for line in new_file:
            # split line to 2 pieces
            parts = line.split(';')
            # name first, price second
            fruit_prices[parts[0]] = float(parts[1])
    return fruit_prices


if __name__ == "__main__":
    print(read_fruits())
