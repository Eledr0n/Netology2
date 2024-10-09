def load_recipes_from_file(filename):
    "Чтение из файла и вохвращает в словарь"
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
    "Сохранение из словаря в файл"
    with open(filename, 'w') as file:
        for dish_name, ingredients in cook_book.items():
            file.write(f"{dish_name}\n")
            file.write(f"{len(ingredients)}\n")
            for ingredient in ingredients:
                file.write(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}\n")


def show_recipe(cook_book, dish_name):
    "Показать рецепт по названию"
    recipe = cook_book.get(dish_name)
    if recipe:
        print(f"\nРецепт для {dish_name}:")
        for ingredient in recipe:
            print(f"{ingredient['ingredient_name']} — {ingredient['quantity']} {ingredient['measure']}")
    else:
        print(f"Рецепт {dish_name} не найден.")


def add_new_recipe(cook_book):
    "Добавление рецепта"
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
    "Отобразить словарь"
    if cook_book:
        print("\nКулинарная книга:")
        for dish_name, ingredients in cook_book.items():
            print(f"\n{dish_name}:")
            for ingredient in ingredients:
                print(f"  {ingredient['ingredient_name']} — {ingredient['quantity']} {ingredient['measure']}")
    else:
        print("Кулинарная книга пуста.")


def display_menu():
    "Меню"
    print("\n1. Показать рецепт")
    print("2. Добавить рецепт")
    print("3. Показать все рецепты")
    print("4. Сохранить и выйти")
    return input("Выберите действие: ")


def main(filename):
    "Добавление блюда"
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
            save_recipes_to_file(filename, cook_book)
            print("Рецепты сохранены. Выход.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main('recipes.txt')
