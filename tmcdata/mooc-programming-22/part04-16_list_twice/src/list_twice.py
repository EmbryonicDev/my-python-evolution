items = []
while True:
    new_item = int(input("New item: "))
    if new_item == 0:
        break
    items.append(new_item)
    print(f"The list now: {items}")
    print(f"The list in order: {sorted(items)} ")
print("Bye!")
