def load_recipes_from_file(filename):
    "Чтение списка"
    recipes = {}
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
                        'name': name,
                        'amount': amount,
                        'unit': unit
                    })

                recipes[dish_name] = ingredients

    except FileNotFoundError:
        print(f"Файл {filename} не найден.")

    return recipes


def save_recipes_to_file(filename, recipes):
    "Сохранение в файл"
    with open(filename, 'w') as file:
        for dish_name, ingredients in recipes.items():
            file.write(f"{dish_name}\n")
            file.write(f"{len(ingredients)}\n")
            for ingredient in ingredients:
                file.write(f"{ingredient['name']} | {ingredient['amount']} | {ingredient['unit']}\n")


def show_recipe(recipes, dish_name):
    "Показывает рецепт по названию"
    recipe = recipes.get(dish_name)
    if recipe:
        print(f"\nРецепт для {dish_name}:")
        for ingredient in recipe:
            print(f"{ingredient['name']} — {ingredient['amount']} {ingredient['unit']}")
    else:
        print(f"Рецепт {dish_name} не найден.")


def add_new_recipe(recipes):
    "Добавление рецепта"
    dish_name = input("Введите название блюда: ")
    if dish_name in recipes:
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
            'name': name,
            'amount': amount,
            'unit': unit
        })

    recipes[dish_name] = ingredients
    print(f"Рецепт для {dish_name} успешно добавлен.")


def display_menu():
    "Меню"
    print("\n1. Показать рецепт")
    print("2. Добавить рецепт")
    print("3. Сохранить и выйти")
    return input("Выберите действие: ")


def main(filename):
    """Основная функция программы."""
    recipes = load_recipes_from_file(filename)

    while True:
        choice = display_menu()

        if choice == '1':
            dish_name = input("Введите название блюда: ")
            show_recipe(recipes, dish_name)
        elif choice == '2':
            add_new_recipe(recipes)
        elif choice == '3':
            save_recipes_to_file(filename, recipes)
            print("Рецепты сохранены. Выход.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main('recipes.txt')
