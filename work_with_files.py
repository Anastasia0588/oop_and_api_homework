def read_cook_book():  # Задача №1
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


def get_shop_list_by_dishes(dishes, person_count):  # Задача #2
    cook_book = read_cook_book()
    shop_list = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list


print(get_shop_list_by_dishes(['Фахитос', 'Фахитос'], 3))


def open_all_files():  # Задача 3
    file_information = []
    for i in range(1, 4):
        with open(f'pyapi_homework/{i}.txt', encoding='utf-8') as f:
            lines_list = f.readlines()
            file_information.append({
                'file': f'{i}.txt',
                'lines_count': str(len(lines_list)),
                'text': lines_list})
    file_information.sort(key=lambda item: item['lines_count'])
    with open('all_files_info.txt', 'a', encoding='utf-8') as output:
        for data in file_information:
            output.write(f'{data['file']}\n')
            output.write(f'{data['lines_count']}\n')
            for line in data['text']:
                output.write(f'{line}')
            output.write("\n")


open_all_files()
