def mean(list):
    return float(sum(list)  / len(list))

# test code
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)