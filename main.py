def load_recipes_from_file(filename):
    "Читает список рецептов из файла и возвращает словарь cook_book."
    cook_book = {}
    try:
        with open(filename, 'r') as file:
            while True:
                dish_name = file.readline().strip()
                if not dish_name:
                    break

                num_ingredients = int(file.readline().strip())
                ingredients = []

                for _ in range(num_ingredients):
                    ingredient_line = file.readline().strip()
                    name, amount, unit = ingredient_line.split(' | ')
                    ingredients.append({
                        'ingredient_name': name,
                        'quantity': float(amount),
                        'measure': unit
                    })

                cook_book[dish_name] = ingredients

    except FileNotFoundError:
        print(f"Файл {filename} не найден.")

    return cook_book


def save_recipes_to_file(filename, cook_book):
    with open(filename, 'w') as file:
        for dish_name, ingredients in cook_book.items():
            file.write(f"{dish_name}\n")
            file.write(f"{len(ingredients)}\n")
            for ingredient in ingredients:
                file.write(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}\n")


def show_recipe(cook_book, dish_name):
    "Пункт 1"
    recipe = cook_book.get(dish_name)
    if recipe:
        print(f"\nРецепт для {dish_name}:")
        for ingredient in recipe:
            print(f"{ingredient['ingredient_name']} — {ingredient['quantity']} {ingredient['measure']}")
    else:
        print(f"Рецепт {dish_name} не найден.")


def add_new_recipe(cook_book):
    "Пункт 2"
    dish_name = input("Введите название блюда: ")
    if dish_name in cook_book:
        print("Рецепт с таким названием уже существует.")
        return

    try:
        num_ingredients = int(input("Введите количество ингредиентов: "))
    except ValueError:
        print("Количество ингредиентов должно быть числом.")
        return

    ingredients = []
    for _ in range(num_ingredients):
        name = input("Название ингредиента: ")
        try:
            amount = float(input("Количество: "))
        except ValueError:
            print("Количество должно быть числом.")
            return
        unit = input("Единица измерения: ")
        ingredients.append({
            'ingredient_name': name,
            'quantity': amount,
            'measure': unit
        })

    cook_book[dish_name] = ingredients
    print(f"Рецепт для {dish_name} успешно добавлен.")


def display_cook_book(cook_book):
    "Пункт 3"
    if cook_book:
        print("\nКулинарная книга:")
        for dish_name, ingredients in cook_book.items():
            print(f"\n{dish_name}:")
            for ingredient in ingredients:
                print(f"  {ingredient['ingredient_name']} — {ingredient['quantity']} {ingredient['measure']}")
    else:
        print("Кулинарная книга пуста.")


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    "Пункт 4"
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count  # Умножаем количество на число персон
                measure = ingredient['measure']

                if name in shop_list:
                    # Если ингредиент уже есть в списке, увеличиваем его количество
                    shop_list[name]['quantity'] += quantity
                else:
                    # Если ингредиента еще нет, добавляем его
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо {dish} не найдено в кулинарной книге.")

    return shop_list


def display_shop_list(shop_list):
    "Отображение пункта 4"
    print("\nСписок покупок:")
    for name, info in shop_list.items():
        print(f"{name}: {info['quantity']} {info['measure']}")


def display_menu():
    "Меню"
    print("\n1. Показать рецепт")
    print("2. Добавить рецепт")
    print("3. Показать все рецепты")
    print("4. Получить список покупок")
    print("5. Сохранить и выйти")
    return input("Выберите действие: ")


def main(filename):
    cook_book = load_recipes_from_file(filename)

    while True:
        choice = display_menu()

        if choice == '1':
            dish_name = input("Введите название блюда: ")
            show_recipe(cook_book, dish_name)
        elif choice == '2':
            add_new_recipe(cook_book)
        elif choice == '3':
            display_cook_book(cook_book)
        elif choice == '4':
            dishes = input("Введите названия блюд через запятую: ").split(', ')
            try:
                person_count = int(input("Введите количество персон: "))
                shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
                display_shop_list(shop_list)
            except ValueError:
                print("Количество персон должно быть числом.")
        elif choice == '5':
            save_recipes_to_file(filename, cook_book)
            print("Рецепты сохранены. Выход.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main('recipes.txt')
