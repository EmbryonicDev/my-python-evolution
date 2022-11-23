def get_recipes(filename: str):
    recipes_list = []
    temp_list = []
    with open(filename) as file:
        for line in file:
            if line == '\n':
                # append a copy of temp list to recipes list
                recipes_list.append(temp_list[:])
                temp_list.clear()
            else:
                temp_list.append(line.strip())
    # append final recipe before returning recipe list
    recipes_list.append((temp_list[:]))
    return recipes_list


def search_by_name(filename: str, word: str):
    recipes = get_recipes(filename)
    found_recipes = []
    # push found recipe name to found_recipes
    for recipe in recipes:
        if word in recipe[0].lower():
            found_recipes.append(recipe[0])
    return found_recipes


def search_by_time(filename: str, prep_time: int):
    recipes = get_recipes(filename)
    recipe_with_time = []
    # push recipe with time to recipe_with_time if prep time <= prep_time
    for recipe in recipes:
        if int(recipe[1]) <= prep_time:
            list_value = f"{recipe[0]}, preparation time {recipe[1]} min"
            recipe_with_time.append(list_value)
    return recipe_with_time

if __name__ == "__main__":
    # part 1
    print('Part 1')
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)

    # part 2
    print('Part 2')
    found_recipes = search_by_time("recipes1.txt", 20)
    for recipe in found_recipes:
        print(recipe)