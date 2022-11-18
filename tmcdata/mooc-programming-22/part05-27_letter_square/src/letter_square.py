layer = int(input("Layer: "))

alpha = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
index = layer - 1
my_range = index
level = 1
half_list = [alpha[index] * layer]

# create first half of each required string & push to list
for i in range(index):
    temp_str = half_list[-1][0:level]

    for i in range(my_range):
        temp_str += alpha[index - level]
    half_list.append(temp_str)

    level += 1
    my_range -= 1

# create reversed version of half_list & remove first letter
reversed_half_list = []
for item in half_list:
    item = item[0:-1]
    reversed_half_list.append(item[::-1])

# combine half list & reverse list for final str
combined_list = []
for i in range(0, layer):
    temp_str = half_list[i] + reversed_half_list[i]
    combined_list.append(temp_str)

# prepare combined list for final submission
  # append combined list with reversed order of combined list (except last index)
for i in range(index - 1, -1, -1):
    combined_list.append(combined_list[i])

# print combined list values
for string in combined_list:
    print(string)
