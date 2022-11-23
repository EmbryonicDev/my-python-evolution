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


if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)
