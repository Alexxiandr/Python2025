def insert():
    a = input("Введіть список через пробіл: ").split()
    print("Початковий список:", a)

    new = input("Введіть новий елемент для вставки: ")
    target = input(f'Введіть елемент, перед яким треба вставити "{new}": ')

    result = []

    for item in a:
        if item == target:
            result.append(new)

        result.append(item)

    print("Оновлений список:", result)
    return result

insert()