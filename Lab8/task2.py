import json
import os

employees_f = "employees.json"
result_f = "employees_result.json"

employees = [
    {"Surname": "Шевченко", "Address": "Київ, вул. Шевченка, 10", "Position": "Менеджер"},
    {"Surname": "Іванов", "Address": "Львів, вул. Франка, 7", "Position": "Програміст"},
    {"Surname": "Петренко", "Address": "Одеса, вул. Козацька, 12", "Position": "Дизайнер"},
    {"Surname": "Бондаренко", "Address": "Харків, вул. Сумська, 21", "Position": "Інженер"},
    {"Surname": "Коваленко", "Address": "Дніпро, просп. Свободи, 9", "Position": "HR-менеджер"},
    {"Surname": "Ткаченко", "Address": "Полтава, вул. Соборності, 33", "Position": "Бухгалтер"},
    {"Surname": "Кравченко", "Address": "Чернігів, вул. Миру, 5", "Position": "Розробник"},
    {"Surname": "Мороз", "Address": "Луцьк, вул. Лесі Українки, 4", "Position": "Аналітик"},
    {"Surname": "Мельник", "Address": "Вінниця, вул. Коцюбинського, 14", "Position": "Секретар"},
    {"Surname": "Зінченко", "Address": "Запоріжжя, просп. Соборний, 2", "Position": "Юрист"}
]

if not os.path.exists(employees_f):
    with open("employees.json", "w", encoding="utf-8") as f:
        json.dump(employees, f, ensure_ascii=False, indent=4)

def load_d():
    try:
        with open(employees_f, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл '{employees_f}' не знайдено")
        return []
    except json.JSONDecodeError:
        print(f"Файл '{employees_f}' пошкоджено або містить некоректний JSON")
        return []

def save_d(data):
    try:
        with open(employees_f, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Помилка запису у файл '{employees_f}': {e}")

def view_d():
    data = load_d()
    print("\nУсі співробітники:")
    for e in data:
        print(f"{e['Surname']} — {e['Position']} ({e['Address']})")


def add_employee():
    data = load_d()
    surname = input("Прізвище: ").title()
    address = input("Адреса: ")
    position = input("Посада: ")
    data.append({"Surname": surname, "Address": address, "Position": position})
    save_d(data)
    print("Запис додано")


def del_employee():
    data = load_d()
    surname = input("Введіть прізвище для видалення: ").title()
    new_data = [e for e in data if e["Surname"] != surname]
    if len(new_data) < len(data):
        save_d(new_data)
        print(f"Співробітника {surname} видалено.")
    else:
        print("Такого прізвища не знайдено.")


def find_letter():
    data = load_d()
    letter = input("Введіть початкову літеру прізвища: ").title()
    found = [e for e in data if e["Surname"].startswith(letter)]
    if found:
        print("\nЗнайдені співробітники:")
        for e in found:
            print(f"{e['Surname']} — {e['Address']} ({e['Position']})")
        with open(result_f, "w", encoding="utf-8") as f:
            json.dump(found, f, ensure_ascii=False, indent=4)
        print(f"Результати записано у '{result_f}'")
    else:
        print("Співробітників із такою літерою не знайдено.")

while True:
    print("\n Меню:")
    print("1 – Переглянути всі записи")
    print("2 – Додати запис")
    print("3 – Видалити запис")
    print("4 – Пошук за літерою прізвища")
    print("5 – Вихід")

    choice = input("Оберіть опцію: ")

    if choice == "1":
        view_d()
    elif choice == "2":
        add_employee()
    elif choice == "3":
        del_employee()
    elif choice == "4":
        find_letter()
    elif choice == "5":
        print("Вихід із програми.")
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")