item_count = int(input("How many items: "))
counter = 1
list = []
while counter <= item_count:
    value = int(input(f"Item {counter}: "))
    list.append(value)
    counter += 1
print(list)
