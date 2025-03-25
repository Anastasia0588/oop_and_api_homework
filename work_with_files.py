def read_cook_book():
    cook_book = {}
    lines_list = []
    with open('recipes.txt', encoding="utf-8") as f:
        for line in f:
            lines_list.append(line.strip())
        dish = None
        for line in lines_list:
            if line == "" or line.isdigit():
                continue
            elif not line.isdigit() and "|" not in line:
                dish = line
                cook_book[dish] = []
            elif dish is not None:
                ingredient_list = line.strip().split("|")
                ingredient = {
                    'ingredient_name': ingredient_list[0].strip(),
                    'quantity': int(ingredient_list[1].strip()),
                    'measure': ingredient_list[2].strip()
                }
                cook_book[dish].append(ingredient)
    return cook_book


print(read_cook_book())


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book()
    shop_list = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            shop_list = {
                ingredient['ingredient_name']: {
                    'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count
                }
            }
            print(shop_list)
    return shop_list


print(get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 12))