def find():
    while True:
        input_l = input('Введіть список чисел через пробіл: ')
        try:
            a = list(map(int, input_l.split()))
            break
        except ValueError:
            print("Введіть тільки числові дані.")

    print("Ваш список:", a)

    while True:
        input_n = input('Введіть число для пошуку: ')
        try:
            k = int(input_n)
            break
        except ValueError:
            print(f"'{input_n}' не є числом. Спробуйте ще раз.")

    result = []
    for i in range(len(a)):
        if a[i] == k:
            result.append(i)

    if result:
        print(f"Число {k} знайдено на індексах: {result}")
    else:
        print(f"Число {k} не знайдено.")

    return result

find()