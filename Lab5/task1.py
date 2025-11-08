#словник співробітників
employees = {
    "Іванов": "вул. Центральна, 15",
    "Петров": "вул. Київська, 22",
    "Сидоров": "вул. Шевченка, 44",
    "Кузін": "вул. Грушевського, 11",
    "Куравльов": "вул. Козацька, 9",
    "Кудін": "вул. Миру, 5",
    "Кульков": "вул. Соборна, 18",
    "Кубиків": "вул. Хрещатик, 2",
    "Семенов": "вул. Франка, 30",
    "Гринчук": "вул. Лесі Українки, 7"
}

#список прізвищ, які треба знайти
target = ["Кузін", "Куравльов", "Кудін", "Кульков", "Кубиків"]

#вивести всі записи
def Show():
    if not employees:
        print("Словник порожній.")
        return

    print("\n===== Всі співробітники =====")
    for surname, address in employees.items():
        print(f"{surname}: {address}")


#додавання запису
def Add():
    surname = input("Введіть прізвище співробітника: ").strip()
    address = input("Введіть адресу співробітника: ").strip()

    if not surname or not address:
        print("Прізвище та адреса не можуть бути порожні.")
        return

    if surname in employees:
        print("Такий співробітник вже існує.")
        print("1 - Перезаписати)")
        print("2 - Відмінити")
        try:
            ch = int(input("Ваш вибір: "))
        except:
            print("Помилка.")
            return

        if ch == 2:
            print("Додавання скасовано.")
            return

    employees[surname] = address
    print("Співробітника успішно додано.")


#видалення запису
def Delete():
    if not employees:
        print("Словник порожній.")
        return

    surname = input("Введіть прізвище співробітника для видалення: ").strip()

    if surname not in employees:
        print("Співробітника з таким прізвищем не знайдено.")
        return

    confirm = input(f"Ви впевнені, що хочете видалити '{surname}'? (так/ні): ").lower()
    if confirm == "так":
        employees.pop(surname)
        print("Запис видалено.")
    else:
        print("Видалення скасовано.")


#сортування за прізвищем
def Sorted():
    if not employees:
        print("Словник порожній.")
        return

    search = input("Введіть прізвище для пошуку: ").strip()
    if not search:
        print("Порожній ввід. Скасовано.")
        return

    sorted_keys = sorted(employees.keys())

    found_key = None
    for k in sorted_keys:
        if k.lower() == search.lower():
            found_key = k
            break

    if found_key:
        print("\n===== Знайдено =====")
        print(f"{found_key}: {employees[found_key]}")
    else:
        print(f"Прізвища '{search}' у словнику не знайдено.")

#завдання програми
def FindTarget():
    print("\n===== Перевірка прізвищ за умовою =====")

    found = False
    for name in target:
        if name in employees:
            found = True
            print(f"{name} працює у фірмі. Адреса: {employees[name]}")

    if not found:
        print("Жодного з цих співробітників у фірмі не знайдено.")

#меню
while True:
    print("\n========== МЕНЮ ==========")
    print("1 - Додати співробітника")
    print("2 - Видалити співробітника")
    print("3 - Вивести всіх співробітників")
    print("4 - Пошук співробітника за прізвищем")
    print("5 - Перевірити задані прізвища")
    print("6 - Завершити програму")

    try:
        choice = int(input("Оберіть пункт: "))
    except:
        print("Некоректне введення.")
        continue

    match choice:
        case 1:
            Add()
        case 2:
            Delete()
        case 3:
            Show()
        case 4:
            Sorted()
        case 5:
            FindTarget()
        case 6:
            print("Роботу завершено.")
            break
        case _:
            print("Невірний вибір меню.")