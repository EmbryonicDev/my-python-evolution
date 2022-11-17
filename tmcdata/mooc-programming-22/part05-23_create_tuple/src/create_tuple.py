def create_tuple(x: int, y: int, z: int):
  # function returns a tuple formed from parameters (smallest, greatest, sum)
    temp_list = [x, y, z]
    new_tuple = (min(temp_list), max(temp_list), sum(temp_list))
    return new_tuple


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
